import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def inicializar_driver():
    """
    Inicializa o driver do Selenium configurado para o Chrome.
    """
    try:
        logging.info("Inicializando o driver do Chrome...")
        options = Options()
        options.add_argument("--start-maximized") 
        options.add_argument("--disable-notifications") 
        options.add_argument("--disable-infobars")  
        options.add_argument("--disable-popup-blocking") 
        options.add_argument("--log-level=3")
            
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        logging.info("Driver inicializado!")
        return driver
    except Exception as e:
        logging.error(f"Error na inicialização do driver!: {e}")
        raise RuntimeError("Falha ao inciar o ChromeDriverManager") from e
    
