import os
from selenium import webdriver
import time
import  math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




link = "http://suninjuly.github.io/explicit_wait2.html"


# Работа с окнами

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")) # жде до тех пор, пока не появтияс текст  $100 у элемента

    browser.find_element_by_xpath("//button[text()='Book']").click()







    x_element = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           x_element)  # скроллим к элементу x_element, он окажется вверху станицы

    x = x_element.text  # <span class="nowrap" id="input_value">206</span> , получит значение у элмента  x_element
    print(" x= ", x)
    y = calc(x)

    browser.find_element_by_class_name("form-control").send_keys(y)

    browser.find_element_by_xpath("//button[text()='Submit']").click() # ищем кнопку с тектсом Submit






finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()



