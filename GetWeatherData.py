from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_weather_data() -> str:
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    service = ChromeService(executable_path = ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.get("https://www.tempo.com/jaragua-do-sul.htm")

    row = driver.find_element(By.XPATH, "//tr[contains(@class, '')]")

    day_time = row.find_element(By.XPATH, ".//span[@class='text-princ']").text
    temp_in_celsius = row.find_element(By.XPATH, ".//td[@class='title-mod changeUnitT']").text
    description = row.find_element(By.XPATH, ".//td[@class='descripcion']/strong").text
    wind_speed = row.find_element(By.XPATH, ".//div[@class='row wind']/span[@class='velocidad col']").text.replace('\n', ' ')
    uv_index = row.find_element(By.XPATH, ".//span[@class='row']//span[@class='col velocidad']/strong").text
    
    string_result = f"Horario: {day_time} \n Temperatura: {temp_in_celsius} \n Descrição: {description} \n Variação da velocidade do vento: {wind_speed} \n Indice Uv: {uv_index}"
    driver.quit()

    return string_result