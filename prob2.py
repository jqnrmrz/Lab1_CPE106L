def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def main():
    while True:
        filename = input("Enter the filename (or '0' to quit): ")
        
        if filename == '0':
            break
        
        lines = read_file(filename)
        if not lines:
            continue

        num_lines = len(lines)

        while True:
            try:
                line_number = int(input(f"Enter a line number (1 - {num_lines}): "))
                if line_number == 0:
                    break
                elif 1 <= line_number <= num_lines:
                    print(lines[line_number - 1])
                else:
                    print(f"Line number should be between 1 and {num_lines}.")
            except ValueError:
                print("Invalid input. Please enter a valid line number.")
    
if __name__ == "__main__":
    main()
