import matplotlib.pyplot as plt

def plot_marks_by_subject(df, semester_number=None):
    if semester_number is not None:
        df = df[df["Semester"] == semester_number]
    plt.figure(figsize=(12, 6))

    plt.bar(df["Subject"], df["Marks"])

    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Marks by Subject")

    plt.ylim(0, 100)
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()  

def plot_sgpa_trend(df):
    plt.figure(figsize=(8, 5))

    plt.plot(
        df["Semester"],
        df["SGPA"],
        marker="o"
    )

    plt.xlabel("Semester")
    plt.ylabel("SGPA")
    plt.title("SGPA Trend")
    plt.xticks(df["Semester"])
    plt.ylim(0, 10)

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def plot_grade_distribution(data):
    plt.figure(figsize=(8, 5))

    data.plot(kind="bar")

    plt.xlabel("Grade")
    plt.ylabel("Number of Subjects")
    plt.title("Grade Distribution")

    plt.tight_layout()
    plt.show()

def plot_credits_by_semester(data):
    plt.figure(figsize=(8, 5))

    data.plot(kind="bar")

    plt.xlabel("Semester")
    plt.ylabel("Total Credits")
    plt.title("Credits per Semester")

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    from storage import load_student
    from analytics import get_credits_by_semesters

    student = load_student()

    if student:
        data = get_credits_by_semesters(student)
        print(data)
        plot_credits_by_semester(data)
    else:
        print("No student found.")