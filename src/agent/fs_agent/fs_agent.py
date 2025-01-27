import logging

from smolagents import Model

from src.agent.agentq import AgentQ
from src.agent.fs_agent.fs_tools import tools
from src.agent.fs_agent.prompt import agent_prompt
log = logging.getLogger(__name__)

class FsAgent(AgentQ):

    def __init__(self, model: Model):
        super().__init__(model, agent_prompt=agent_prompt, tools=tools)

    def get_code_imports(self):
        return "from src.agent.fs_agent.fs_tools import *"

    def do(self, task: str, force_regenerate: bool = False) -> any:
        log.debug(f"Running task: {task}")
        return super().do(task= task, force_regenerate=force_regenerate)
