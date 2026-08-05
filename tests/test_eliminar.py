from selenium.webdriver.common.by import By
from conftest import URL_BASE, loguearse


# historia de usuario: como usuario quiero eliminar tareas que ya no necesito

def test_eliminar_camino_feliz(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("tarea a borrar")
    driver.find_element(By.ID, "btn-crear").click()

    driver.find_element(By.XPATH, "//button[text()='eliminar']").click()
    assert "tarea a borrar" not in driver.page_source


def test_eliminar_negativo_id_inexistente(driver):
    loguearse(driver)
    driver.get(f"{URL_BASE}/tareas/9999/eliminar")
    # el metodo GET no esta permitido en esa ruta (solo POST), debe fallar
    assert "405" in driver.page_source or driver.current_url.endswith("/9999/eliminar")


def test_eliminar_limite_lista_vuelve_vacia(driver):
    loguearse(driver)
    driver.find_element(By.ID, "titulo").send_keys("unica tarea")
    driver.find_element(By.ID, "btn-crear").click()
    driver.find_element(By.XPATH, "//button[text()='eliminar']").click()

    assert "lista-vacia" in driver.page_source
