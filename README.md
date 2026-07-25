# GradeVault

GradeVault is a command-line application built in Python to manage a student's academic records. It allows users to add semesters and subjects, calculate SGPA and CGPA, edit or remove records, and automatically save data using JSON.

This project was built to practice object-oriented programming, file handling, JSON serialization, and Git.

---

## Features

- Create a student profile
- Add and remove semesters
- Add, edit, and remove subjects
- Calculate SGPA for each semester
- Calculate overall CGPA
- Automatic validation of subject details
- Persistent storage using JSON
- View detailed semester and student information

---

## Project Structure

```
gradevault/
│
├── models/
│   ├── subject.py
│   ├── semester.py
│   └── student.py
│
├── storage.py
├── main.py
├── README.md
└── .gitignore
```

---

## Concepts Used

- Object-Oriented Programming
- Classes and Objects
- Encapsulation
- Composition
- Exception Handling
- File Handling
- JSON Serialization / Deserialization
- Git & GitHub

---

## Installation

Clone the repository

```bash
git clone https://github.com/astronaut-63/GradeVault.git
```

Navigate into the project

```bash
cd gradevault
```

Run the application

```bash
python main.py
```

---

## Example

```
1. Create Student
2. Add Semester
3. Add Subject
4. View Student
5. View Semester
6. Edit Subject
7. Delete Subject
8. Delete Semester
9. Exit
```

---

## Future Improvements

- Support multiple students
- Export data to CSV
- Search subjects
- Dashboard with statistics
- GPA trend visualization

---

## What I Learned

Building GradeVault helped me gain practical experience with:

- Designing applications using object-oriented programming
- Structuring projects across multiple modules
- Writing reusable methods instead of duplicating logic
- Serializing objects using JSON
- Reading from and writing to files
- Maintaining a clean Git commit history

---

## Author

AstroNaut