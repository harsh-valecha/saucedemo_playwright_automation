import pytest
from playwright.sync_api import sync_playwright,Page
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config
from data.db_connector import get_valid_users

# username
user_username = None

@pytest.fixture(scope='function', params=get_valid_users())
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch browser
        context = browser.new_context()  # Create a new browser context
        page = context.new_page()  # Open a new page

        # Use user_data inside the fixture for login
        user_data = request.param
        global user_username
        user_username = user_data['username']
        # print(user_data)
        # page.pause()
        login_page = LoginPage(page, Config.login_page_url)
        login_page.login(user_data['username'], user_data['password'])

        yield page  # Yield the page to the test

        # Teardown phase: logout
        inventory_page = InventoryPage(page, Config.inventory_page_url)
        inventory_page.logout()

        context.close()
        browser.close()


def test_empty_checkout(page:Page):
    cart_page = CartPage(page)
    cart_page.checkout_button.click()
    assert page.url == Config.checkout_page_url,f"The URL is working correctly for this user for {user_username}"
    page.screenshot(path=f'screenshots/test_screenshots/{user_username}/empty_cart_checkout.png',full_page=True)


def test_continue_shopping(page:Page):
    cart_page = CartPage(page)
    cart_page.continue_shopping_button.click()
    assert page.url == Config.inventory_page_url,f"Page not redirected to inventory for {user_username} "
    page.screenshot(path=f'screenshots/test_screenshots/{user_username}/continue_shopping_button_check.png', full_page=True)

def test_checkout(page:Page):
    inventory_page = InventoryPage(page)
    price_from_inventory = inventory_page.add_to_cart_item()
    cart_page = CartPage(page)
    price_in_cart = float(cart_page.cart_item_price.text_content()[1:])
    assert price_from_inventory == price_in_cart,f"Price is not the same as inventory for {user_username}"
    cart_page.checkout_button.click()
    assert page.url == Config.checkout_page_url,f"page not redirected to checkout page for {user_username}"
    page.screenshot(path=f'screenshots/test_screenshots/{user_username}/positive_checkout.png',
                    full_page=True)


def test_remove_item(page:Page):
    inventory_page = InventoryPage(page)
    price_from_inventory = inventory_page.add_to_cart_item()
    cart_page = CartPage(page)
    price_in_cart = float(cart_page.cart_item_price.text_content()[1:])
    assert price_from_inventory == price_in_cart,f"Price is not the same as inventory for {user_username}"
    cart_page.remove_button.click()
    assert cart_page.cart_item_names.is_visible()==False,f"Item is still visible for {user_username}"
    page.screenshot(path=f'screenshots/test_screenshots/{user_username}/remove_item.png',
                    full_page=True)
