class Subject:
    def __init__(self, name, time, difficulty, professor, zoomNumber):
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.professor = professor
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

def optionInAction(choice, subjects):
    if((choice == 'A') or (choice == 'a')):
        user = Subject.from_input()
        subjects[user.name] = user
        print("Subject was added to you schedule\n")
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

    elif((choice == 'B') or (choice == 'b')):
        print('This is all your classes:\n')
        for key in subjects:
            print(key)
        print('\n')
        respuesta = input("Which one do you want to delete? ")
        if respuesta in subjects:
            delete = subjects.pop(respuesta)
            print('Removed element: ', delete)
        else:
            print('You do not have that subject!')

        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

    elif ((choice == 'C') or (choice == 'c')):
        print('This is all your classes:\n')
        for key in subjects:
            print(key)
        print('\n')
        respuesta = input('What subject do you want to change? ')
        print('This is all the information of that subject:\n')
        print("Name: " + subjects[respuesta].name)
        print("Time: " + subjects[respuesta].time)
        print("Difficulty: " + subjects[respuesta].difficulty)
        print("Professor: " + subjects[respuesta].professor)
        print("Zoom number: " + subjects[respuesta].zoomNumber)
        print('\n')

        change = input("What do you want to change? ")
        print('\n')
        newInformation = input('What do you want to put instead? ')
        print('\n')

        if (change == 'Name'): 
            subjects[respuesta].name = newInformation
            subjects[newInformation] = subjects.pop(respuesta)
        elif ((change == 'Time') or (change == 'time')):
            subjects[respuesta].time = newInformation
        elif ((change == 'Difficulty') or (change == 'difficulty')):
            subjects[respuesta].difficulty = newInformation
        elif ((change == 'Professor') or (change == 'professor')):
            subjects[respuesta].professor = newInformation
        elif ((change == 'Zoom number') or (change == 'zoom number')):
            subjects[respuesta].zoomNumber = newInformation
        else:
            print('Change denied')
        
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

    elif ((choice == 'D') or (choice == 'd')):
        print('DDDDD\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

    elif ((choice == 'E')) or (choice == 'e'):
        print('EEEEEE\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

    elif ((choice == 'Exit') or (choice == 'exit')):
        print('Thank you')

    else:
        print('Invalid input\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects)

print("Hello, this is a Schedule programm!")    
options()
choice = input('Enter your choice:')
subjects = {}
optionInAction(choice, subjects)

#print('wanna check out your subjects?')
#answer = input('answer yes or no:')
#if (answer == 'yes'):
  
#else:
    #print('That is all')

