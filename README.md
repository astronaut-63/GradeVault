# GradeVault

> A personal academic performance tracker built with Python and Flask.

GradeVault helps students manage their academic records, calculate SGPA and CGPA, and visualize their performance through a web-based dashboard.

Built as a learning project while exploring Python, Flask, OOP, data analysis, web development, and Git.

## Features

### Student Profile
- Create a student profile
- Edit name and roll number
- Persistent profile data

### Semester Management
- Add semesters
- Delete semesters
- View semester-wise academic information
- Display semester SGPA and total credits

### Subject Management
- Add subjects to a semester
- Edit subject details
- Delete subjects
- Store credits and marks
- Automatically calculate grades and grade points

### Academic Calculations
- Automatic SGPA calculation
- Automatic CGPA calculation
- Credit-weighted CGPA
- Grade and grade-point calculation

### Dashboard
The dashboard provides an overview of:
- CGPA
- Total credits
- Number of semesters
- Semester-wise SGPA
- Number of subjects in each semester

### Analytics
The web application currently includes an initial analytics system with:
- SGPA trend visualization
- Subject performance data
- Grade distribution data

More analytics and visualizations are planned for future releases.

## Grade Scale

| Marks | Grade | Grade Point |
|------:|:-----:|------------:|
| 90–100 | O | 10 |
| 80–89 | A+ | 9 |
| 70–79 | A | 8 |
| 60–69 | B+ | 7 |
| 55–59 | B | 6 |
| 50–54 | C | 5 |
| 40–49 | P | 4 |
| < 40 | F | 0 |

## Tech Stack

- **Python**
- **Flask** — web framework
- **Jinja2** — HTML templating
- **Pandas** — academic data analysis
- **Chart.js** — data visualization
- **JSON** — local data persistence
- **HTML / CSS / JavaScript** — frontend

## Project Structure

```text
GradeVault/
│
├── models/
│   ├── subject.py
│   ├── semester.py
│   └── student.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── semester.html
│   ├── add_subject.html
│   ├── edit_subject.html
│   ├── add_semester.html
│   ├── create_student.html
│   ├── edit_student.html
│   └── analytics.html
│
├── static/
│   └── css/
│       └── style.css
│
├── analytics.py
├── storage.py
├── visualizer.py
├── app.py
├── main.py
├── gradevault.json
├── .gitignore
└── README.md