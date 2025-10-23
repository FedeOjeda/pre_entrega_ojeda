import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilites.utils import login

# Archivo Global

# Funciones para abrir y cerrar el navegador
#@pytest.fixture
#def driver():
    #driver = webdriver.Chrome()
    #yield driver
    #driver.quit()

@pytest.fixture
def driver():
    #abre chrome como incognito y desactiva popup de contraseña filtrada
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()

# Función para inciar Sesión
@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver