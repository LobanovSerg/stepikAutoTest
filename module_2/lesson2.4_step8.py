# ----------------------------------------------------
# task: waiting for the desired text on the page
# ----------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc_func(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # говорим Selenium проверять в течение 12 секунд,
    # пока ценa не станет 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id('book').click()

    # получаем х, вычисляем ответ
    x = calc_func(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(str(x))

    browser.find_element_by_id('solve').click()

    alert = browser.switch_to.alert.text
    print('\n>>\t' + alert.split()[-1] + '\t<<\n')

finally:
    browser.quit()
