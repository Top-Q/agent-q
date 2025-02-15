import os
import pytest
from dotenv import load_dotenv
from smolagents import LiteLLMModel, OpenAIServerModel

from definitions import root_dir
from src.agent.agentq import AgentQ
from src.agent.fs_agent.fs_agent import FsAgent

TEST_FOLDER = "atestfolder"
FOLDER = os.path.join(root_dir,TEST_FOLDER)

@pytest.fixture()
def q():
    load_dotenv()
    model = OpenAIServerModel(api_base="https://api.openai.com/v1/",model_id="gpt-4o-mini", api_key=os.getenv("OPEN_AI_API_KEY"))
    agent = FsAgent(model)
    agent.init_agent()
    return agent

def test_count_files_in_folder(q: AgentQ):
    """
    Count the number of files in the folder
    """
    result = q.do(f"Count the number of files in the folder {FOLDER}")
    assert result == 5
