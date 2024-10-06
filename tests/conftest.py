import os
import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the test and get the report
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == 'call' and report.failed:
        # Get the Playwright page object from the test's arguments
        page = item.funcargs.get('page')
        if page:
            # Define the screenshot directory and create it if necessary
            screenshot_dir = 'screenshots/failed_screenshot/'
            os.makedirs(screenshot_dir, exist_ok=True)

            # Generate a unique screenshot path based on the test's node id
            screenshot_path = os.path.join(screenshot_dir, f"{item.nodeid.replace('::', '_')}.png")

            # Capture the full page screenshot
            page.screenshot(path=screenshot_path, full_page=True)

            # Attach the screenshot to the Allure report
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)




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


