# -------------------------------------
# task: work with a drop-down list
# -------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем значение x и y, вычисляем сумму
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    val = str(int(x) + int(y))

    # находим верное значение
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(val)
    # отправляем...
    browser.find_element_by_class_name('btn').click()

    # получаем ответ из всплывающего окна
    alert = browser.switch_to_alert().text
    print('\n' + alert.split()[-1] + '\n')

finally:
    browser.quit()
