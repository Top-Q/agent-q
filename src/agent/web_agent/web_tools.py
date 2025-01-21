from playwright.sync_api import Page, Locator
from smolagents import tool

from src.agent.web_agent.sanitizer import sanitize_html

ctx = {}


@tool
def goto_url(url: str) -> str:
    """
    Go to a page in URL

    Args:
        url: URL to go to

    """
    page: Page = ctx.get("page")
    page.goto(url)
    return f"Opened {url}"


@tool
def get_page_html() -> str:
    """
    Get the HTML source of the page

    """
    page: Page = ctx.get("page")
    html = sanitize_html(page.content())
    print(f"HTML Snapshot: {html}")
    return html


def __get_locator(playwright_selector: str) -> Locator:
    """
        Get a playwright locator according to the selector
    :param playwright_selector: playwright selector
    :return:
    """
    page: Page = ctx.get("page")
    return page.locator(playwright_selector)


@tool
def fill_element(playwright_selector: str, text: str) -> str:
    """
    Fill an element with text

    Args:
        playwright_selector: playwright selector
        text: text to fill the element with

    """
    __get_locator(playwright_selector).first.fill(text)
    return f"Filled {playwright_selector} with {text}"

@tool
def get_table_inner_text(table_selector: str) -> str:
    """
    Get the inner text of a table

    Args:
        table_selector: playwright selector of the table

    """
    table_locator = __get_locator(table_selector).first
    return table_locator.inner_text()

@tool
def get_element_inner_text(playwright_selector: str) -> str:
    """
    Get the inner text of an element

    Args:
        playwright_selector: playwright selector of the element

    """
    return __get_locator(playwright_selector).first.inner_text()


@tool
def count_elements(playwright_selector: str) -> int:
    """
    Count elements with the given selector

     Args:
        playwright_selector: playwright selector

    :return: number of elements
    """
    return __get_locator(playwright_selector).count()


@tool
def is_element_visible(playwright_selector: str) -> bool:
    """
    Check if an element is visible

    Args:
        playwright_selector: playwright selector

    :return: True if the element is visible, False otherwise
    """
    return __get_locator(playwright_selector).first.is_visible()


@tool
def click_element(playwright_selector: str) -> str:
    """
    Click an element locator

     Args:
        playwright_selector: playwright selector

    """
    __get_locator(playwright_selector).first.click()
    return f"Clicked {playwright_selector}"

@tool
def get_aria_snapshot() -> str:
    """
    Get the ARIA snapshot of the page

    """
    page: Page = ctx.get("page")
    snapshot = str(page.accessibility.snapshot())
    print(f"Aria snapshot: {snapshot}")
    return snapshot

tools = [goto_url, get_page_html, fill_element, click_element, count_elements, is_element_visible,
         get_element_inner_text, get_table_inner_text, get_aria_snapshot]
