from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GetWeatherData import get_weather_data
import time

def MakePost(driver):
    string_result = get_weather_data()
    time.sleep
    post_input_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
    post_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, post_input_xpath))
    )
    post_input.send_keys(string_result)

    send_post_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button'
    send_post = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, send_post_button_xpath))
    )
    send_post.click()
    print('Post feito')