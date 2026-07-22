from models.subject import Subject
from models.semester import Semester
from models.student import Student


def menu():
    student = None

    while True:
        print('1. Create Student\n2. Add Semester\n3. Add Subject\n4. Exit')
        choice = int(input('Enter your choice: '))
        try:
            if choice == 1:
                name = input('Enter the name: ')
                roll_number = input('Enter the roll number: ')
                student = Student(name, roll_number)
                print('Student created!')
            elif choice == 2:
                try:
                    if student is None:
                        raise ValueError('Create a student first.')

                    number = int(input('Enter the semester number: '))
                    new_semester = Semester(number)
                    student.add_semester(new_semester)
                    print("Semester added!")
                except ValueError as e:
                    print(e)
            elif choice == 3:
                try:
                    if student is None:
                        raise ValueError('Create a student first.')
                    elif not student.semesters:
                        raise ValueError('Create a semester first.')

                    name = input('Enter subject name: ')
                    credits = int(input('Enter credits: '))
                    obtained_marks = int(input('Enter obtained marks: '))
                    subject = Subject(name, credits, obtained_marks)
                    semester_number = int(input('Enter the semester: '))
                    selected_semester = student.find_semester(semester_number)
                    selected_semester.add_subject(subject)
                    print('Subject added!')
                except ValueError as e:
                    print(e)
            elif choice == 4:
                print('Thank you!')
                break
            else:
                print('Invalid choice')
        except ValueError:
            print('Enter a valid choice.')


menu()
