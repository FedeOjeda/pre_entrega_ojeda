import pytest
from selenium import webdriver
from Utilites.utils import login

# Archivo Global

# Funciones para abrir y cerrar el navegador
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Función para inciar Sesión
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver