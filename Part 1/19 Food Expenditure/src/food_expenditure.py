# Write your solution here
frequency = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_expense = float(input("How much money do you spend on groceries in a week? "))

weekly_expense = (lunch_price * frequency) + grocery_expense
daily_expense = weekly_expense / 7;

print(f"Average food expenditure:\nDaily: {daily_expense} euros\nWeekly: {weekly_expense} euros")