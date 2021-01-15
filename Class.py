class Subject:
    def __init__(self, name, time, difficulty, proffesor, zoomNumber):
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.proffesor = proffesor
        self.zoomNumber = zoomNumber
    
    @classmethod
    def from_input(cls):
        return cls(
            input('Name: '),
            input('Time: '),
            input('Difficulty: '),
            input('Professor: '),
            input('Zoom number: ')
        )
        
def options():
    print("Choose a option:\n")
    print("\'A\' for adding a subject")
    print("\'B\' for deleting a subject")
    print("\'C\' for changing a subject")
    print("\'D\' for see your schedule")
    print("\'E\' for write schedule in another file")
    print("\'Exit\' for exit of this programm\n")

def optionInAction(choice):
    if((choice == 'A') or (choice == 'a')):
        user = Subject.from_input()
        subjects[user.name] = user
        print("Subject was added to you schedule\n")
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)
    elif((choice == 'B') or (choice == 'b')):
        print('BBBBB\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)
    elif ((choice == 'C') or (choice == 'c')):
        print('CCCCC\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)
    elif ((choice == 'D') or (choice == 'd')):
        print('DDDDD\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)
    elif ((choice == 'E')) or (choice == 'e'):
        print('EEEEEE\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)
    elif ((choice == 'Exit') or (choice == 'exit')):
        print('Thank you')
    else:
        print('Invalid input\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice)

print("Hello, this is a Schedule programm!")    
options()
choice = input('Enter your choice:')
subjects = {}
optionInAction(choice)

