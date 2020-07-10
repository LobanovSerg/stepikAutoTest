from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Bender Bending")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Rodriguez")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Tijuana")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Estados Unidos Mexicanos")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    browser.quit()
