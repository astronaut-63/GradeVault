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
            found = False
            if semester.number == number:
                found = True
                return semester
            if not found:
                raise ValueError('Semester not found!')
    
