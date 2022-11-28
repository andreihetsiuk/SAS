from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(1)
    browser.switch_to.alert.accept()

    num = browser.find_element(By.ID, 'input_value').text
    send = browser.find_element(By.ID, 'answer')

    send.send_keys(calc(num))
    time.sleep(1)

    submit = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    submit.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
