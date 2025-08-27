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

    # basic log count
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
    
    # search file
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
        
        if input("Do you want to export these results? (y/n):"):
            file_name = input("Enter a file name: ")
            log_search_export(list_match,file_name)
        
    # export file
    elif choice == '3':
        path = file_path()

        file_ext = file_type()
        if not file_ext:
            print("Export canceled.")
        else:
            file_name = input("Enter file name: ") or "report"
            full_name = f"{file_name}.{file_ext}"  
            log_export(path, full_name) 

    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid input")