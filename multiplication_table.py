# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table: "))


# Generate and Print the Multiplication Table:
print(f"Multiplication Table for {number}: ")
for i in range(1, 11):
   X = number 
   Y = i 
   Z = X * Y
   print(f"{X} * {Y} = {Z}")
   