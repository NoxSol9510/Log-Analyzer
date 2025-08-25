def format_txt(file_name, total, info, error, warning):
    with open(file_name + ".txt", "a") as f:
        f.write(f"Total Log: {total}\n")
        f.write(f"Info: {info}\n")
        f.write(f"Error: {error}\n")
        f.write(f"Warning: {warning}\n")
    return file_name + ".txt"

def format_csv(file_name, total, info, error, warning):
    with open(file_name + ".csv", "a") as f:
        f.write("Level,Count\n")
        f.write(f"Total Log,{total}\n")
        f.write(f"Info,{info}\n")
        f.write(f"Error,{error}\n")
        f.write(f"Warning,{warning}\n")
    return file_name + ".csv"

def format_json(file_name, total, info, error, warning):
    import json
    report = {
        "Total Log" : total,
        "Info" : info,
        "Error" : error,
        "Warning" : warning
    }

    with open(file_name + ".json", "a") as f:
        json.dump(report, f, indent=4)
    return file_name + ".json"