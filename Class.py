class Subject:
    def __init__(self, name, time, days, difficulty, professor, zoomNumber):
        self.name = name
        self.time = time
        self.days = days
        self.difficulty = difficulty
        self.professor = professor
        self.zoomNumber = zoomNumber
    
    @classmethod
    def from_input(cls):
        return cls(
            input('Name: '),
            input('Time: '),
            input('Days: '),
            input('Difficulty (Hard, Medium, Easy): '),
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

def optionInAction(choice, subjects, Schedule):
    if((choice == 'A') or (choice == 'a')):
        user = Subject.from_input()
        if (user.time[1] == ' '):
            user.time = '0' + user.time

        if(user.time[0] == ' '):
            user.time = user.time[1:]
            user.time = '0' + user.time

        subjects[user.name] = user
        print("Subject was added to you schedule\n")
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

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
        optionInAction(choice, subjects, Schedule)

    elif ((choice == 'C') or (choice == 'c')):
        print('This is all your classes:\n')
        for key in subjects:
            print(key)
        print('\n')
        respuesta = input('What subject do you want to change? ')
        if respuesta in subjects:
            print('This is all the information of that subject:\n')
            print("Name: " + subjects[respuesta].name)
            print("Time: " + subjects[respuesta].time)
            print("Days: " + subjects[respuesta].days)
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
            elif ((change == 'Days') or (change == 'days')):
                subjects[respuesta].days = newInformation
            elif ((change == 'Difficulty') or (change == 'difficulty')):
                subjects[respuesta].difficulty = newInformation
            elif ((change == 'Professor') or (change == 'professor')):
                subjects[respuesta].professor = newInformation
            elif ((change == 'Zoom number') or (change == 'zoom number')):
                subjects[respuesta].zoomNumber = newInformation
            else:
                print('Change denied')
        else:
            print('That subject is not included\n')

        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)
    
    elif ((choice == 'D') or (choice == 'd')): 

        print('\n')
        for key in subjects:
            positionOfTime = subjects[key].time
            positionOfDay = subjects[key].days
            for j in range(len(Schedule[0])):
                if (Schedule[0][j] == positionOfDay):                    
                    for i in range(len(Schedule)):
                        if (Schedule[i][0] == positionOfTime):
                            if(len(subjects[key].name) < len(Schedule[i][j])):
                                diferencia = (len(Schedule[i][j]) - (len(subjects[key].name)))
                                Schedule[i][j+1] = (diferencia*' ') + Schedule[i][j+1]

                            Schedule[i][j] = subjects[key].name


        for i in range(len(Schedule)):
            for j in range(len(Schedule[i])):
                print(Schedule[i][j], end=' ')
            print()    
        print('\n')
        correction = input('Do you like your Schedule? (yes/no) ')
        if ((correction == 'Yes') or (correction == 'yes')):
            print('Nice!\n')
        else:
            print('You can change it')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

    elif ((choice == 'E')) or (choice == 'e'):
        print('EEEEEE\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

    elif ((choice == 'Exit') or (choice == 'exit')):
        print('Thank you')

    else:
        print('Invalid input\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)


Schedule = [['     ','Monday','    ', 'Tuesday','    ', 'Wednesday','    ','Thursday','    ', 'Friday','    ', 'Saturday','    '] 
        , ['06 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['07 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['08 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['09 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['10 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['11 am','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['12 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['01 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['02 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['03 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['04 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']
        ,['05 pm','      ','    ','       ','    ','         ','    ','        ','    ','      ','    ','        ','    ']] 
print("Hello, this is a Schedule programm!")    
options()
choice = input('Enter your choice:')
subjects = {}
optionInAction(choice, subjects, Schedule)

