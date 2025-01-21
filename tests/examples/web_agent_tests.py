import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

from src.agent.agentq import AgentQ
from src.agent.web_agent.web_agent import WebAgent


@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()

@pytest.fixture
def q(page):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    agent = WebAgent(page, api_key)
    agent.init_agent()
    return agent

def login_to_acme_bank(page: Page):
    page.goto("https://demo.applitools.com/")
    page.get_by_role(role="textbox", name="Enter your username").fill("admin")
    page.locator("id=password").fill("admin")
    page.locator("id=log-in").click()

def test_fill_realistic_values(page: Page, q: AgentQ):
    """
    Test generate realistic data for the login page of the ACME bank
    """
    page.goto("https://demo.applitools.com/")
    q.do("Fill all the login page input fields with realistic data and click on the sign in button")

def test_perform_signin(page: Page, q: AgentQ):
    page.goto("https://demo.applitools.com/")
    q.do("Fill the sign in form with username 'admin' and password 'admin' and click on the sign in button")

def test_get_credit_available(page: Page, q: AgentQ):
    login_to_acme_bank(page)
    credit = q.do("Get the available credit in the page")
    print(f"The available credit is {credit}")

def test_get_all_text_from_table(page: Page, q: AgentQ):
    login_to_acme_bank(page)
    page_content = q.do("Get all the text from the table")
    print(page_content)

def test_count_elements_in_page(page: Page, q: AgentQ):
    login_to_acme_bank(page)
    count = q.do("Count the number of transaction with state 'Complete' in the page")
    print(f"The number of transactions with state 'Complete' is {count}")

def test_monsters_page(page: Page, q: AgentQ):
    page.goto("https://snw-companion.web.app")
    q.do("Select 'מפלצות' from the menu")
    result = q.do("Count the numbers of monsters in the table")
    print(f"The number of monsters in the table is {result}")

def test_open_project(page: Page, q: AgentQ):
    page.goto('http://localhost:8080')
    page.get_by_role("link", name="Sign in").click()
    q.do("Fill 'admin' in username textbox and password 'adminadmin' in password textbox, and click on the 'Sign in' button")
    q.do("Click on the 'Select a project' link")
    q.do("Click on 'Demo project' link")
    q.do("Click on the 'Work packages' link", force_regenerate=False)

