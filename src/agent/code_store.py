import shutil
import uuid
import json
import os
from datetime import datetime

from definitions import root_dir

CODE_STORE_FOLDER = "code_store"
TEMP_FILE_NAME = "temp.py"

def load_code_store():
    """
    Load the code store data from the file system.
    :return:
    """
    code_store_file = os.path.join(root_dir, CODE_STORE_FOLDER, "code_store.json")
    if os.path.exists(code_store_file):
        with open(code_store_file, "r") as file:
            return json.load(file)
    return {}

def save_code_store(code_store):
    """
    Save the code store data to the file system.

    :param code_store:
    :return:
    """
    code_store_file = os.path.join(root_dir, CODE_STORE_FOLDER, "code_store.json")
    with open(code_store_file, "w", encoding="utf-8") as file:
        json.dump(code_store, file, indent=4)

def add_to_store(code_identifier: str, task: str) -> str:
    """
    Aad the code identifier to the code store for the given task.

    :param code_identifier: UUID for the task code. Usually the file name.
    :param task: The task for which the code is generated.
    :return: The code identifier.
    """

    code_store = load_code_store()
    code_store[task] = {
        "file_identifier": code_identifier,
        "created": str(datetime.now())
    }
    save_code_store(code_store)
    return code_identifier

def save_code() -> str:
    """
    Save the code to a file and return the file identifier.
    :return:
    """
    store_folder = os.path.join(root_dir, CODE_STORE_FOLDER)
    if not os.path.exists(store_folder):
        os.makedirs(store_folder)
    temp_code_file = os.path.join(store_folder, TEMP_FILE_NAME)
    if not os.path.exists(temp_code_file):
        # No code was produced, nothing to do
        return ""
    file_identifier = str(uuid.uuid4())
    code_file = os.path.join(root_dir, CODE_STORE_FOLDER, file_identifier + ".py")
    shutil.copyfile(temp_code_file, code_file)
    os.remove(temp_code_file)
    return file_identifier


def task_code_exists(task: str) -> bool:
    """
    Check if the code for the given task exists in the code store.
    :param task:
    :return:
    """
    code_store = load_code_store()
    return task in code_store

def get_task_code(task: str):
    code_store = load_code_store()
    code_identifier = code_store[task]["file_identifier"]
    code_file = os.path.join(root_dir, CODE_STORE_FOLDER, code_identifier + ".py")
    with open(code_file, "r") as file:
        code_snippet = file.read()
    return code_snippet

