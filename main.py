from models.subject import Subject
from models.semester import Semester
from models.student import Student

LINE = '-'*40


def menu():
    student = None

    while True:
        print('1. Create Student\n2. Add Semester\n3. Add Subject\n4. View Student\n5. View Semester\n6. Exit')
        try:
            choice = int(input('Enter your choice: '))
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
                try:
                    if student is None:
                        raise ValueError('Create a student first.')
                    print(LINE)
                    print(f'{'Name':<20}: {student.name}')
                    print(f'{'Roll Number':<20}: {student.roll_number}')
                    print()
                    print(f'{'Semesters Completed':<20}: {len(student.semesters)}')
                    print(f'{'CGPA':<20}: {student.calculate_cgpa():.2f}')
                    print(LINE)
                except ValueError as e:
                    print(e)
            elif choice == 5:
                if student is None:
                    raise ValueError('No student found.')
                elif not student.semesters:
                    raise ValueError('Semester not found.')
                semester_asked = int(input('Semester number: '))
                semester_to_display = student.find_semester(semester_asked)
                print(f'{'Semester':<20}: {semester_to_display.number}')
                print(f'{'SGPA':<20}: {semester_to_display.calculate_sgpa()}')
                print(f'{'Credits':<20}: {semester_to_display.get_total_credits()}')
                print()
                print('Subjects')
                print(LINE)
                print(f'{'Subject':<30}{'Cr':<6}{'Marks':<8}{'Grade':<8}{'GP':<4}')
                for subject in semester_to_display.subjects:
                    print(
                        f'{subject.name:<30}{subject.credits:<6}{subject.obtained_marks:<8}{subject.get_grade():<8}{subject.get_grade_point():<4}')
                print(LINE)
            elif choice == 6:
                print('Thank you!')
                break
            else:
                raise ValueError('Invalid choice.')
        except ValueError as e:
            print(e)


menu()
