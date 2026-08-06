from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
from conftest import URL_BASE, loguearse


# historia de usuario: como usuario quiero eliminar tareas que ya no necesito

def test_eliminar_camino_feliz(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("tarea a borrar")
    driver.find_element(By.ID, "btn-crear").click()

    driver.find_element(By.XPATH, "//button[text()='eliminar']").click()
    WebDriverWait(driver, 5).until(lambda d: "tarea a borrar" not in d.page_source)
    assert "tarea a borrar" not in driver.page_source


def test_eliminar_negativo_id_inexistente(driver):
    loguearse(driver)
    # este endpoint solo acepta POST, probamos con GET directo (sin pasar por el navegador)
    # usando las cookies de la sesion ya logueada, para revisar el codigo de respuesta real
    cookies = {c["name"]: c["value"] for c in driver.get_cookies()}
    respuesta = requests.get(f"{URL_BASE}/tareas/9999/eliminar", cookies=cookies)
    assert respuesta.status_code == 405


def test_eliminar_limite_lista_vuelve_vacia(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("unica tarea")
    driver.find_element(By.ID, "btn-crear").click()
    driver.find_element(By.XPATH, "//button[text()='eliminar']").click()

    WebDriverWait(driver, 5).until(lambda d: "lista-vacia" in d.page_source)
    assert "lista-vacia" in driver.page_source
