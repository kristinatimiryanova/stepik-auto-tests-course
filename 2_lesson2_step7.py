from selenium import webdriver
import time
import math

import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[contains(@placeholder,'first name')]")
    input1.send_keys("Kris")
    input2 = browser.find_element_by_xpath("//input[contains(@placeholder,'last name')]")
    input2.send_keys("Timi")
    input3 = browser.find_element_by_xpath("//input[contains(@placeholder,'email')]")
    input3.send_keys("KrisTimi@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()