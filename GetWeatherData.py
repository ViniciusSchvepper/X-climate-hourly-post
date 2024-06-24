from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.tempo.com/jaragua-do-sul.htm")

row = driver.find_element(By.XPATH, "//tr[contains(@class, '')]")

horario = row.find_element(By.XPATH, ".//span[@class='text-princ']").text
print("Horário:", horario)

temperatura = row.find_element(By.XPATH, ".//td[@class='title-mod changeUnitT']").text
print("Temperatura:", temperatura)

descricao = row.find_element(By.XPATH, ".//td[@class='descripcion']/strong").text
print("Descrição:", descricao)

velocidade_vento = row.find_element(By.XPATH, ".//div[@class='row wind']/span[@class='velocidad col']").text
print("Velocidade do Vento:", velocidade_vento)

indice_uv = row.find_element(By.XPATH, ".//span[@class='row']//span[@class='col velocidad']/strong").text
print("Índice UV:", indice_uv)

driver.quit()