from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_id("num1").text
    x_element2 = browser.find_element_by_id("num2").text
    print("x_element1= ", x_element1)
    print("x_element2= ", x_element2)

    x = int(x_element1) + int(x_element2)
    print("x=", x)

    select = Select(browser.find_element_by_tag_name("select"))





    select.select_by_value(str(x))

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()









finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла