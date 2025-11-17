name = input("Hey what's your name? ")

print("Hello!",name,)
print("Welcome to the finance management program.\nMay I ask what you would like to start with?")

income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expense: "))
monthly_savings = income - expense

print("Your monthly savings are kes",monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * int(0.05))

print("Projected savings after one year of earning '5%' interest will be",projected_savings)