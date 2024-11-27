from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
usuario = os.getenv("LOGIN")
senha = os.getenv("SENHA")


print(f"Usuário carregado: {usuario}")
print(f"Senha carregada: {senha}")

# Configurar o WebDriver
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# Acessar a página
browser.get('https://caol.agence.com.br/index.php')

# Inserir login e senha
browser.find_element(By.XPATH, '//*[@id="edt_login"]').send_keys(usuario)
browser.find_element(By.XPATH, '//*[@id="pwd_senha"]').send_keys(senha)

# Clicar no botão de login
browser.find_element(By.XPATH, '//*[@id="cont_principal"]/div/form/fieldset/input[3]').click()

input("Pressione Enter para fechar o navegador...")
browser.quit()
