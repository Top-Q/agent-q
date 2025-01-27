import os

import pytest
from dotenv import load_dotenv
from smolagents import HfApiModel, TransformersModel

from definitions import root_dir
from src.agent.agentq import AgentQ
from src.agent.fs_agent.fs_agent import FsAgent
TEST_FOLDER = "atestfolder"
FOLDER = os.path.join(root_dir,TEST_FOLDER)

@pytest.fixture
def q():
    load_dotenv()
    model = TransformersModel(model_id="Qwen/Qwen2.5-3B-Instruct", device="cpu")
    agent = FsAgent(model)
    agent.init_agent()
    return agent

def test_count_files_in_folder(q: AgentQ):
    """
    Count the number of files in the folder
    """
    result = q.do(f"Count the number of files in the folder {FOLDER}")
    assert result == 5