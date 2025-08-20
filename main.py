#TEMP path to log file
file_path = r"Sample Log\samaple_log1.txt"

file = open(file_path, "r")
line = file.readline()

#counting the amount of each log level
def log_levels_count(content, info, error, warning):
    if "INFO" in content:
        info += 1
    elif "ERROR" in content:
        error += 1
    elif "WARNING" in content:
        warning += 1
    
    return info, error, warning

count_info = 0
count_error = 0
count_warning = 0

while line:
    print(line.strip())
    count_info, count_error, count_warning = log_levels_count(line, count_info, count_error, count_warning)
    line = file.readline()

total_log = count_info + count_error + count_warning

print("--- Log Analysis Report ---")
print(f"Total Log: {total_log}")
print(f"Info: {count_info}")
print(f"Error: {count_error}")
print(f"Warning: {count_warning}")

while True:
    print("\nMain Menu:")
    print("1. Log Analysis Report")
    print("2. Search Keyword")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Test 1")
    
    elif choice == '2':
        print("Test 2")
    
    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid input")