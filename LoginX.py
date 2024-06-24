from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LoginCredentials import user, password
from MakePost import MakePost

service = ChromeService(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get("https://x.com")

try:
    login_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div'
    click_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, login_button_xpath))
    )
    click_login_button.click()

    login_credentials_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
    login_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, login_credentials_xpath))
    )
    login_element.send_keys(user)

    next_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, next_button_xpath))
    )
    next_button.click()

    pwd_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    pwd_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, pwd_xpath))
    )
    pwd_element.send_keys(password)

    final_login_button_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'
    final_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, final_login_button_xpath))
    )
    final_login_button.click()
finally:
    MakePost(driver)
    driver.quit()
