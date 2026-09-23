import pandas as pd

def get_subject_data(student):
    rows = []

    for semester in student.semesters:
        for subject in semester.subjects:
            rows.append({
                "Semester": semester.number,
                "Subject": subject.name,
                "Credits": subject.credits,
                "Marks": subject.obtained_marks,
                "Grade": subject.get_grade(),
                "Grade Point": subject.get_grade_point()
            })

    return pd.DataFrame(rows)

def get_sgpa_data(student):
    rows = []

    for semester in student.semesters:
        rows.append({
            "Semester": semester.number,
            "SGPA": semester.calculate_sgpa()
        })

    return pd.DataFrame(rows)

def get_grade_distribution(student):
    df = get_subject_data(student)

    return df["Grade"].value_counts()

if __name__ == "__main__":
    from storage import load_student

    student = load_student()

    if student:
        df = get_subject_data(student)
        print(df)
    else:
        print("No student found.")