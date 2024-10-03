from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page,url:str):
        self.page = page
        self.url = url
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.header = page.get_by_text("Swag Labs")
        self.login_btn = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def load_page(self):
        self.page.goto(self.url)

    def login(self,username:str,password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def get_error(self):
        return self.error_message.text_content()
