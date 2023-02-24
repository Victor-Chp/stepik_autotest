# !/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//div[label[contains(., "First name*")]]/input')
    input1.send_keys("Vasiya")
    input2 = browser.find_element(By.XPATH, '//div[label[contains(., "Last name*")]]/input')
    input2.send_keys("Orlov")
    input3 = browser.find_element(By.XPATH, '//div[label[contains(., "Email*")]]/input')
    input3.send_keys("moscow@shit.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.XPATH, '//h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставлять пустую строку в конце файла
