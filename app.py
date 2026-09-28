from flask import Flask, render_template, request, redirect
from storage import load_student, save_student
from models.subject import Subject
from analytics import get_academic_overview

app = Flask(__name__)

@app.route("/")
def home():
    student = load_student()

    overview = None

    if student:
        overview = get_academic_overview(student)

    return render_template(
        "dashboard.html",
        student=student,
        overview=overview
    )

@app.route("/semester/<int:semester_number>")
def semester_details(semester_number):
    student = load_student()

    if student is None:
        return "No student found.", 404

    try:
        semester = student.find_semester(semester_number)
    except ValueError:
        return "Semester not found.", 404

    return render_template(
        "semester.html",
        student = student,
        semester = semester
    )

@app.route("/semester/<int:semester_number>/add-subject", methods=["GET", "POST"])
def add_subject(semester_number):
    student = load_student()

    if student is None:
        return "No student found.", 404

    try:
        semester = student.find_semester(semester_number)
    except ValueError:
        return "Semester not found.", 404

    if request.method == "POST":
        name = request.form["name"]
        credits = int(request.form["credits"])
        obtained_marks = int(request.form["obtained_marks"])

        subject = Subject(
            name,
            credits,
            obtained_marks
        )

        semester.add_subject(subject)
        save_student(student)

        return redirect(f"/semester/{semester_number}")

    return render_template(
        "add_subject.html",
        semester=semester
    )

@app.route("/semester/<int:semester_number>/edit-subject/<subject_name>", methods=["GET", "POST"])
def edit_subject(semester_number, subject_name):
    student = load_student()

    if student is None:
        return "No student found.", 404

    try:
        semester = student.find_semester(semester_number)
        subject = semester.find_subject(subject_name)
    except ValueError:
        return "Subject not found.", 404

    if request.method == "POST":
        try:
            name = request.form["name"]
            credits = int(request.form["credits"])
            obtained_marks = int(request.form["obtained_marks"])

            subject.update_name(name)
            subject.update_credits(credits)
            subject.update_obtained_marks(obtained_marks)

            save_student(student)

            return redirect(f"/semester/{semester_number}")

        except ValueError as e:
            return render_template(
                "edit_subject.html",
                semester=semester,
                subject=subject,
                error=str(e)
            )

    return render_template(
        "edit_subject.html",
        semester=semester,
        subject=subject
    )

def home():
    student = load_student()

    overview = None

    if student:
        overview = get_academic_overview(student)

    return render_template(
        "dashboard.html",
        student=student,
        overview=overview
    )


if __name__ == "__main__":
    app.run(debug=True)