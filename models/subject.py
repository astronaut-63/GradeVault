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

