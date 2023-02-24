# !/usr/bin/env python3
import time

import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    redirect = browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    confirm = browser.switch_to.alert.accept()

    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
    button.click()

    number = browser.switch_to.alert.text
    print (number)

finally:
    time.sleep(1)
    # Закрыть драйвер
    browser.quit()
