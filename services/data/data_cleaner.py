import re
from utilities.util_file import get_last_n_file_path, remove_file_extension

LINE_PATTERN_MATCH = r'\d{1,2}\s[a-z]\s\d{1,2}'

def clean_text_file(file_path: str):
    clean_data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue

            clean_line = _clean_text_line(line)

            if clean_line == '':
                continue

            clean_data.append(clean_line)
    
    if len(clean_data) == 0:
        return

    file_path = get_last_n_file_path(file_path, 2)
    new_cleaned_file_name = "./results/" + remove_file_extension(file_path) + "_cleaned.txt"
    with open(new_cleaned_file_name, 'w') as outfile:
        for line in clean_data:
            outfile.write(line + '\n')

def _clean_text_line(line: str):
    line = line.strip()
    line_matches = re.findall(LINE_PATTERN_MATCH, line)
    return line_matches[0] if len(line_matches) > 0 else ''
