# !/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    input = browser.find_element(By.ID, "answer").send_keys(answer)
    check_robot = browser.find_element(By.ID, "robotCheckbox").click()
    radio_robot = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robot)
    radio_robot.click()

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # Время для копирования кода
    time.sleep(10)
    # Закрыть драйвер
    browser.quit()

