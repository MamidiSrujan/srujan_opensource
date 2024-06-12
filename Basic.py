class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if name in self.students:
            print("Student already exists.")
        else:
            self.students[name] = Student(name, grade)
            print("Student added successfully.")

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            print("Student removed successfully.")
        else:
            print("Student not found.")

    def display_students(self):
        print("List of students:")
        for student in self.students.values():
            print(student)

    def save_students(self, filename):
        with open(filename, 'w') as file:
            for student in self.students.values():
                file.write(f"{student.name},{student.grade}\n")
        print("Data saved successfully.")

    def load_students(self, filename):
        self.students.clear()
        with open(filename, 'r') as file:
            for line in file:
                name, grade = line.strip().split(',')
                self.students[name] = Student(name, int(grade))
        print("Data loaded successfully.")

def main():
    system = StudentManagementSystem()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            system.add_student(name, grade)
        elif choice == '2':
            name = input("Enter student name to remove: ")
            system.remove_student(name)
        elif choice == '3':
            system.display_students()
        elif choice == '4':
            filename = input("Enter filename to save data: ")
            system.save_students(filename)
        elif choice == '5':
            filename = input("Enter filename to load data: ")
            system.load_students(filename)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
