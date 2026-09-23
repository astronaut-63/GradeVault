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

def get_credits_by_semesters(student):
    df = get_subject_data(student)

    return df.groupby("Semester")["Credits"].sum()

def get_academic_overview(student):
    total_credits = 0;

    for semester in student.semesters:
        total_credits += semester.get_total_credits()

    latest_sgpa = None

    if student.semesters:
        latest_semester = max(
            student.semesters,
            key=lambda semester: semester.number
        )
        latest_sgpa = latest_semester.calculate_sgpa()

    return {
        "CGPA": student.calculate_cgpa(),
        "Latest SGPA": latest_sgpa,
        "Total Credits": total_credits,
        "Semesters Completed": len(student.semesters)
    }

if __name__ == "__main__":
    from storage import load_student

    student = load_student()

    if student:
        overview = get_academic_overview(student)
        print(overview)
    else:
        print("No student found.")