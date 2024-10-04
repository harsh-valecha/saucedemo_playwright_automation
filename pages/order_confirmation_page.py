from playwright.sync_api import Page

class OrderConfirmationPage:
    def __init__(self,page:Page,url:str):
        self.page = page
        self.page.goto(url)
        self.product_name = Page.locator("//div[@class='inventory_item_name']")
        self.product_price = Page.locator("//div[@class='inventory_item_price']")
        self.item_total = Page.locator("//div[@class='summary_subtotal_label']")
        self.item_tax = Page.locator("//div[@class='summary_tax_label']")
        self.total = Page.locator("//div[@data-test='total-label']")
        self.cancel_button = Page.locator("//button[@id='cancel']")
        self.finish_button = Page.locator("//button[@id='finish']")


