from selenium.webdriver.common.by import By
from conftest import URL_BASE


# historia de usuario: como usuario quiero iniciar sesion para acceder a mis tareas

def test_login_camino_feliz(driver):
    driver.get(f"{URL_BASE}/login")
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "clave").send_keys("1234")
    driver.find_element(By.ID, "btn-login").click()

    assert "/tareas" in driver.current_url


def test_login_negativo_clave_incorrecta(driver):
    driver.get(f"{URL_BASE}/login")
    driver.find_element(By.ID, "usuario").send_keys("admin")
    driver.find_element(By.ID, "clave").send_keys("clave-mala")
    driver.find_element(By.ID, "btn-login").click()

    error = driver.find_element(By.ID, "error-login")
    assert "incorrectos" in error.text


def test_login_limite_campos_vacios(driver):
    driver.get(f"{URL_BASE}/login")
    driver.find_element(By.ID, "btn-login").click()

    # como no llenamos nada, se queda en el login con error
    error = driver.find_element(By.ID, "error-login")
    assert "incorrectos" in error.text
