import requests
import pytest
from Utils.logger import logger

# Obtener usuario
def test_get_user(url_base,header_request):
    logger.info(f"Realizando la solicitud GEt a {url_base} ")
    response = requests.get(f"{url_base}/2",headers=header_request)
    
    logger.info(f"Status code: {response.status_code} ")
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    
    data = response.json()
    
    logger.info("Validando el id dentro del usuario")
    # Verificar que la clave "id = 2"
    assert data["data"]["id"] == 2
    
# Crear usuario
def test_create_user(url_base,header_request):
    payload = {
        "name":"Jose",
        "job": "Profesor" 
        }
    response = requests.post(url_base,headers=header_request,json=payload)
    
     # Verificar que la respuesta sea exitosa
    assert response.status_code == 201
    
    data = response.json()
    
    # Verificar que el nombre de la respuesta sea el mismo que el enviado
    assert data["name"] == payload["name"]
    
# Eliminar usuario
def test_delete_user(url_base,header_request):
    response = requests.delete(f"{url_base}/2",headers=header_request)
    
    # Verificar que la respuesta sea exitosa
    assert response.status_code == 204
    
    