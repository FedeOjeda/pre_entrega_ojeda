from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from Pages.inventory_page import InventoryPage

# Test de la página del Inventario
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver):
    try:
        # Dentro de una variable cargo la función del login
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"

        # Verificar vacio el carrito al inicio
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto
        inventory_page.agregar_primer_producto()

        # Verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito() == 1
    
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()
