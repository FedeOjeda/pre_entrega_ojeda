import logging
import pathlib

# Creamos la Carpeta
audit_dir = pathlib.Path('Logs')
audit_dir.mkdir(exist_ok=True)

# Creamos el archivo
log_file = audit_dir/'Suite.log'

# Seteamos el archivo
logger = logging.getLogger("TalentoTech")
logger.setLevel(logging.INFO)

# Verificamos que no haya duplicados a la hora de correr el test
if not logger.handlers:
    file_handler = logging.FileHandler(log_file,mode="a",encoding="utf-8")
    formater = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)