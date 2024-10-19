import mimetypes
import os

def get_file_extension(file_name: str):
    mime_type, _ = mimetypes.guess_type(file_name)
    return mime_type

def remove_file_extension(file_name: str):
    base, _ = os.path.splitext(file_name)
    return base

def get_last_n_file_path(file_path: str, number_path: int):
    file_path_list = file_path.split("/")
    return_file_path = []
    for i in range(0, number_path):
        return_file_path.append(file_path_list[-1-i])
    return '/'.join(reversed(return_file_path))
