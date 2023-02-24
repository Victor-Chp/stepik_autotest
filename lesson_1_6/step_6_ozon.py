# !/usr/bin/env python3
import time

import undetected_chromedriver as ucd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = ucd.Chrome()
uri_google = "https://google.com"
try:
    # open google.com
    browser.get(uri_google)
    search = browser.find_element(By.TAG_NAME, "input")

    # search request for ozon.ru
    search.send_keys("ozon.ru")
    search.send_keys(Keys.ENTER)

    # locate by partial link and open ozon.ru
    browser.find_element(By.PARTIAL_LINK_TEXT, "ozon.ru").click()
    time.sleep(5)

    prod_1 = browser.find_element(By.CSS_SELECTOR,
                                  '[data-widget="skuLine"] > div > div:nth-child(1) div[type="addToCartButtonWithQuantity"]').click()
    time.sleep(3)
    cart = browser.find_element(By.CSS_SELECTOR, 'a[href="/cart"]').click()
    time.sleep(10)

finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
