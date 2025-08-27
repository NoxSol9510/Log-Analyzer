#log level count
import os 
from formatter import *

def file_type():
    choices = {
        "1": "txt",
        "2": "csv",
        "3": "json",
        "0": None
    }

    while True:
        print("1. Text\n2. CSV\n3. JSON\n0. Cancel")
        choice = input("Choose file type: ")
        if choice in choices:
            return choices[choice]
        print("Invalid input")

def log_analysis(path):
    count_info = 0
    count_error = 0
    count_warning = 0

    try:
        with open(path) as file:
            for line in file:

                content = line.upper()
                if "INFO" in content:
                    count_info += 1
                elif "ERROR" in content:
                    count_error += 1
                elif "WARNING" in content:
                    count_warning += 1

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None, None, None, None
    
    total_log = count_info + count_error + count_warning
    return total_log, count_info, count_error, count_warning

def log_search(path, keyword):
    count_match = 0
    list_match = []
    
    # Convert the search keyword to lowercase for case not sensitive
    keyword_lower = keyword.lower()

    try:
        with open(path) as file:
            for line in file:
                if keyword_lower in line.lower():
                    list_match.append(line)
                    count_match += 1
    
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None, []

    return count_match, list_match

def log_exist(path):
    if os.path.exists(path):
        print("Log finish export")
    else:
        print("Error while exporting")

def log_export(path, full_name):
    total, info, error, warning = log_analysis(path)
    
    if full_name.endswith(".txt"):
        file_name = format_txt(full_name, total, info, error, warning)
    elif full_name.endswith(".csv"):
        file_name = format_csv(full_name, total, info, error, warning)
    elif full_name.endswith(".json"):
        file_name = format_json(full_name, total, info, error, warning)
    else:
        print("Invalid export format")
        return
    
    log_exist(file_name)

def log_search_export(results, full_name):
    if full_name.endswith(".txt"):
        with open(full_name, "w") as f:
            for line in results:
                f.write(line)
        log_exist(full_name)

    elif full_name.endswith(".csv"):
        with open(full_name, "w") as f:
            f.write("Matched Lines\n")
            for line in results:
                f.write(f"\"{line.strip()}\"\n")
        log_exist(full_name)

    elif full_name.endswith(".json"):
        import json
        with open(full_name, "w") as f:
            json.dump(results, f, indent=4)
        log_exist(full_name)

    else:
        print("Invalid export format")
