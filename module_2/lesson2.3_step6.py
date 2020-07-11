# -----------------------------
# task: switch to a new tab
# -----------------------------

from selenium import webdriver
from math import log, sin


def calc_func(x):
    return log(abs(12 * sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_class_name('trollface').click()

    # переход на новую вкладку
    win_name = browser.window_handles[1]
    browser.switch_to.window(win_name)

    x = calc_func(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(str(x))

    browser.find_element_by_class_name('btn').click()

    alert = browser.switch_to.alert.text
    print('\n>>\t' + alert.split()[-1] + '\t<<\n')

finally:
    browser.quit()
