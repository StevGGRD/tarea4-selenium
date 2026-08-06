import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os

URL_BASE = "http://localhost:5000"


@pytest.fixture(autouse=True)
def resetear_datos():
    # antes de cada prueba borro las tareas para que no queden
    # datos pegados de la prueba anterior
    requests.post(f"{URL_BASE}/test/reset")
    yield


@pytest.fixture
def driver():
    opciones = Options()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1280,900")
    navegador = webdriver.Chrome(options=opciones)
    navegador.implicitly_wait(5)  # espera hasta 5 seg si un elemento no aparece de una vez
    yield navegador
    navegador.quit()


def loguearse(driver):
    driver.get(f"{URL_BASE}/login")
    driver.find_element("id", "usuario").send_keys("admin")
    driver.find_element("id", "clave").send_keys("1234")
    driver.find_element("id", "btn-login").click()
    # espero a que la redireccion a /tareas termine antes de seguir
    WebDriverWait(driver, 5).until(lambda d: "/tareas" in d.current_url)


# esto toma una captura de pantalla automatica de cada prueba y la mete en el reporte html
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver is not None:
            os.makedirs("screenshots", exist_ok=True)
            nombre = f"screenshots/{item.name}.png"
            driver.save_screenshot(nombre)

            extra = getattr(report, "extra", [])
            try:
                import pytest_html
                extra.append(pytest_html.extras.image(nombre))
                report.extra = extra
            except Exception:
                pass
