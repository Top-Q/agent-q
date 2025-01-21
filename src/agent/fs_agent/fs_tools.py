import os

from smolagents import tool


@tool
def count_files_in_folder(folder: str) -> int:
    """
    Count files in a folder

    Args:
        folder: folder path

    :return: number of files in the folder

    """
    return len(os.listdir(folder))

@tool
def get_file_size(file: str) -> int:
    """
    Get the size of a file

    Args:
        file: file path

    :return: size of the file
    """
    return os.path.getsize(file)

@tool
def get_content(file: str) -> str:
    """
    Get the content of a file

    Args:
        file: file path

    :returns: content of the file
    """

    with open(file, "r") as f:
        return f.read()

@tool
def list_files(folder: str) -> str:
    """
    List all file names in folder

    Args:
        folder: folder path

    :return: list of files as string
    """

    return os.listdir(folder)


tools = [get_file_size, count_files_in_folder, get_content, list_files]
