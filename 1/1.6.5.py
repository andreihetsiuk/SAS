from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    input1 = browser.find_element(By.PARTIAL_LINK_TEXT, num)
    input1.click()

    f_name = browser.find_element(By.NAME, "first_name")
    f_name.send_keys("test1")

    l_name = browser.find_element(By.NAME, "last_name")
    l_name.send_keys("test2")

    city = browser.find_element(By.NAME, "firstname")
    city.send_keys("test1")

    country = browser.find_element(By.ID, "country")
    country.send_keys("test2")

    butt = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    butt.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
