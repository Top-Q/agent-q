import os
import pytest
from dotenv import load_dotenv
from smolagents import LiteLLMModel

from definitions import root_dir
from src.agent.agentq import AgentQ
from src.agent.fs_agent.fs_agent import FsAgent

TEST_FOLDER = "atestfolder"
FOLDER = os.path.join(root_dir,TEST_FOLDER)


@pytest.fixture
def q():
    load_dotenv()
    model = LiteLLMModel(model_id="gpt-4o-mini", api_key=os.getenv("OPEN_AI_API_KEY"))
    agent = FsAgent(model)
    agent.init_agent()
    return agent

def test_count_files_in_folder(q: AgentQ):
    """
    Count the number of files in the folder
    """
    result = q.do(f"Count the number of files in the folder {FOLDER}")
    assert result == 5

def test_find_the_biggest_file_in_folder(q: AgentQ):
    """
    Find the biggest file in the folder
    """
    result = q.do(f"Find the biggest file in the folder {FOLDER}")
    print(result)

def test_get_the_content_of_the_biggest_file(q: AgentQ):
    """
    Get the content of the biggest file in the folder
    """
    result = q.do(f"Get the content of the biggest file in the folder {FOLDER}")
    print(result)

def test_count_files_in_sub_folders(q: AgentQ):
    """
    Count the number of files in the sub folders
    """
    result = q.do(f"Count the number of files in the folder {FOLDER} and its sub folders")
    print(result)