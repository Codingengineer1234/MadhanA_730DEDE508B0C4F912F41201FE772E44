# Define a student class with attributes: name, roll_number, and cgpa
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Define the sort_students function
def sort_students(student_list):
    # Use the sorted() function with a custom key function to sort the list by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
  # Create a list of student objects
students = [
    Student("Alice", "A101", 3.9),
    Student("Bob", "B102", 3.6),
    Student("Charlie", "C103", 3.8),
    Student("David", "D104", 4.0),
]

# Call the sort_students function to sort the students by CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")