import logging
from pathlib import Path
from typing import Optional, Dict

from smolagents import Model

from src.agent.agentq import AgentQ
from src.agent.rest_agent.rest_tools import tools
from src.agent.rest_agent.prompt import agent_prompt
log = logging.getLogger(__name__)


class RestAgent(AgentQ):

    def __init__(self, base_url: str, swagger_json: str, model: Model):
        super().__init__(model=model, agent_prompt=agent_prompt, tools=tools)
        self.base_url = base_url
        self.swagger_json = swagger_json

    def get_code_imports(self):
        return "from src.agent.rest_agent.rest_tools import *"

    def do(self, task: str, force_regenerate: bool = False, additional_args: Optional[Dict] = None) -> any:
        additional_args = additional_args or {}
        additional_args["Base URL"] = self.base_url
        additional_args["Swagger JSON"] = self.swagger_json
        log.debug(f"Running task: {task}")
        return super().do(task=task, force_regenerate=force_regenerate, additional_args=additional_args)
