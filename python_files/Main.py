from Student import Student
from ArraySort import ArraySort
from BinarySearch import BinarySearch

def main():
  id = int(input("Enter the student ID: "))
  name = input("Enter the student's name: ")
  age = int(input("Enter the student's age: "))
  gpa = float(input("Enter the student's GPA: "))

  student = Student(id, name, age, gpa)
  print(student.return_student_record())


if __name__ == '__main__':
  main()