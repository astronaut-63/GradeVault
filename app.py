from flask import Flask, render_template, request, redirect
from storage import load_student, save_student
from models.semester import Semester
from models.subject import Subject
from models.student import Student
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

@app.route("/semester/<int:semester_number>/delete-subject/<subject_name>", methods=["POST"])
def delete_subject(semester_number, subject_name):
    student = load_student()

    if student is None:
        return "No student found.", 404

    try:
        semester = student.find_semester(semester_number)
        semester.remove_subject(subject_name)
        save_student(student)
        return redirect(f"/semester/{semester_number}")
    except ValueError:
        return "Subject not found.", 404

@app.route("/add-semester", methods=["GET", "POST"])
def add_semester():
    student = load_student()

    if student is None:
        return "No student found.", 404

    if request.method == "POST":
        try:
            number = int(request.form["number"])

            semester = Semester(number)

            student.add_semester(semester)
            save_student(student)

            return redirect("/")
        except ValueError as e:
            return render_template(
                "add_semester.html",
                error=str(e)
            )

    return render_template("add_semester.html")

@app.route("/delete-semester/<int:semester_number>", methods=["POST"])
def delete_semester(semester_number):
    student = load_student()

    if student is None:
        return "No student found.", 404

    try:
        student.remove_semester(semester_number)
        save_student(student)
        return redirect("/")
    except ValueError:
        return "Semester not found.", 404

@app.route("/create-student/", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        try:
            name = request.form["name"]
            roll_number = request.form["roll_number"]

            student = Student(name, roll_number)
            save_student(student)

            return redirect("/")

        except ValueError as e:
            return render_template(
                "create_student.html",
                error=str(e)
            )

    return render_template("create_student.html")

@app.route("/edit-student", methods=["GET", "POST"])
def edit_student():
    student = load_student()

    if student is None:
        return "No student found.", 404

    if request.method == "POST":
        try:
            name = request.form["name"]
            roll_number = request.form["roll_number"]

            student.update_name(name)
            student.update_roll_number(roll_number)

            save_student(student)

            return redirect("/")

        except ValueError as e:
            return render_template(
                "edit_student.html",
                student=student,
                error=str(e)
            )

    return render_template(
        "edit_student.html",
        student=student
    )

@app.route("/analytics")
def analytics():
    student = load_student()

    if student is None:
        return "No student found.", 404

    from analytics import (
        get_sgpa_data,
        get_grade_distribution,
        get_subject_data
    )

    sgpa_data = get_sgpa_data(student).to_dict(orient="records")
    grade_distribution = get_grade_distribution(student)
    subject_data = get_subject_data(student)

    return render_template(
        "analytics.html",
        student=student,
        sgpa_data=sgpa_data,
        grade_distribution=grade_distribution,
        subject_data=subject_data
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