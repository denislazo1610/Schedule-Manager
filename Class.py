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
            int(input('Zoom number: '))
        )
        
choice = input('Enter your choice:')

print("Hello, this is a Schedule programm!")
print("Choose a option:\n")
print("\'A\' for adding a subject")
print("\'B\' for deleting a subject")
print("\'C\' for changing a subject")
print("\'D\' for see your schedule")
print("\'E\' for exit of this programm\n")


subjects = {}

if ((choice == 'A') or (choice == 'a')):
    user = Subject.from_input()
    subjects[user.name] = user
    
elif ((choice == 'B') or (choice == 'b')):
    print('BBBBB')
elif ((choice == 'C') or (choice == 'c')):
    print('CCCCC')
elif ((choice == 'D') or (choice == 'd')):
    print('DDDDD')
elif ((choice == 'E') or (choice == 'e')):
    print('EEEEE')
else:
    print('Invalid input')

