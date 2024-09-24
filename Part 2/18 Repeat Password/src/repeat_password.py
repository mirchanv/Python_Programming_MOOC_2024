# Write your solution here
pwd = input("Password: ")

while True:
    pwd_repeat = input("Repeat password: ")

    if pwd_repeat != pwd:
        print("They do not match!")
    else:
        break

print("User account created!")
