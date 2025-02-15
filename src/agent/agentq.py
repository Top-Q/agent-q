import os
from abc import ABC, abstractmethod
from typing import Optional, Dict

from smolagents import CodeAgent, LiteLLMModel, tool, HfApiModel, Model
from definitions import root_dir
from src.agent.code_store import task_code_exists, get_task_code, save_code, add_to_store
import logging

from src.agent.prompt import system_prompt

logging.basicConfig(filename=os.path.join(root_dir,'ai_agent.log'), level=logging.DEBUG)
log = logging.getLogger(__name__)

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'
TEMP_FILE_NAME = "temp.py"
CODE_STORE_FOLDER = "code_store"


@tool
def save_code_to_file(code_snippet: str) -> str:
    """
    Save LLM-generated code into a specified file.

    Args:
        code_snippet: The code to be saved into the file. This should be a valid string containing Python code.

    Returns:
        str: A confirmation message if the code is successfully saved, or an error message if something goes wrong.
    """
    code_as_bytes = code_snippet.encode("utf-8")
    store_folder = os.path.join(root_dir, CODE_STORE_FOLDER)
    if not os.path.exists(store_folder):
        os.makedirs(store_folder)
    code_file_name = os.path.join(store_folder, TEMP_FILE_NAME)
    try:
        if os.path.exists(code_file_name):
            os.remove(code_file_name)
        with open(f"{code_file_name}", "wb") as file:
            file.write(code_as_bytes.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING))
        log.debug(f"Code successfully saved to {code_file_name}")
        return f"Code successfully saved to {code_file_name}"
    except Exception as e:
        return f"Failed to save code: {e}"


class AgentQ(ABC):
    """
    Abstract class for the AI agent. Extend the class to create a new agent with specific tools and prompts.

    """
    def __init__(self, model: Model, agent_prompt: str, tools=None):
        if tools is None:
            tools = []
        self.agent: CodeAgent = None
        self.model = model
        self.system_prompt = system_prompt + "\n" + agent_prompt
        self.tools = tools

    @abstractmethod
    def get_code_imports(self):
        """
        Get the imports needed for the code snippet.
        :return:
        """
        return ""

    def init_agent(self):
        self.tools.append(save_code_to_file)
        self.agent = CodeAgent(
            tools=self.tools,
            model=self.model,
            add_base_tools=False,
            max_steps=20,
            additional_authorized_imports=["pytest", "time", "json"]
        )

    def do(self, task: str, force_regenerate: bool = False, additional_args: Optional[Dict] = None) -> any:
        """
        Perform the task. If the task is already saved in the code store, use the saved code.

        :param task: task to perform
        :param force_regenerate: force the agent to regenerate the code
        :param additional_args: additional arguments for the task
        :return: result of the task
        """
        if not force_regenerate and task_code_exists(task):
            python_code_snippet = get_task_code(task)
            return self.__perform_code(python_code_snippet)
        result = self.agent.run(
            task=self.system_prompt + "\n" + task,
            single_step=False,
            additional_args=additional_args)
        code_identifier = save_code()
        if code_identifier:
            add_to_store(code_identifier, task)
        return result

    def __perform_code(self, code: str) -> any:
        """
        Perform the code snippet.
        :param code:
        :return: result of the code snippet
        """
        code = self.get_code_imports() + "\r\n\r\n" + code
        log.debug(f"Performing code snippet:\n {code}")
        local_vars = {}
        exec(code, local_vars)
        if "result" in local_vars:
            return local_vars["result"]
        else:
            return list(local_vars.values())[-1]
