student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Ethan": 88
}

student_name = input("Enter student's name: ")

if student_name in student_marks:
    print(f"Marks for {student_name}: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")