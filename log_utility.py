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

def log_export(data, name):
    # log count export
    if isinstance(data, dict):
        if name.endswith(".txt"):
            name = format_txt(name, data["Total Log"], data["Info"], data["Error"], data["Warning"])
        elif name.endswith(".csv"):
            name = format_csv(name, data["Total Log"], data["Info"], data["Error"], data["Warning"])
        elif name.endswith(".json"):
            name = format_json(name, data["Total Log"], data["Info"], data["Error"], data["Warning"])
        else:
            print("Invalid export format")
            return

    # search result export
    elif isinstance(data, list):
        if name.endswith(".txt"):
            with open(name, "w") as f:
                for line in data:
                    f.write(line)

        elif name.endswith(".csv"):
            with open(name, "w") as f:
                f.write("Matched Lines\n")
                for line in data:
                    f.write(f"\"{line.strip()}\"\n")

        elif name.endswith(".json"):
            import json
            with open(name, "w") as f:
                json.dump(data, f, indent=4)

        else:
            print("Invalid export format")
    
    else:
        print("Export Error: No match Data")
        return
    
    log_exist(name)