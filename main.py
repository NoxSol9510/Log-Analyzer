from log_utility import *

def file_path():
    #temp for open file explorer
    #TEMP path to log file
    return r"Sample Log\samaple_log1.txt"

while True:
    print("\nMain Menu:")
    print("1. Log Analysis Report")
    print("2. Search Keyword")
    print("3. Export File")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("--- Log Analysis Report ---")
        path = file_path()
        total_log, info, error, warning = log_analysis(path)

        if total_log is not None:
            print(f"Total Log: {total_log}")
            print(f"Info: {info}")
            print(f"Error: {error}")
            print(f"Warning: {warning}")
        
        else:
            print("Error reading log")
    
    elif choice == '2':
        path = file_path()
        keyword = input("Enter search keyword: ")

        if keyword is not None:
            total_match, list_match = log_search(path, keyword)

        else:
            print("Returning to Main menu")

        print("--- Keyword Search Report ---")
        print(f"Total match: {total_match}")

        for item in list_match:
            print(item)
    
    elif choice == '3':
        path = file_path()

        print("1. txt")
        print("2. csv")
        print("3. Cancel")

        while True:
            file_type = input("Choose file type: ")

            if file_type == '1':
                log_export(path, 1)
                break
            
            elif file_type == '2':
                log_export(path, 2)
                break
            
            elif file_type == '3':
                break

            else:
                print("Invalid input")

    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid input")