filename = "filename.txt"

with open(filename, 'r') as f:
    for line in f:
        print(line, end="")