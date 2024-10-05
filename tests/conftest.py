import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    # Load session storage if available
    context = browser.new_context()

    try:
        # Load session data from a file if exists
        with open("session_storage.json", "r") as f:
            storage = f.read()
            context.add_cookies(eval(storage))  # Load cookies or session storage data here
    except FileNotFoundError:
        pass

    yield context

    # Save session storage after tests
    session_storage = context.cookies()  # Replace this with the session storage API if needed
    with open("session_storage.json", "w") as f:
        f.write(str(session_storage))

    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


