from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  # <span class="nowrap" id="input_value">206</span> , получит значение у элмента  x_element
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 23787700);")  #  скроллим станицу вниз на 100 пиксеелй

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    el = browser.find_element_by_id("robotsRule")

    browser.execute_script("return arguments[0].scrollIntoView(true);", el) # скроллим  кэлементу el, элемент окадется верху станицы
    el.click()


    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()









finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла