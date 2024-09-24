# Write your solution here
year = int(input("Year: "))
next_leap_year = year

while True:
    next_leap_year += 1
    is_leap_year = next_leap_year % 4 == 0 and next_leap_year %100 != 0 or next_leap_year % 100 == 0 and next_leap_year % 400 == 0

    if is_leap_year:
        print(f"The next leap year after {year} is {next_leap_year}")
        break

