# !/usr/bin/env python3

import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)

    answer = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)

    button = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()

    number = browser.switch_to.alert.text
    print(number)

finally:
    # Закрыть драйвер
    browser.quit()
