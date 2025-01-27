import logging
from pathlib import Path

from smolagents import Model

from src.agent.agentq import AgentQ
from src.agent.rest_agent.rest_tools import tools
from src.agent.rest_agent.prompt import agent_prompt
log = logging.getLogger(__name__)


class RestAgent(AgentQ):

    def __init__(self, model: Model, base_url: str, swagger_json: str):
        super().__init__(model=model, agent_prompt=agent_prompt, tools=tools, base_url=base_url, swagger_json=swagger_json)

    def get_code_imports(self):
        return "from src.agent.rest_agent.rest_tools import *"

    def do(self, task: str, force_regenerate: bool = False) -> any:
        log.debug(f"Running task: {task}")
        return super().do(task=task, force_regenerate=force_regenerate)
