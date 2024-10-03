import pytest
from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self,page:Page,url:str):
        self.page = page
        self.page.goto(url)
        self.firstname_input = page.locator("//input[@id='first-name']")
        self.lastname_input = page.locator("//input[@id='last-name']")
        self.zipcode_input=page.locator("//input[@id='postal-code']")
        self.checkout_button = page.locator("//button[@id='checkout']")
        self.continue_shopping_button = page.locator("//button[@id='continue-shopping']")