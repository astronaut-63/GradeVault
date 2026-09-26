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


if __name__ == "__main__":
    app.run(debug=True)