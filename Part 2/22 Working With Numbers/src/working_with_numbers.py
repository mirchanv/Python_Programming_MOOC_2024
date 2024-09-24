# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
total = 0
positives = 0
negatives = 0

while True:
    num = int(input("Number: "))
    
    if num == 0:
        break
    
    if num > 0:
        positives += 1
    else:
        negatives += 1

    count += 1
    total += num

mean = total / count 
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")

