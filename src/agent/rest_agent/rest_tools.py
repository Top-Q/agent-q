from typing import Tuple

import requests

from smolagents import tool


@tool
def get_request(url: str) -> str:
    """
    Send HTTP GET request

    Args:
        url: URL of the requested endpoint

    :return: The response body as text string
    """

    response = requests.get(url=url)
    return response.text


@tool
def post_request(url: str, request_body: dict, headers: dict) -> str:
    """
    Send HTTP POST request

    Args:
        url: URL of the requested endpoint
        request_body: The payload JSON to be sent in the request body
        headers: The request headers

    :return: The response body as text string
    """

    response = requests.post(url=url, json=request_body, headers=headers)
    return response.text


tools = [get_request, post_request]