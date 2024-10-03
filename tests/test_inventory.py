import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    inventory_page.click_add_to_cart()
    assert inventory_page.add_to_cart_button.is_visible()==False
    assert inventory_page.remove_button.is_visible()==True
    inventory_page.cart_button.screenshot(path='screenshots/test_screenshots/add_to_cart.png')