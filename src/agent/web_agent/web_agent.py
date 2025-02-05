import logging
from typing import Optional, Dict

from playwright.sync_api import Page
from smolagents import Model

from src.agent.agentq import AgentQ
from src.agent.web_agent import web_tools
from src.agent.web_agent.prompt import agent_prompt
from src.agent.web_agent.web_tools import get_page_html, tools, get_aria_snapshot

log = logging.getLogger(__name__)

class WebAgent(AgentQ):
    """
    Agent for web automation tasks using Playwright based tools.
    """

    def __init__(self, page: Page, model: Model):
        """
        :param page: Playwright page object
        :param model: Model to use for the agent
        """
        super().__init__(model=model, agent_prompt=agent_prompt, tools=tools)
        self.page = page

    def get_code_imports(self):
        return "from src.agent.web_agent.web_tools import *"

    def do(self, task: str, force_regenerate: bool = False, additional_args: Optional[Dict] = None) -> any:
        """
        Perform the web automation task. If the task is already saved in the code store, use the saved code.
        :param task:
        :param force_regenerate:
        :param additional_args:
        :return:
        """
        log.debug(f"Running task: {task}")
        web_tools.ctx = {"page": self.page}
        additional_args = additional_args or {}
        additional_args["html snapshot"] =get_page_html()
        additional_args["aria snapshot"] = get_aria_snapshot()
        return super().do(task= task, force_regenerate=force_regenerate, additional_args=additional_args)

