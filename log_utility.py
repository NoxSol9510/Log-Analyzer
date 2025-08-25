#log level count
import os 
from formatter import *

def file_type():
    print("1. Text")
    print("2. CSV")
    print("3. JSON")
    print("0. Cancel")

    while True:
        choice = input("Choose file type: ")
        if choice == '1':
            return ".txt"
        elif choice == '2':
            return ".csv"
        elif choice == '3':
            return ".json"
        elif choice == '0':
            return "cancel"
        else:
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

def log_export(path, out_file):
    total, info, error, warning = log_analysis(path)

    file_name = input("Enter a file name: ") or "report"
            
    if out_file == 1:
        file_name = format_txt(file_name, total, info, error, warning)
            
    elif out_file == 2:
        file_name = format_csv(file_name, total, info, error, warning)
    
    elif out_file == 3:
        file_name = format_json(file_name, total, info, error, warning)
    
    else:
        print("Invalid export format")
    
    log_exist(file_name)

def log_search_export(list, file_name):
    choice = input("")

    if file_name == "":
        file_name = "report"
    
    with open(file_name, "a") as f:
        for item in list:
            f.write(item)

    log_exist(file_name)