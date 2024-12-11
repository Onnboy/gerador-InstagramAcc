"""
Script principal para execução do robô de cadastro automatizado no Instagram.
"""

import time
import logging
import log_config
from utils.form_utils import delay
from selenium.webdriver.common.by import By
from utils.driver_utils import inicializar_driver
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_utils import gerar_auto_cadastro_aleatorio
from utils.form_utils import auto_cadastro, enviar_formulario
from selenium.webdriver.support import expected_conditions as EC

def main():
    #Função principal que coordena o processo de automação.
    start_time = time.time()
    logging.info("Iniciando o robo...")
    
    driver = None
    try:
        driver = inicializar_driver()
        email, username, fullname, password = gerar_auto_cadastro_aleatorio()
        
        url = "https://www.instagram.com/accounts/emailsignup/"  # Certifique-se de que a URL está correta
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.url_contains("accounts/emailsignup"))
        delay(2, 4)
        
        auto_cadastro(driver, email, username, fullname, password)
        enviar_formulario(driver)
        logging.info(f"Dados gerados:\nEmail: {email}\nUsername: {username}\nFull Name: {fullname}\nPassword: {password}")
        
        logging.info("Processo de cadastro finalizado!")
    except Exception as e:
        logging.fatal(f"Erro no script!: {e}")
    finally:
        if driver:
            driver.quit()
            logging.info("Driver encerrado!")
    total_time = time.time() - start_time
    logging.info(f'Tempo total de execução do script: {total_time:.2f} segundos')
            
if __name__ == "__main__":
    main()