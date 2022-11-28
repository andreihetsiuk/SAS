from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1 = int(num1.text)
    num2 = browser.find_element(By.ID, 'num2')
    num2 = int(num2.text)
    summ = str(num1 + num2)
    print(summ)
    v = ()

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select = select.select_by_visible_text(summ)

    #browser.find_element(By.CSS_SELECTOR, "[value='"+summ +"']").click()
    # option = browser.find_elements(By.TAG_NAME, 'option')
    #
    # for i in range(len(option)):
    #     num3 = option[i].text
    #     if num3 == summ:
    #         print(num3)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(3)











finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
