# ------------------------------------
# task: search with get_attribute
# ------------------------------------

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем значение x и подставляем в формулу
    val_x = browser.find_element_by_id('treasure')
    x = calc(val_x.get_attribute('valuex'))

    # вводим ответ отмечаем чекбоксы
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    # отправляем...
    browser.find_element_by_class_name('btn').click()

finally:
    # время для копирования ответа
    time.sleep(10)
    browser.quit()
