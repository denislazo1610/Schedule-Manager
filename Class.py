import os

class Subject:
    # This is the attributes of the class "Subject"
    def __init__(self, name, time, days, difficulty, professor, zoomNumber):
        self.name = name
        self.time = time
        self.days = days
        self.difficulty = difficulty
        self.professor = professor
        self.zoomNumber = zoomNumber
    
    # In here, the user will be asked the information of every subject
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

# This is a function that will give options to the users.      
def options():
    print("Choose a option:\n")
    print("\'A\' for adding a subject")
    print("\'B\' for deleting a subject")
    print("\'C\' for changing a subject")
    print("\'D\' for see your schedule")
    print("\'E\' for write schedule in another file")
    print("\'Exit\' for exit of this programm\n")

#This function depends on the answer from the previous function. 

def optionInAction(choice, subjects, Schedule):
#In here, the user is adding a subject to the schedule.
    if((choice == 'A') or (choice == 'a')):
        os.system("cls")
        print("Details of class: \n")
        
#In this part, the time is being chnages, if the use put "2 pm", then it is going to be 
#savved "02 pm". The reason is for the next functions. 
        user = Subject.from_input()
        if (user.time[1] == ' '):
            user.time = '0' + user.time

        if(user.time[0] == ' '):
            user.time = user.time[1:]
            user.time = '0' + user.time

        subjects[user.name] = user
        os.system("cls")

        print("Subject was added to you schedule\n")
# In here, we are asking to the user again the options. 
        options()
        choice = input('Enter your choice:')

        os.system("cls")
        optionInAction(choice, subjects, Schedule)

#In this part, the user will be able to delete a subject that the user has.

    elif((choice == 'B') or (choice == 'b')):

        os.system("cls")

        print('This is all your classes:\n')
        for key in subjects:
            print(key)
        print('\n')
        respuesta = input("Which one do you want to delete? ")
        if respuesta in subjects:
            delete = subjects.pop(respuesta)
            os.system("cls")
            print('Removed element: ', respuesta)
            
        else:
#If the user is trying to delete a subject that the user does not have, then this will happen.
            os.system("cls")
            print('You do not have that subject!\n')

#in this part, we are giving to the user the options again
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

#In this part, the user will be able to chnage the information of every subject that the user has. 
    elif ((choice == 'C') or (choice == 'c')):
        os.system("cls")
        print('This is all your classes:\n')
        for key in subjects:
            print(key)
        print('\n')
        respuesta = input('What subject do you want to change? ')

        os.system("cls")
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
            os.system("cls")

            if (change == 'Name'): 
                subjects[respuesta].name = newInformation
                subjects[newInformation] = subjects.pop(respuesta)
            elif ((change == 'Time') or (change == 'time')):
                if (newInformation[1] == ' '):
                    newInformation = '0' + newInformation

                if(newInformation[0] == ' '):
                    newInformation = newInformation[1:]
                    newInformation = '0' + newInformation
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
                os.system("cls")
                print('Change denied')
        else:
            os.system("cls")
            print('That subject is not included\n')


        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

#In this part, the user will be able to see the schedule.
   
    elif ((choice == 'D') or (choice == 'd')): 
        os.system("cls")

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
                            elif(len(subjects[key].name) > len(Schedule[i][j])):
                                 diferencia = (len(subjects[key].name)-(len(Schedule[i][j])))
                
                            Schedule[i][j] = subjects[key].name

        
        

        for i in range(len(Schedule)):
            for j in range(len(Schedule[i])):
                print(Schedule[i][j], end=' ')
            print()    
        print('\n')
        correction = input('Do you like your Schedule? (yes/no) ')
        os.system("cls")
        if ((correction == 'Yes') or (correction == 'yes')):
            print('Nice!\n')
        else:
            print('You can change it\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

#In this part, the program will  create another file containing all the added subjects
    elif ((choice == 'E')) or (choice == 'e'):
        os.system("cls")
    
        newFile = input('Create a file: \n')

        with open(newFile, "w+") as writer:
            for j in range(len(Schedule)):
                for i in range(len(Schedule[j])):
                    information = (Schedule[j][i])
                    writer.write(information)
                writer.write("\n")
        os.system("cls")

        print("File created\n")
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

#In here, the user decide to exit from the program
    elif ((choice == 'Exit') or (choice == 'exit')):
        os.system("cls")
        print('Thank you')

#In this part, if the user type other thing besides the options, this will happen

    else:
        os.system("cls")
        print('Invalid input\n')
        options()
        choice = input('Enter your choice:')
        optionInAction(choice, subjects, Schedule)

#This is the schedule

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

Level = [["Hard:     ", "Medium:    ", "Easy:    "]]

os.system("cls")

print("Hello, this is a Schedule programm!")    
options()
choice = input('Enter your choice:')
subjects = {}
optionInAction(choice, subjects, Schedule)



