import json

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


@tool
def find_json_key(json_str: str, key: str) -> any:
    """
    Searches for a given key in a JSON string and returns its value.
    Supports nested dictionaries and lists.

    Args:
        json_str: A string representation of a JSON object.
        key: The key to search for.

    :return: The value of the key if found, otherwise None.
    """
    def search(data, key):
        if isinstance(data, dict):
            if key in data:
                return data[key]
            for value in data.values():
                result = search(value, key)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = search(item, key)
                if result is not None:
                    return result
        return None

    try:
        json_data = json.loads(json_str)
        return search(json_data, key)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string")


tools = [get_request, post_request, find_json_key]