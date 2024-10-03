import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage

@pytest.mark.order(2)
def test_add_to_cart(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    inventory_page.add_to_cart_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==False
    assert inventory_page.remove_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/add_to_cart.png')

@pytest.mark.order(3)
def test_empty_cart(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    assert inventory_page.remove_button.is_visible()==True
    inventory_page.remove_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/empty_cart_from_inventory.png')

@pytest.mark.order(4)
def test_sort_titles_ascending(page):
    inventory_page = InventoryPage(page,'https://www.saucedemo.com/inventory.html')
    titles = inventory_page.inventory_titles.all_inner_texts()
    titles.sort()
    inventory_page.sorter_dropdown.select_option(value='az')
    titles_after = inventory_page.inventory_titles.all_inner_texts()
    assert titles_after == titles
    page.screenshot(path='screenshots/test_screenshots/sort_ascending_titles.png',full_page=True)

@pytest.mark.order(5)
def test_sort_titles_descending(page):
    inventory_page = InventoryPage(page, 'https://www.saucedemo.com/inventory.html')
    titles = inventory_page.inventory_titles.all_inner_texts()
    titles.sort(reverse=True)
    inventory_page.sorter_dropdown.select_option(value='za')
    titles_after = inventory_page.inventory_titles.all_inner_texts()
    assert titles_after == titles
    page.screenshot(path='screenshots/test_screenshots/sort_descending_titles.png',full_page=True)