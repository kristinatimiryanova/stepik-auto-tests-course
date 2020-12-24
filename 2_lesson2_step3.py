from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_xpath("//span[@id='num1'][@class='nowrap']")
    x=x_element.text
    y_element  = browser.find_element_by_xpath("//span[@id='num2'][@class='nowrap']")
    y=y_element.text
    z= str(int(x)+int(y))

       
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z) 
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()