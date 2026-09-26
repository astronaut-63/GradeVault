from flask import Flask, render_template
from storage import load_student

app = Flask(__name__)


@app.route("/")
def home():
    student = load_student()

    return render_template(
        "dashboard.html",
        student=student
    )


if __name__ == "__main__":
    app.run(debug=True)