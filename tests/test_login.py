from lib2to3.fixes.fix_input import context
import pytest
from pages.login_page import LoginPage

@pytest.mark.order(1)
def test_valid_login(page):
    login_page = LoginPage(page,'https://www.saucedemo.com/')
    login_page.load_page()
    login_page.login('standard_user','secret_sauce')
    assert page.url == 'https://www.saucedemo.com/inventory.html'


@pytest.mark.skip
def test_invalid_login(page):
    login_page = LoginPage(page, 'https://www.saucedemo.com/')
    login_page.load_page()
    login_page.login('test_user', 'secret_sauce')
    #page.pause() # adding breakpoint to debug the testcase
    assert login_page.get_error() == 'Epic sadface: Username and password do not match any user in this service'
