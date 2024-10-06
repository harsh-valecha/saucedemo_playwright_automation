import pytest
from playwright.sync_api import Page
from utils.config import Config

class CartPage:
    def __init__(self,page:Page,url:str=Config.cart_page_url):
        self.page = page
        self.page.goto(url)
        self.title = page.locator("//span[@class='title']")
        self.cart_items = page.locator("//div[@class='cart_item']")
        self.cart_item_names = page.locator("//div[@class='cart_item']")
        self.checkout_button = page.locator("//button[@id='checkout']")
        self.continue_shopping_button = page.locator("//button[@id='continue-shopping']")

