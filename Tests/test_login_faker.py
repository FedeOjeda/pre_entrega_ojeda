from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from faker import Faker 
from Pages.login_page import LoginPage

fake = Faker()    

# Test del Login con Faker
@pytest.mark.parametrize("usuario,password,debe_funcionar",[
    (fake.user_name(),fake.password(),False),
    (fake.user_name(),fake.password(),False),
    
])
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    driver = login_in_driver

    if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
    elif debe_funcionar == False:
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"