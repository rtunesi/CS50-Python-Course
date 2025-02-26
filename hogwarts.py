students = ["Hermione", "Harry", "Ron"]


# Don't use _ as you are using the variable later in the code
for student in students:
    print(student)

for student in students:
    for letter in student:
        print(letter)


# For each item in the length of the list, print the item number
for index in range(len(students)):
    print(index, students[index])