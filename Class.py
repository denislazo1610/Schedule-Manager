class Subject:
    def __init__(self, name, time, difficulty, proffesor, zoomNumber):
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.time = time
        self.proffesor = proffesor
        self.zoomNumber = zoomNumber
        

print("Hello, this is a Schedule programm!")
print("Choose a option:\n")
print("\'A\' for adding a subject")
print("\'B\' for deleting a subject")
print("\'C\' for changing a subject")
print("\'D\' for see your schedule")
print("\'E\' for exit of this programm\n")

choice = input('Enter your choice:')

if ((choice == 'A') or (choice == 'a')):
    print('AAAAAAA')
elif ((choice == 'B') or (choice == 'b')):
    print('BBBBB')
elif ((choice == 'C') or (choice == 'c')):
    print('CCCCC')
elif ((choice == 'D') or (choice == 'd')):
    print('DDDDD')
elif ((choice == 'E') or (choice == 'e')):
    print('EEEEE')
else:
    print('Invalid input')e

