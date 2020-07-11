# --------------------------------------------
# task: finding elements using Selenium
# --------------------------------------------

from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"
link_ = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_link_text(link_)
    link.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Obi-Wan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Kenobi")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Stewjon")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Coruscant")
    button = browser.find_element_by_xpath("//button[text()='Submit']]")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
