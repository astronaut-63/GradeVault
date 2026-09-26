from flask import Flask, render_template
from storage import load_student
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