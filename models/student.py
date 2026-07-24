from semester import Semester


class Student:

    def __init__(self, name, roll_number):
        self.semesters = []
        self.name = name
        self.roll_number = roll_number

    def add_semester(self, new_semester):
        for existing_semester in self.semesters:
            if new_semester.number == existing_semester.number:
                raise ValueError('This semester already exists!')

        self.semesters.append(new_semester)

    def find_semester(self, number):
        for semester in self.semesters:
            if semester.number == number:
                return semester
        raise ValueError('Semester not found!')

    def calculate_cgpa(self):
        numerator = 0
        denominator = 0
        for semester in self.semesters:
            credits = semester.get_total_credits()
            numerator += semester.calculate_sgpa() * credits
            denominator += credits
        if denominator == 0:
            raise ValueError(
                'Cannot calculate CGPA because no subjects have been added.')
        return numerator/denominator

    def remove_semester(self, number):
        semester_to_remove = self.find_semester(number)
        self.semesters.remove(semester_to_remove)

    def to_dict(self):
        semester_list = []
        for semester in self.semesters:
            semester_list.append(semester.to_dict())
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "semesters": semester_list
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["name"], data["roll_number"])
        for semester_data in data["semesters"]:
            semester = Semester.from_dict(semester_data)
            student.add_semester(semester)
        return student
