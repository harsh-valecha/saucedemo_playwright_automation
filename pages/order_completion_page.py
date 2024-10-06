from playwright.sync_api import Page


class OrderCompletionPage:
    def __init__(self,page:Page,url:str):
        self.page = page
        self.page.goto(url)
        self.title = Page.locator("//span[@data-test='title']")
        self.thankyou = Page.locator("//h2")
        self.back_to_home_button = Page.locator("//button[@id='back-to-products']")
