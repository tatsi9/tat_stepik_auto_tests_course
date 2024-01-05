from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

try:
    # Открыть страницу  
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд):
    button = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    # Нажать на кнопку
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


    # Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.ID, 'input_value').text
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    button = browser.find_element(By.ID, 'solve')
    button.click()

    time.sleep(10)

finally:

    browser.quit()