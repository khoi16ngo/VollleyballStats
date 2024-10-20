import csv

def print_stats_csv(file_path: str, data: list):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)