import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from smolagents import LiteLLMModel

from src.agent.agentq import AgentQ
from src.agent.rest_agent.rest_agent import RestAgent


@pytest.fixture
def q():
    load_dotenv()
    model = LiteLLMModel(model_id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    base_url = "https://petstore.swagger.io/v2"
    swagger_json = Path("../../swagger/swagger_petstore.json").read_text()
    agent = RestAgent(model=model, base_url=base_url, swagger_json=swagger_json)
    agent.init_agent()
    return agent


def test_get_pet_by_id(q: AgentQ):
    result = q.do("Get pet with ID=3")
    print(result)


def test_add_new_pet(q: AgentQ):
    result = q.do("Add a new pet with the name 'Yoshi'")
    print(result)

def test_add_new_pet_and_get_it_by_id(q: AgentQ):
    result = q.do("Add a new pet with a random pet name, then find in the response JSON the ID of the newly created pet and get the pet details from the API")
    print(result)