from selenium.webdriver.common.by import By
import time

# Función principal Login 
def login(driver):
    
    # Accedo a la página
    driver.get("https://www.saucedemo.com/")
    
    # Cargar el usuario
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    
    # Cargar la contraseña
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    
    # Click sobre el boton para hacer el login
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)