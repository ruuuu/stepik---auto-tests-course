import os
from selenium import webdriver
import time
import  math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




link = "http://suninjuly.github.io/alert_accept.html"


# Работа с окнами

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']") # ищем кнопку  стектсотм I want to go on a magical journey!
    button.click()

    confirm = browser.switch_to.alert  # получаем мод окно
    confirm.accept()  # жмем  в нем ок

    #first_window = browser.window_handles[0] # текущая владка

    window_name = browser.window_handles[0] # находим текущю вкладку
    browser.switch_to.window(window_name) # переходим на нее


    # работает уже в этой новой вкладке
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # <span class="nowrap" id="input_value">206</span> , получит значение у элмента  x_element
    y = calc(x)

    browser.find_element_by_class_name("form-control").send_keys(y)

    browser.find_element_by_xpath("//button[text()='Submit']").click() # ищем кнопку с тектсом Submit






finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(14)
    # закрываем браузер после всех манипуляций
    browser.quit()



