import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    inventory_page.add_to_cart_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==False
    assert inventory_page.remove_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/add_to_cart.png')


def test_empty_cart(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    assert inventory_page.remove_button.is_visible()==True
    inventory_page.remove_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/empty_cart_from_inventory.png')