from selenium.webdriver.common.by import By
from conftest import URL_BASE, loguearse


# historia de usuario: como usuario quiero editar una tarea para corregir el titulo

def test_actualizar_camino_feliz(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("titulo viejo")
    driver.find_element(By.ID, "btn-crear").click()

    driver.find_element(By.LINK_TEXT, "editar").click()
    campo = driver.find_element(By.ID, "titulo")
    campo.clear()
    campo.send_keys("titulo nuevo")
    driver.find_element(By.ID, "btn-guardar").click()

    assert "titulo nuevo" in driver.page_source


def test_actualizar_negativo_id_inexistente(driver):
    loguearse(driver)
    driver.get(f"{URL_BASE}/tareas/9999/editar")
    mensaje = driver.find_element(By.ID, "mensaje-error")
    assert "no encontrada" in mensaje.text


def test_actualizar_limite_titulo_vacio_no_cambia(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("no me borres")
    driver.find_element(By.ID, "btn-crear").click()

    driver.find_element(By.LINK_TEXT, "editar").click()
    campo = driver.find_element(By.ID, "titulo")
    campo.clear()
    driver.find_element(By.ID, "btn-guardar").click()

    # el backend ignora el titulo vacio, la tarea original debe seguir
    assert "no me borres" in driver.page_source
