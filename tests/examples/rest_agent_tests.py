import os
import pytest

from src.agent.agentq import AgentQ
from src.agent.rest_agent.rest_agent import RestAgent


@pytest.fixture
def q():
    api_key = os.environ["OPENAI_API_KEY"]
    base_url = "https://petstore.swagger.io/v2"
    agent = RestAgent(base_url=base_url, swagger_json_file="../../swagger/swagger_petstore.json", api_key=api_key)
    agent.init_agent()
    return agent


def test_get_pet_by_id(q: AgentQ):
    result = q.do("Get pet with ID=2")
    print(result)


def test_add_new_pet(q: AgentQ):
    result = q.do("Add a new pet with the name 'Yoshi'")
    print(result)