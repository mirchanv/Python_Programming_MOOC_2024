# Write your solution here
no_of_students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups_formed = (no_of_students + (group_size-1)) // group_size

print(f"Number of groups formed: {groups_formed}")
