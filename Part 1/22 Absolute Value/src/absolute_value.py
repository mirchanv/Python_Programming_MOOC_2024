# Write your solution here
num = int(input("Please type in a number: "))
ans = "The absolute value of this number is "
if num < 0:
    print(f"{ans}{-num}")
else:
    print(f"{ans}{num}")