from selenium.webdriver.common.by import By
from selenium import webdriver

# Test del Login
def test_login_validation(login_in_driver):
    try:
        # Dentro de una variable cargo la función del login
        driver = login_in_driver

        # Comprueba que carga la página del inventario
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
    
