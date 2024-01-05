from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть страницу 
    link = 'http://suninjuly.github.io/redirect_accept.html'   
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # 3. Переключиться на новую вкладку
    confirm = browser.switch_to.window(browser.window_handles[1])

    # 4. Пройти капчу для робота и получить число-ответ
    x = browser.find_element(By.ID, 'input_value').text
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(5)

finally:

    browser.quit()