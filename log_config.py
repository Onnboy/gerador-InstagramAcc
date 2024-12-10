import logging
from logging.handlers import RotatingFileHandler

# Configuração do logging
logging.basicConfig(
    level=logging.DEBUG,  # Alterado para DEBUG para capturar todos os tipos de log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato das mensagens de log
    handlers=[
        logging.StreamHandler(),  # Exibe os logs no terminal
        RotatingFileHandler('automation_log.log', maxBytes=5*1024*1024, backupCount=2)  # Grava os logs no arquivo
    ]
)