from html_sanitizer import Sanitizer
from bs4 import BeautifulSoup as bs


def sanitize_html(page_content: str) -> str:
    """
    Sanitize HTML content

    :param page_content: The HTML content to sanitize
    :return: Sanitized HTML content
    """
    allowed_attributes = (
        "href", "name", "target", "title", "id", "rel", "class", "test_id", "data-test-id", "aria-label", "role",
        "aria-hidden")
    sanitizer = Sanitizer({
        "tags": {
            "a", "h1", "h2", "h3", "strong", "em", "p", "ul", "ol", "input", "select", "option", "label", "form",
            "li", "br", "sub", "sup", "hr", "table", "thead", "tbody", "span", "tr", "td", "th",
            "div", "img"

        },
        "attributes": {"a": allowed_attributes,
                       "table": allowed_attributes,
                       "td": allowed_attributes,
                       "th": allowed_attributes,
                       "tr": allowed_attributes,
                       "div": allowed_attributes,
                       "span": allowed_attributes,
                       "p": allowed_attributes,
                       "ul": allowed_attributes,
                       "ol": allowed_attributes,
                       "li": allowed_attributes,
                       "sub": allowed_attributes,
                       "input": allowed_attributes,
                       "select": allowed_attributes,
                       "option": allowed_attributes,
                       "label": allowed_attributes,
                       "form": allowed_attributes,
                       },
        "empty": {"hr", "a", "br", "input"},
        "separate": {"a", "p", "li"},
        "whitespace": {"br"},
        "keep_typographic_whitespace": False,
        "add_nofollow": False,
        "autolink": False,

    })
    sanitized = sanitizer.sanitize(page_content)
    soup = bs(sanitized)  # make BeautifulSoup
    return soup.prettify()  # prettify the html
