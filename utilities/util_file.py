import mimetypes
import os

def get_file_extension(file_name: str):
    mime_type, _ = mimetypes.guess_type(file_name)
    return mime_type

def remove_file_extension(file_name: str):
    base, _ = os.path.splitext(file_name)
    return base
