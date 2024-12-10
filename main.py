import logging, log_config
from utils.form_utils import delay
from selenium.webdriver.common.by import By
from utils.driver_utils import inicializar_driver
from selenium.webdriver.support.ui import WebDriverWait
from utils.data_utils import gerar_auto_cadastro_aleatorio
from utils.form_utils import auto_cadastro, enviar_formulario
from selenium.webdriver.support import expected_conditions as EC

def acessar_pagina(driver, url, tentativas=3):
    logging.info(f"Acessando a pagina: {url}")
    for tentativa in range (tentativas):
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME,'body')))
            logging.info(f"Página carregada com sucesso!: {url}")
            delay(3, 5)
            return True
        except Exception as e:
            logging.warning(f"Tentativa {tentativa + 1} falhou ao carregar {url}: {e}")
        logging.error(f"Não foi possivel carregar a pagina após {tentativas} tentativas...")
        return False
    
def main():
    logging.info("Iniciando o processo de cadastro automatizado...")
    
    driver = None
    try:
        driver = inicializar_driver()
        url = "https://www.instagram.com/accounts/emailsignup/"  # Certifique-se de que a URL está correta
        
        if not acessar_pagina(driver, url):
            logging.fatal("Falha ao carregar a pagina. Encerrando o programa")
            return
        
        email, username, full_name, password = gerar_auto_cadastro_aleatorio()
        logging.info(f"Dados gerados:\nEmail: {email}\nUsername: {username}\nFull Name: {full_name}\nPassword: {password}")

        if not auto_cadastro(driver, email, username, full_name, password):
            logging.fatal("Falha ao preencer o cadastro. Encerrando o programa")
            return 
        
        if not enviar_formulario(driver):
            logging.fatal("Falha ao enviar o cadastro. Encerrando o programa")
            return
        
        logging.info("Processo de cadastro finalizado!")
    except Exception as e:
        logging.fatal(f"Fatal error!: {e}")
    finally:
        if driver:
            driver.quit()
            logging.info("Driver encerrado!")
            
if __name__ == "__main__":
    main()