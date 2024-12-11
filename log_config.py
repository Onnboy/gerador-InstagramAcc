import logging
from logging.handlers import RotatingFileHandler

def configurar_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Alterar para DEBUG, se necessário.

    # Formato dos logs
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] (%(module)s): %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Arquivo de log rotativo
    file_handler = RotatingFileHandler(
        'automation_log.log', maxBytes=5_000_000, backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Remover duplicação de logs
    logging.getLogger().propagate = False

    logging.info("Logging configurado com sucesso!")

configurar_logging()