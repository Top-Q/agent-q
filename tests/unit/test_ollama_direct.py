from ollama import chat, Client
from ollama import ChatResponse
from smolagents import CodeAgent, tool

from src.model.ollama_model import OllamaModel


def test_simple_chat():
    response: ChatResponse = chat(model='llama3.1:8b', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ])
    print(response['message']['content'])

def test_simple_client():
    client = Client(
        host='http://localhost:11434',
        headers={'x-some-header': 'some-value'}
    )
    response = client.chat(model='llama3.1:8b', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ])
    print(response['message']['content'])

@tool
def multiply(a: int, b: int) -> int:
    """
    Calculate the product of two numbers.

    Args:
        a: The first number.
        b: The second number.
    """
    return a * b

def test_ollama_model():
    model = OllamaModel("llama3.1", host='192.168.68.116')
    agent = CodeAgent(model=model, tools=[multiply])
    response = agent.run("Calculate 20 * 4")
    print(response)
