import pytest
from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser


@pytest.fixture(params=['chromium','firefox'])
def browser_type_launch(request):
    browser_type = request.param
    with sync_playwright() as playwright:
        browser = getattr(playwright,browser_type).launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser_type_launch):
    context = browser_type_launch.new_context()
    page = context.new_page()
    yield page
    context.close()
