# ----------------------------------
# task: parameterization of tests
# ----------------------------------

import pytest
from selenium import webdriver
import time
import math

answer = ''


# фикстура управляющяя открытием и закрытием браузера
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(answer)  # вывод результата


# список частей адресов ссылок
links_list = ['895', '896', '897', '898', '899', '903', '904', '905']


# класс с параметризацией
@pytest.mark.parametrize('lnk', links_list)
class TestLinks:
    def test_link(self, browser, lnk):
        global answer
        browser.get(f'https://stepik.org/lesson/236{lnk}/step/1')
        browser.find_element_by_tag_name('textarea').send_keys(
            str(math.log(int(time.time()))))
        browser.find_element_by_class_name('submit-submission').click()
        text = browser.find_element_by_class_name('smart-hints__hint').text
        # сохранение частей ответа в строку
        try:
            assert text == 'Correct!', '>>\t{text}'
        except AssertionError:
            answer += text
