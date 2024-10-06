import pytest
from playwright.sync_api import Page
from utils.config import Config

class CheckoutPage:
    def __init__(self,page:Page,url:str= Config.checkout_page_url):
        self.page = page
        self.page.goto(url)
        self.firstname_input = page.locator("//input[@id='first-name']")
        self.lastname_input = page.locator("//input[@id='last-name']")
        self.zipcode_input=page.locator("//input[@id='postal-code']")
        self.checkout_button = page.locator("//button[@id='checkout']")
        self.continue_shopping_button = page.locator("//button[@id='continue-shopping']")

    def confirm_order(self,first_name:str,last_name:str,pincode:str):
        self.firstname_input.fill(first_name)
        self.lastname_input.fill(last_name)
        self.zipcode_input.fill(pincode)
        self.checkout_button.click()