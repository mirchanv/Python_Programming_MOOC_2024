# Fix the program
points = int(input("How many points are on your card? "))

if points >= 100:
    bonus = points * 0.15
    points += bonus
    print("Your bonus is 15 %")

if points < 100:
    bonus = points * 0.1
    points += bonus
    print("Your bonus is 10 %")

print("You now have", points, "points")