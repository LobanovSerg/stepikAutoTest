# ----------------------------
# task: unittest style tests
# ----------------------------

from selenium import webdriver
import unittest


def input_func(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get(link)
    # код, который заполняет обязательные поля
    browser.find_element_by_class_name(
        'first_block .first').send_keys('Dart')
    browser.find_element_by_class_name(
        'first_block .second').send_keys('Vader')
    browser.find_element_by_class_name(
        'first_block .third').send_keys('death@star.com')
    # Отправляем заполненную форму
    browser.find_element_by_class_name("btn").click()

    # находим элемент, содержащий текст
    welcome_text = browser.find_element_by_tag_name("h1").text
    browser.quit()
    return welcome_text, "Congratulations! You have successfully registered!"


class TestForm(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            *input_func("http://suninjuly.github.io/registration1.html"))

    def test_2(self):
        self.assertEqual(
            *input_func("http://suninjuly.github.io/registration2.html"))


if __name__ == "__main__":
    unittest.main()
