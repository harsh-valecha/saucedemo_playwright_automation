import pytest
from playwright.sync_api import Page
from utils.config import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.order_completion_page import OrderCompletionPage
from data.db_connector import get_users


@pytest.mark.parametrize("user_data",get_users())
def test_complete_flow(page:Page,user_data:dict):
    login_page = LoginPage(page,Config.login_page_url)
    login_page.login(user_data['username'],user_data['password'])
    inventory_page = InventoryPage(page,Config.inventory_page_url)
    inventory_page.add_to_cart_button.click()
    inventory_page.cart_button.click()
    cart_page = CartPage(page,Config.cart_page_url)
    cart_page.checkout_button.click()
    checkout_page = CheckoutPage(page,Config.checkout_page_url)
    checkout_page.confirm_order(first_name='test',last_name='test',pincode='1234')
    order_confirmation_page = OrderConfirmationPage(page,Config.order_confirmation_page)
    order_confirmation_page.finish_button.click()
    #order_completion_page = OrderCompletionPage(page,Config.order_completion_page)
    assert page.url == Config.order_completion_page

@pytest.mark.parametrize("user_data",get_users())
def test_db(user_data):
    print(user_data['username'],user_data['password'])
