# Write your solution here
year = int(input("Please type in a year: "))

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400  == 0

if divisible_by_4 and divisible_by_100 and divisible_by_400:
    print("That year is a leap year.")
elif divisible_by_4 and divisible_by_100:
    print("That year is not a leap year.")
elif divisible_by_4:
    print("That year is a leap year.")
else: 
    print("That year is not a leap year.")