import pytest

# Lista de archivos de test a ejecutar
test_files = [
    "Tests/test_login.py",
    "Tests/test_inventory.py",
    "Tests/test_cart.py",
    "Tests/test_cart_json.py",
    "Test/test_api_reqres.py"
    
]

# Argumentos para ejecutar las pruebas: archivos y creación del reporte HTML
pytest_args = test_files + ["--html=Reporte/report.html","--self-contained-html","-v"]

pytest.main(pytest_args)