monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are kes",monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Projected savings after one year of earning '5%' interest will be", projected_savings)