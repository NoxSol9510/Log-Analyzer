from log_utility import *

def file_path():
    #temp for open file explorer
    #TEMP path to log file
    return r"Sample Log\samaple_log1.txt"

while True:
    print("\nMain Menu:")
    print("1. Log Analysis Report")
    print("2. Search Keyword")
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
        print("Test 2")
    
    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid input")