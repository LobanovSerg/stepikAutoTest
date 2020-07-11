# ----------------------------------------
# task: checkboxes and radiobuttons
# ----------------------------------------

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    # получаем значение x и подставляем в формулу
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    # вводим ответ отмечаем чекбоксы
    input_ = browser.find_element_by_id('answer')
    input_.send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    # отправляем...
    browser.find_element_by_class_name('btn').click()

finally:
    # ожидание
    # визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.quit()
