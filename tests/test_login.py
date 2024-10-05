from lib2to3.fixes.fix_input import context
import pytest
from pages.login_page import LoginPage
from utils.config import Config
from data.db_connector import get_valid_users ,get_invalid_users

@pytest.mark.parametrize("user_data",get_valid_users())
@pytest.mark.order(1)
def test_valid_login(page,user_data:dict):
    login_page = LoginPage(page,Config.login_page_url)
    login_page.login(user_data['username'],user_data['password'])
    # print(user_data['username'])
    assert page.url == Config.inventory_page_url

@pytest.mark.parametrize("user_data",get_invalid_users())
def test_invalid_login(page,user_data:dict):
    login_page = LoginPage(page, Config.login_page_url)
    login_page.login(user_data['username'],user_data['password'])
    #page.pause() # adding breakpoint to debug the testcase
    assert 'Epic sadface: ' in login_page.get_error()
