GRADE_POINTS = {'O': 10, 'A+': 9, 'A': 8,
                'B+': 7, 'B': 6, 'C': 5, 'P': 4, 'F': 0}


class Subject:

    def __init__(self, name, credits, obtained_marks):
        if not name.strip():
            raise ValueError('Enter a valid name.')

        if credits <= 0:
            raise ValueError('Enter valid credits.')

        if not 0 <= obtained_marks <= 100:
            raise ValueError('Enter valid marks.')

        self.name = name
        self.credits = credits
        self.obtained_marks = obtained_marks

    def get_grade(self):
        if 90 <= self.obtained_marks <= 100:
            return 'O'
        elif 80 <= self.obtained_marks < 90:
            return 'A+'
        elif 70 <= self.obtained_marks < 80:
            return 'A'
        elif 60 <= self.obtained_marks < 70:
            return 'B+'
        elif 55 <= self.obtained_marks < 60:
            return 'B'
        elif 50 <= self.obtained_marks < 55:
            return 'C'
        elif 40 <= self.obtained_marks < 50:
            return 'P'
        elif self.obtained_marks < 40:
            return 'F'

    def get_grade_point(self):
        grade = self.get_grade()
        return GRADE_POINTS.get(grade)
