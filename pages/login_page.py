from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    # URL - Punto de Entrada
    URL = "https://www.saucedemo.com/"
    
    # Localizador
    _USER_INPUT = (By.ID,"user-name")
    _PASS_INPUT = (By.ID,"password")
    _LOGIN_BUTTON = (By.ID, "login-button")
        
    # Función de Inicialización del Driver
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10) 
    
    # Función para abrir la página
    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    # Función para completar el usuario
    def completar_user(self,usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
        
    # Función para completar la contraseña
    def completar_pass(self,password):
        input = self.driver.find_element(*self._PASS_INPUT)
        input.clear()
        input.send_keys(password)
        return self
    
    # Función para hacer click en el botón
    def hacer_click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        
    # Función para ejecutar todas las funciones
    def login_completo(self,usuario,password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self
        