import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from utils.config import Config

@pytest.mark.order(2)
def test_add_to_cart(page):
    inventory_page = InventoryPage(page,Config.inventory_page_url)
    inventory_page.add_to_cart_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==False
    assert inventory_page.remove_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/add_to_cart.png')

#@pytest.mark.dependency(depends=["test_add_to_cart"])
@pytest.mark.order(3)
def test_empty_cart(page):
    inventory_page = InventoryPage(page,Config.inventory_page_url)
    assert inventory_page.remove_button.is_visible()==True
    inventory_page.remove_button.click()
    assert inventory_page.add_to_cart_button.is_visible()==True
    page.screenshot(path='screenshots/test_screenshots/empty_cart_from_inventory.png')

@pytest.mark.order(4)
def test_sort_titles_ascending(page):
    inventory_page = InventoryPage(page,Config.inventory_page_url)
    titles = inventory_page.inventory_titles.all_inner_texts()
    titles.sort()
    inventory_page.sorter_dropdown.select_option(value='az')
    titles_after = inventory_page.inventory_titles.all_inner_texts()
    assert titles_after == titles
    page.screenshot(path='screenshots/test_screenshots/sort_ascending_titles.png',full_page=True)

@pytest.mark.order(5)
def test_sort_titles_descending(page):
    inventory_page = InventoryPage(page, Config.inventory_page_url)
    titles = inventory_page.inventory_titles.all_inner_texts()
    titles.sort(reverse=True)
    inventory_page.sorter_dropdown.select_option(value='za')
    titles_after = inventory_page.inventory_titles.all_inner_texts()
    assert titles_after == titles
    page.screenshot(path='screenshots/test_screenshots/sort_descending_titles.png',full_page=True)

@pytest.mark.order(6)
def test_sort_prices_ascending(page):
    inventory_page = InventoryPage(page, Config.inventory_page_url)
    prices = inventory_page.inventory_prices.all_text_contents()
    prices_sorted = [float(i[1:]) for i in prices ]
    prices_sorted.sort()
    inventory_page.sorter_dropdown.select_option(value='lohi')
    prices_after = inventory_page.inventory_prices.all_text_contents()
    prices_converted = [float(i[1:]) for i in prices_after ]
    assert prices_sorted == prices_converted
    page.screenshot(path='screenshots/test_screenshots/sort_ascending_prices.png',full_page=True)

@pytest.mark.order(7)
def test_sort_prices_descending(page):
    inventory_page = InventoryPage(page, Config.inventory_page_url)
    prices = inventory_page.inventory_prices.all_text_contents()
    prices_sorted = [float(i[1:]) for i in prices ]
    prices_sorted.sort(reverse=True)
    inventory_page.sorter_dropdown.select_option(value='hilo')
    prices_after = inventory_page.inventory_prices.all_text_contents()
    prices_converted = [float(i[1:]) for i in prices_after ]

    assert prices_sorted == prices_converted
    page.screenshot(path='screenshots/test_screenshots/sort_descending_prices.png',full_page=True)