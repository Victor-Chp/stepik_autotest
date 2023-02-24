# !/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Создать файл
file_name = "step_8.txt"
with open(file_name, "w") as txt_file:
    text = txt_file.write("Hello World")

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, '//label[contains(text(), "First name*")]//following-sibling::input')
    first_name.send_keys("Vasiya")
    last_name = browser.find_element(By.XPATH, '//label[contains(text(), "Last name*")]//following-sibling::input')
    last_name.send_keys("Pupkin")
    email = browser.find_element(By.XPATH, '//label[contains(text(), "Email *")]//following-sibling::input')
    email.send_keys("fantik@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.XPATH, '//label[contains(text(), "Choose file to upload")]//following-sibling::input[@type="file"]')
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    # Удалить файл
    os.remove(file_name)
    # Время для копирования кода
    time.sleep(10)
    # Закрыть драйвер
    browser.close()

