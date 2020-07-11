# ----------------------
# task: download file
# ----------------------

from selenium import webdriver
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    # вводим ответ отмечаем чекбоксы
    input_ = browser.find_element_by_css_selector('[name="firstname"]')
    input_.send_keys('Doctor')
    input_2 = browser.find_element_by_css_selector('[name="lastname"]')
    input_2.send_keys('Who')
    input_3 = browser.find_element_by_css_selector('[name="email"]')
    input_3.send_keys('police@box.net')

    input_4 = browser.find_element_by_id('file')
    # получаем путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'src/text.txt')
    # отправляем файл
    input_4.send_keys(file_path)

    # отправляем форму
    browser.find_element_by_class_name('btn').click()

    # получаем ответ из всплывающего окна
    alert = browser.switch_to_alert().text
    print('\n>>\t' + alert.split()[-1] + '\t<<\n')

finally:
    browser.quit()
