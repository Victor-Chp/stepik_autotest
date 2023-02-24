# !/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    num3 = int(num1) + int(num2)

    select_num = browser.find_element(By.XPATH, '//option[text()="%s"]' % num3)
    select_num.click()

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # Ожидание для копирования числа
    time.sleep(10)
    # закрыть браузер после всех манипуляций
    browser.quit()