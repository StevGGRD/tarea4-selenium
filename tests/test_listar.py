from selenium.webdriver.common.by import By
from conftest import URL_BASE, loguearse


# historia de usuario: como usuario quiero ver mis tareas para saber que tengo pendiente

def test_listar_camino_feliz(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("tarea de prueba")
    driver.find_element(By.ID, "btn-crear").click()

    lista = driver.find_element(By.ID, "lista-tareas")
    assert "tarea de prueba" in lista.text


def test_listar_negativo_sin_sesion(driver):
    # intentamos entrar a /tareas sin loguearnos primero
    driver.get(f"{URL_BASE}/tareas")
    assert "/login" in driver.current_url


def test_listar_limite_lista_vacia(driver):
    loguearse(driver)
    driver.get(f"{URL_BASE}/tareas")
    # como el servidor se reinicia entre corridas, puede estar vacia
    body = driver.page_source
    assert "lista-vacia" in body or "lista-tareas" in body
