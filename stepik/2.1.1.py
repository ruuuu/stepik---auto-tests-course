from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex") # элемент есть <img src="images/chest.png" height="40" width="40" id="treasure" valuex="216"> , у него находим атрибут valuex
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_id("robotsRule").click()









    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла