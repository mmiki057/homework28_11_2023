def calculate_average(grades):
    if grades:
        total = sum(grades)
        return total / len(grades)
    else:
        return None
def read_grades_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Grades:"):
                    grades_str = line.split(":")[1].strip()
                    grades = [float(grade) for grade in grades_str.split(',')]
                    return grades
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
if __name__ == "__main__":
    file_path = "grades.txt"
    grades = read_grades_from_file(file_path)
    if grades is not None:
        average = calculate_average(grades)
        if average is not None:
            print(f"The arithmetic mean of the student's grades is: {average:.2f}")
        else:
            print("No grades found in the file.")
    else:
        print("Error reading grades from the file.")