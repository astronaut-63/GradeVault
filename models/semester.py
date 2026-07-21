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
