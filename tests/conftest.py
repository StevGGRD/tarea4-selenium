import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

URL_BASE = "http://localhost:5000"


@pytest.fixture
def driver():
    opciones = Options()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1280,900")
    navegador = webdriver.Chrome(options=opciones)
    yield navegador
    navegador.quit()


def loguearse(driver):
    driver.get(f"{URL_BASE}/login")
    driver.find_element("id", "usuario").send_keys("admin")
    driver.find_element("id", "clave").send_keys("1234")
    driver.find_element("id", "btn-login").click()


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
