def read_data_file(file_path: str):
    clean_data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            clean_data.append(line)
    
    return clean_data