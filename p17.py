def display_lines(file_path, lines_to_display=5):
    with open(file_path, 'r') as file:
        all_lines = file.readlines()
    
    total_lines = len(all_lines)
    start_index = 0

    while start_index < total_lines:
        end_index = min(start_index + lines_to_display, total_lines)
        
        for i in range(start_index, end_index):
            print(all_lines[i].strip())

        input("Press Enter to continue...")
        start_index = end_index

if __name__ == "__main__":
    file_path = "p17.txt"
    display_lines(file_path)