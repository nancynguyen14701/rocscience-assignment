import pytest
from playwright.sync_api import sync_playwright, Browser

from config import URLS
from pages.base_page import BasePage


@pytest.fixture(scope="session", autouse=True)
def configure(request):
    env = request.config.getoption("--env")

    BasePage.base_url = URLS[env]

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment: staging, prod",
    )