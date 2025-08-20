#log level count
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
    