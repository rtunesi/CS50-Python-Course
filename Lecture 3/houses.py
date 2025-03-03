# Left value = Key
# Right value = Value
hogwarts = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(hogwarts["Hermoine"])

for student in hogwarts:
    print(f"{student}: {hogwarts[student]}")

students = [{"Name": "Hermoine", "House": "Gryffindor", "Patronus": "Otter"},
            {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
            {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
            {"Name": "Draco", "House": "Slytherin", "Patronus": None}
            ]

for student in students:
    print(student["Name"])
    print(student["House"])
    print(student["Patronus"])