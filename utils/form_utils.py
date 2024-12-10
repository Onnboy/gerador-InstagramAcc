from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import random
import time

def delay(min_delay=2, max_delay=5):
    """
    Função para atrasos aleatórios.
    """
    time.sleep(random.uniform(min_delay, max_delay))
    
def preencher_campo(driver, by, locator, valor, tempo_espera=10):
    # Localiza, limpa e preenche um campo no formulário.
    try:
        campo = WebDriverWait(driver, tempo_espera).until(
            EC.visibility_of_element_located((by, locator))
        )
        campo.clear()
        campo.send_keys(valor)
        logging.info(f"Campo '{locator}' preenchido com: {valor}")
        return True
    except Exception as e:
        logging.error(f"Erro ao preencher o campo '{locator}': {e}")
        return False

def auto_cadastro(driver, email, username, full_name, password, max_tentativas=4):
    # Realiza o cadastro automatizado com tentativas.
    for tentativa in range(max_tentativas):
        try:
            logging.info(f"Tentativa '{tentativa + 1}' de preenchimento...")
            
            if not preencher_campo(driver, By.NAME, "emailOrPhone", email):
                logging.error("Falha ao preencher o e-mail ou telefone")
                return False
            delay(3, 5)
            
            if not preencher_campo(driver, By.NAME, "fullName", full_name):
                logging.error("Falha ao preencher o nome completo")
                return False
            delay(3, 5)
            
            if not preencher_campo(driver, By.NAME, "username", username):
                logging.error("Falha ao preencher o nome de usuário")
                return False
            delay(3, 5)
            
            if not preencher_campo(driver, By.NAME, "password", password):
                logging.error("Falha ao preencher a senha")
                return False
            delay(3, 5)
            
            logging.info("Campos preenchidos com sucesso!")
            return True
        except Exception as e:
            logging.error(f"Erro na tentativa '{tentativa + 1}': {e}")
            continue
    logging.error("Falha após múltiplas tentativas de preenchimento!")
    return False

def clicar_botao(driver, by, locator, tempo_espera=10):
    #Clica em um botão identificado pelo localizador fornecido.
    try:
        botao = WebDriverWait(driver, tempo_espera).until(
            EC.element_to_be_clickable((by, locator))
        )
        delay(3, 5)
        botao.click()
        logging.info(f"Botão '{locator}' clicado com sucesso!")
        return True
    except Exception as e:
        logging.error(f"Erro ao clicar no botão '{locator}': {e}")
        return False

def enviar_formulario(driver):
    # Utiliza a função genérica para clicar no botão de cadastro.
    return clicar_botao(driver, By.XPATH, "//button[contains(text(), 'Cadastre-se')]")