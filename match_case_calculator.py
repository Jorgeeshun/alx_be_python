try: 
    # Prompt for User Input:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Perform the Calculation Using Match Case:
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print ("Error: Display by zero is not allowed.")
        case _:
            print("error: Invalid operation. Please choose from +, -, *, /.")

except ValueError:
    print("Error: Please enter valid numeric values.")