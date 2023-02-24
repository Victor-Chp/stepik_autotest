# !/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_lib.formula import calc

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    # говорим Selenium проверять в течение 12 секунд, пока цена не снизится до $100
    wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "$100"))
    button = browser.find_element(By.XPATH, '//button[contains(text(), "Book")]').click()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)
    input_x = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input_x.send_keys(y)

    submit = browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()

    number = browser.switch_to.alert
    print(number.text)
    number.accept()

finally:
    # Закрыть драйвер
    browser.quit()