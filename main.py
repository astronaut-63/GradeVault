from models.subject import Subject
from models.semester import Semester
from models.student import Student
from storage import load_student, save_student

LINE = '-'*60


def menu():
    student = load_student()

    while True:
        print('1. Create Student\n2. Add Semester\n3. Add Subject\n4. View Student\n5. View Semester\n6. Edit Subject\n7. Delete Subject\n8. Delete Semester\n9. Exit')
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                name = input('Enter the name: ')
                roll_number = input('Enter the roll number: ')
                student = Student(name, roll_number)
                save_student(student)
                print('Student created!')
            elif choice == 2:
                try:
                    if student is None:
                        raise ValueError('Create a student first.')

                    number = int(input('Enter the semester number: '))
                    new_semester = Semester(number)
                    student.add_semester(new_semester)
                    save_student(student)
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
                    save_student(student)
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
                if student is None:
                    raise ValueError('No student found.')
                elif not student.semesters:
                    raise ValueError('Semester not found.')
                try:
                    semester_number = int(input('Enter Semester Number: '))
                    selected_semester = student.find_semester(semester_number)
                    subject_name = input('Enter Subject Name: ')
                    subject_to_edit = selected_semester.find_subject(
                        subject_name)
                    print('1. Edit Name\n2. Edit Credits\n3. Edit Obtained Marks')
                    edit_choice = int(input('Enter your choice: '))
                    if edit_choice == 1:
                        new_name = input('Enter new name: ')
                        subject_to_edit.update_name(new_name)
                        save_student(student)
                        print('Name edited successfully.')
                        print(f'New Name: {subject_to_edit.name}')
                    elif edit_choice == 2:
                        new_credits = int(input('Enter new credits: '))
                        subject_to_edit.update_credits(new_credits)
                        save_student(student)
                        print('Credits edited successfully.')
                        print(f'New Credits: {subject_to_edit.credits}')
                    elif edit_choice == 3:
                        new_obtained_marks = int(
                            input('Enter new obtained marks: '))
                        subject_to_edit.update_obtained_marks(
                            new_obtained_marks)
                        save_student(student)
                        print('Obtained marks edited successfully.')
                        print(f'New Marks: {subject_to_edit.obtained_marks}')
                    else:
                        raise ValueError('Invalid choice.')
                except ValueError as e:
                    print(e)

            elif choice == 7:
                if student is None:
                    raise ValueError('No student found.')
                elif not student.semesters:
                    raise ValueError('Semester not found.')
                try:
                    semester_number = int(input('Enter the semester number: '))
                    selected_semester = student.find_semester(semester_number)
                    subject_name = input('Enter the subject name: ')
                    selected_semester.remove_subject(subject_name)
                    save_student(student)
                    print('Subject removed successfully!')
                except ValueError as e:
                    print(e)

            elif choice == 8:
                if student is None:
                    raise ValueError('No student found.')
                elif not student.semesters:
                    raise ValueError('Semester not found.')
                try:
                    semester_number = int(input('Enter the semester number: '))
                    student.remove_semester(semester_number)
                    save_student(student)
                    print(f'Semester {semester_number} removed successfully!')
                except ValueError as e:
                    print(e)

            elif choice == 9:
                print('Thank you!')
                break
            else:
                raise ValueError('Invalid choice.')
        except ValueError as e:
            print(e)


menu()
