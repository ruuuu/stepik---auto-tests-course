from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # browser.find_elements_by_class_name("first").send_keys("Руфина")
    #
    # browser.find_elements_by_class_name("second").send_keys("Lfdktnjdf")
    #
    # browser.find_elements_by_class_name("third").send_keys("Lty6@mail.tu")
    #
    # browser.find_elements_by_class_name("second").send_keys("Lfdktnjdf")




    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("руфина")










    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла