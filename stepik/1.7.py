
from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html" #http://suninjuly.github.io/registration1.html


try:
    browser = webdriver.Chrome()
    browser.get(link)


    input0 = browser.find_element_by_tag_name("input")
    input0.send_keys("Ivan")

    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input1.send_keys("Ivanov")

    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    input2.send_keys("Petrov@mail.ru")

    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    input3.send_keys("8976545654")

    input4 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    input4.send_keys("Russia")

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла