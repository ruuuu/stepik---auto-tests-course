import os
from selenium import webdriver
import time






link = "http://suninjuly.github.io/file_input.html"




try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Rufina")
    browser.find_element_by_name("lastname").send_keys("Davletova")
    browser.find_element_by_name("email").send_keys("rithre@klm.ty")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего  .py файла, то есть /Users/rufina/PycharmProjects/MyProjects/stepik
    print("current_dir :", current_dir)


    file_path = os.path.join(current_dir, 'myfile.txt')  # добавляем к этому пути имя файла, то есть /Users/rufina/PycharmProjects/MyProjects/stepik/myfile.txt
    print("file_path: ", file_path)

    element = browser.find_element_by_xpath("//input[@type='file']")
    element.send_keys(file_path)



    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()









finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()



