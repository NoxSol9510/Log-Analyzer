#TEMP path to log file
file_path = r"Sample Log\samaple_log1.txt"


file = open(file_path, "r")
line = file.readline()

while line:
    print(line.strip())
    line = file.readline()
