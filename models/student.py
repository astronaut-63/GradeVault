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
