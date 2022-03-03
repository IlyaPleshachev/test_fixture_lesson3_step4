import pytest
import time
import math
from selenium import webdriver

result = ""

@pytest.fixture(scope="function")
def browser():
    print("\n* * * OPENING BROWSER * * *")
    browser = webdriver.Chrome()
    yield browser
    print("\n* * * CLOSING BROWSER * * *")
    browser.quit()
    print(result) #че-то про сов в конце

@pytest.mark.parametrize('site', ["236895", "236896", "236897", "236898",
                                  "236899", "236903", "236904","236905"])
def test_input_formula_answer(browser, site):
    global result
    link = f"https://stepik.org/lesson/{site}/step/1/"
    browser.get(link)
    browser.implicitly_wait(10)
      
    input1 = browser.find_element_by_css_selector('.textarea')
    input1.send_keys(str(math.log(int(time.time()))))
    
    browser.find_element_by_css_selector('.submit-submission ').click()
    
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:    #можно без трай, а просто проверку ассерт, и плюсуем в результат если иф не проходит
        assert 'Correct!' == check_text
    except AssertionError:
        result += check_text  # собираем ответ про Сов с каждой ошибкой
    