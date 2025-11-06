import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.login_page import LoginPage

# Archivo Global

# Abre chrome como incognito y desactiva popup de contraseña filtrada
@pytest.fixture
def driver():
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()

# Función para inciar Sesión
@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina().login_completo(usuario,password)
    return driver