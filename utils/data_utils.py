import logging
from faker import Faker
import random
import string

def gerar_auto_cadastro_aleatorio():
    """
    Gera dados fictícios para cadastro automatizado.

    Retorna:
        tuple: Dados de cadastro no formato (email, username, full_name, password).
    """
    logging.info("Gerando dados fictícios para cadastro...")
    fake = Faker()
    dominios_validos = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']
    
    # Gerar email
    nome_local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    dominio = random.choice(dominios_validos)
    email = f"{nome_local}@{dominio}"
    
    # Gera um nome usuario seguindo padrões aceitos pelo instagram
    username = ''.join(random.choices(string.ascii_lowercase + string.digits + '._', k=12)).strip('._')
    
    # Nome completo ficticio
    full_name = fake.first_name() + " " + fake.last_name()
    
    # Gera uma senha robusta
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    
    logging.info(f"Dados gerados: Email={email}, Username={username}, FullName={full_name}, Password=****")
    if not (email and username and full_name and password):
        raise ValueError("Falha ao gerar dados de cadastro válidos")
    
    return email, username, full_name, password
    