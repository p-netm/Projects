import os

def get_dir(files_folder_name):
    """Points to where a file is """
    if not isinstance(files_folder_name, str):
        raise TypeError("Passed in value is not a String")
    parent_dir = os.path.dirname(os.getcwd())
    return os.path.join(parent_dir, files_folder_name)
