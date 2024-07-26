import random
import time
import os
import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
os.system('cls')
email_user_input = input("email: ")
password_user_input = input("pass: ")
time.sleep(0.4)
def login_discord(driver):
    try:
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email_input.clear()
        email_input.send_keys(email_user_input)
        time.sleep(random.uniform(0.1, 0.2))
        
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_input.clear()
        password_input.send_keys(password_user_input)
        time.sleep(random.uniform(0.1, 0.2))
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"].marginBottom8_f7730b.button_b83a05.button_dd4f85.lookFilled_dd4f85.colorBrand_dd4f85.sizeLarge_dd4f85.fullWidth_dd4f85.grow_dd4f85')))
        login_button.click()
    except TimeoutException:
        print("Не удалось найти элемент на странице.")

def main():
    options = undetected_chromedriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.3')
    number = 1
    with webdriver.Chrome(options=options) as driver:
        try:
            # Start,
            driver.set_window_size(200, 500)
            driver.get('https://discord.com/login')
            login_discord(driver)
            while True:
                status_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.avatarWrapper_b2ca13[aria-label="Задать статус"]')))
                status_button.click()
                time.sleep(random.uniform(2.1, 2.2))
                try:
                    status_button = driver.find_element(By.ID, 'status-add-custom-status')
                except:
                    status_button = driver.find_element(By.ID, 'status-edit-custom-status')
                status_button.click()
                time.sleep(random.uniform(2.1, 2.2))
                status_input = driver.find_element(By.CSS_SELECTOR, 'input.inputDefault_f8bc55.input_f8bc55.input_d5bea8')
                status_input.clear()
                status_input.send_keys(number)
                time.sleep(random.uniform(0.1, 0.2))
                status_save = driver.find_element(By.CSS_SELECTOR, "button.button_dd4f85.lookFilled_dd4f85.colorBrand_dd4f85.sizeMedium_dd4f85.grow_dd4f85")
                status_save.click()
                number += 1
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
