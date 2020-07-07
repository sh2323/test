import pytest
import time
from selenium import webdriver


@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_button(browser, url):
    link = url
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn.btn-lg"))
    assert button > 0, "There is no button"

