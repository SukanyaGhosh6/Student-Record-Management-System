# Student Record Management System

# List to store student records
students = []

# Function to add a new student
def add_student():
    name = input("Enter student's name: ")
    roll = int(input("Enter student's roll number: "))
    marks = float(input("Enter student's marks: "))
    students.append({'name': name, 'roll': roll, 'marks': marks})
    print(f"Student {name} added successfully!")

# Function to view all students
def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(f"Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")

# Function to search for a student by roll number using Linear Search
def search_student():
    roll = int(input("Enter roll number to search: "))
    found = False
    for student in students:
        if student['roll'] == roll:
            print(f"Student Found: Name: {student['name']}, Marks: {student['marks']}")
            found = True
            break
    if not found:
        print("Student with given roll number not found.")

# Function to delete a student record
def delete_student():
    roll = int(input("Enter roll number to delete: "))
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print(f"Student with roll number {roll} deleted successfully.")
            return
    print("Student with given roll number not found.")

# Function to sort students by marks using Bubble Sort
def sort_students_by_marks():
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j]['marks'] > students[j+1]['marks']:
                students[j], students[j+1] = students[j+1], students[j]
    print("Students sorted by marks successfully!")

# Main function to show menu
def main():
    while True:
        print("\n===== Student Record Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Sort Students by Marks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            sort_students_by_marks()
        elif choice == '6':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please select between 1-6.")

# Run the program
if __name__ == "__main__":
    main()
