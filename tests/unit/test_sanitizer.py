import pytest
from playwright.sync_api import sync_playwright

from src.agent.web_agent.sanitizer import sanitize_html


@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()

def test_sanitizer(page):
    page.goto("https://demo.applitools.com/")
    html = page.content()
    result = sanitize_html(html)
    print(result)