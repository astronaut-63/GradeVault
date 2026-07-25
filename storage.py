from models.student import Student

import json


def save_student(student):
    data = student.to_dict()

    with open("gradevault.json", "w") as file:
        json.dump(data, file, indent=4)


def load_student():
    try:
        with open('gradevault.json', 'r') as file:
            data = json.load(file)
            return Student.from_dict(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
