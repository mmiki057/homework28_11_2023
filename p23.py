def save_powers_to_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Number\tSecond Power\tThird Power\n")

        for num in range(1, 11):
            second_power = num ** 2
            third_power = num ** 3
            file.write(f"{num}\t{second_power}\t{third_power}\n")

if __name__ == "__main__":
    output_file_path = "p23.txt"

    save_powers_to_file(output_file_path)
    print(f"Powers saved to '{output_file_path}'.")