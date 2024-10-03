from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page,'https://www.saucedemo.com/')
    login_page.load_page()
    login_page.login('standard_user','secret_sauce')

    assert page.url == 'https://www.saucedemo.com/inventory.html'


def test_invalid_login(page):
    login_page = LoginPage(page, 'https://www.saucedemo.com/')
    login_page.load_page()
    login_page.login('test_user', 'secret_sauce')
    assert page.url == 'https://www.saucedemo.com/inventory.html'
