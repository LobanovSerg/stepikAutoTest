# ----------------------------
# task: execute_script job
# ----------------------------

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем значение x и подставляем в формулу
    val_x = browser.find_element_by_id('input_value')
    x = calc(val_x.text)
    # прокрутка в видимую область
    browser.execute_script("return arguments[0].scrollIntoView(true);", val_x)

    # вводим ответ отмечаем чекбоксы
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    # отправляем...
    browser.find_element_by_class_name('btn').click()

    # получаем ответ из всплывающего окна
    alert = browser.switch_to_alert().text
    print('\n' + alert.split()[-1] + '\n')

finally:
    browser.quit()
