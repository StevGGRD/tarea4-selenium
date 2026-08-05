from selenium.webdriver.common.by import By
from conftest import URL_BASE, loguearse


# historia de usuario: como usuario quiero crear tareas para organizarme

def test_crear_camino_feliz(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("comprar comida")
    driver.find_element(By.ID, "btn-crear").click()

    assert "comprar comida" in driver.page_source


def test_crear_negativo_titulo_vacio(driver):
    loguearse(driver)
    driver.find_element(By.ID, "btn-crear").click()

    error = driver.find_element(By.ID, "error-tarea")
    assert "vacio" in error.text


def test_crear_limite_titulo_largo(driver):
    loguearse(driver)
    titulo_largo = "a" * 150  # el limite en el backend es 100 caracteres
    driver.find_element(By.ID, "titulo").send_keys(titulo_largo)
    driver.find_element(By.ID, "btn-crear").click()

    error = driver.find_element(By.ID, "error-tarea")
    assert "largo" in error.text
