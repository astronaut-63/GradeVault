class Semester:

    def __init__(self, number):
        self.number = number
        self.subjects = []

    def add_subject(self, new_subject):
        for existing_subject in self.subjects:
            if existing_subject.name == new_subject.name:
                raise ValueError(
                    f'A subject called {new_subject.name} already exists!')

        self.subjects.append(new_subject)

    def get_total_credits(self):
        total_credits = 0
        for subject in self.subjects:
            total_credits += subject.credits

        return total_credits

    def get_total_weighted_points(self):
        total_weighted_points = 0
        for subject in self.subjects:
            total_weighted_points += subject.credits * subject.get_grade_point()

        return total_weighted_points

    def calculate_sgpa(self):
        if not self.subjects:
            raise ValueError(
                'Cannot calculate SGPA for a semester with no subjects.')
        return round(self.get_total_weighted_points()/self.get_total_credits(), 2)
