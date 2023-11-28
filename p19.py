def copy_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line)

if __name__ == "__main__":
    input_file = "p19.txt"
    output_file = "copylines.txt"

    copy_file(input_file, output_file)
    print(f"Contents copied from '{input_file}' to '{output_file}'.")