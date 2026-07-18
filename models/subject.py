class Subject:

    def __init__(self):
        while True:
            self.name = input('Enter the subject name: ')
            if len(self.name) == 0:
                print('Enter a valid name.')
            else:
                break
        while True:
            try:
                self.credits = int(input('Enter the number of credits: '))
                if self.credits <= 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Enter a valid number of credits.')
        while True:
            try:
                self.obtained_marks = int(input('Enter the obtained marks: '))
                if not 0 < self.obtained_marks < 100:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Enter valid number of obtained marks.')

        print('Subject created!')



