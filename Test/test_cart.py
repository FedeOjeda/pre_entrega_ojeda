from selenium.webdriver.common.by import By
from selenium import webdriver

# Test del Carrito de Compra
def test_cart(login_in_driver):
    try:
        # Dentro de una variable cargo la función del login
        driver = login_in_driver

        # Cargar productos a partir del elemento nombre 
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
    
        # Seleccionar el primer producto a partir de su botón correspondiente 
        productos[0].find_element(By.TAG_NAME,"button").click()
    
        # Validación del la carga del producto
        carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        assert carrito == "1","No hay productos cargados en el carrito."
        
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    
    finally:
        driver.quit()