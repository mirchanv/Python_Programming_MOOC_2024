# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second and second > third or second > first and third > second:
    print(f"The letter in the middle is {second}")   
elif second > first and first > third or first > second and third > first: 
    print(f"The letter in the middle is {first}")
elif third > first and second > third or first > third and third > second:
    print(f"The letter in the middle is {third}")
