# ---------------------
# task: alert accept
# ---------------------

from selenium import webdriver
from math import *
import time


def calc_func(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert.accept()

    time.sleep(1)
    x = calc_func(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(str(x))

    browser.find_element_by_class_name('btn').click()

    alert = browser.switch_to.alert.text
    print('\n>>\t' + alert.split()[-1] + '\t<<\n')

finally:
    browser.quit()
