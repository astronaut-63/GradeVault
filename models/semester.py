from models.subject import Subject


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

    def find_subject(self, name):
        for subject in self.subjects:
            if subject.name == name:
                return subject
        raise ValueError('Subject not found.')

    def remove_subject(self, name):
        subject_to_remove = self.find_subject(name)
        self.subjects.remove(subject_to_remove)

    def to_dict(self):
        subject_list = []
        for subject in self.subjects:
            subject_list.append(subject.to_dict())
        return {
            "number": self.number,
            "subjects": subject_list
        }

    @classmethod
    def from_dict(cls, data):
        semester = cls(data["number"])
        for subject_data in data["subjects"]:
            subject = Subject.from_dict(subject_data)
            semester.add_subject(subject)
        return semester
