
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Ana": 35
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
