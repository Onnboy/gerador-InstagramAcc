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
    time.sleep(random.uniform (min_delay, max_delay))
    
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
    # Localiza, limpa e preenche um campo no formulário.
    for tentativa in range(max_tentativas):
        """Realiza o cadastro automatizado"""
        try:
            logging.info(f"Tentativa {tentativa + 1} de preenchimento...")
            
            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "emailOrPhone"))
            )
            if not email_field:
                raise ValueError("Campo de e-mail não encontrado")
            email_field.clear()
            email_field.send_keys(email)
            email_valor = email_field.get_attribute("value")
            logging.info(f"Campo 'E-mail' preenchido com: {email_valor}")
            delay(2, 3)

            full_name_field = driver.find_element(By.NAME, "fullName")
            if not full_name_field:
                raise ValueError("Campo de nome completo não encontrado")
            full_name_field.clear()
            full_name_field.send_keys(full_name)
            full_name_valor = full_name_field.get_attribute("value")
            logging.info(f"Campo 'Nome completo' preenchido com: {full_name_valor}")
            delay(2, 3)

            username_field = driver.find_element(By.NAME, "username")
            if not username_field:
                raise ValueError("Campo de nome de usuario não encontrado")
            username_field.clear()
            username_field.send_keys(username)
            username_valor = username_field.get_attribute("value")
            logging.info(f"Campo 'Nome de usuario': {username_valor}")
            delay(2, 3)

            password_field = driver.find_element(By.NAME, "password")
            if not password_field:
                raise ValueError("Campo de senha não encontrado")
            password_field.clear()
            password_field.send_keys(password)
            password_valor = password_field.get_attribute("value")
            logging.info(f"Campo 'Senha' preenchida com: {password_valor}")
            delay(2, 3)

            logging.info("Campos preenchidos com sucesso!")
            delay(2, 3)
            
            return True
            
        except Exception as e:
            logging.error(f"Error ao preencher os campos!: {e}")
            return False
    logging.error("Falha após múltiplas tentativas de preenchimento!")
    return False


def enviar_formulario(driver):
    # Utiliza a função genérica para clicar no botão de cadastro.
    try:
        delay(2, 3)
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cadastre-se')]"))
        )
        signup_button.click()
        logging.info("Cadastro enviado com sucesso!")
        return True
    except Exception as e:
        logging.error(f"Error ao enviar cadastro!: {e}")
        return False