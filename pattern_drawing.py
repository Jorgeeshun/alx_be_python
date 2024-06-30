# pattern_drawing.py

def draw_square_pattern(size):
    row = 0  # Initialize row counter

    # Loop to iterate through each row
    while row < size:
        # Nested loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        print()  # Print a newline character after each row
        row += 1  # Move to the next row

def main():
    try:
        # Prompt the user to input a positive integer
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Error: The size must be a positive integer.")
        else:
            draw_square_pattern(size)
    except ValueError:
        print("Error: Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
