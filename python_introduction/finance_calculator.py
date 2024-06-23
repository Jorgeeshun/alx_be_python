# finance_calculator.py

# Prompt the user to input financial details
monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your monthly expenses"))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses 
print(f"Your monthly savings are ${monthly_savings}.")

# Define a variable (Assume annual interest rate of 5%)
simple_annual_intrest = 0.05

# Calculate the Projected Savings after one year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the result
print(f"Projected savings after one year, with interest, is ${projected_savings}.")
