import pytest
from playwright.sync_api import Page

class InventoryPage:
    def __init__(self,page:Page,url:str):
        self.page= page
        self.page.goto(url)
        self.add_to_cart_button = page.locator("//button[@data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_button = page.locator("//button[@data-test='remove-sauce-labs-backpack']")
        self.cart_button = page.locator("//a[@data-test='shopping-cart-link']")
        self.inventory_titles = page.locator("//div[@data-test='inventory-item-name']")
        self.sorter_dropdown = page.locator("//select")



