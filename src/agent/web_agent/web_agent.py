import logging

from playwright.sync_api import Page

from src.agent.agentq import AgentQ
from src.agent.web_agent import web_tools
from src.agent.web_agent.prompt import agent_prompt
from src.agent.web_agent.web_tools import get_page_html, tools
log = logging.getLogger(__name__)

class WebAgent(AgentQ):
    """
    Agent for web automation tasks using Playwright based tools.
    """

    def __init__(self, page: Page, api_key: str):
        """
        :param page: Playwright page object
        :param api_key: OpenAI API key
        """
        super().__init__(api_key=api_key, agent_prompt=agent_prompt, tools=tools)
        self.page = page

    def get_code_imports(self):
        return "from src.agent.web_agent.web_tools import *"

    def do(self, task: str, force_regenerate: bool = False) -> any:
        """
        Perform the web automation task. If the task is already saved in the code store, use the saved code.
        :param task:
        :param force_regenerate:
        :return:
        """
        log.debug(f"Running task: {task}")
        web_tools.ctx = {"page": self.page}
        html = get_page_html()
        task = f"{task}\nUse the following initial HTML content of the page:\n {html}"
        return super().do(task= task, force_regenerate=force_regenerate)
