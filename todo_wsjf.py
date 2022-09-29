'''
Problem: nie wiem czym sie zajac w pierwszej kolejnosci
Rozwiazanie: Sortowanie zadan na podstawie WSJF (https://www.scaledagileframework.com/wsjf/)
WSJF = Cost of delay / Job Duration (Job size)
    Cosy of delay = (1, 2, 3, 5, 8, 13, 20)
    Job size = (1, 2, 3, 5, 8, 13, 20)
Cost of delay = User-business Value + Time criticality + Risk reduction and/or Opportunity enablement
    User-business Value = (1, 2, 3, 5, 8, 13, 20)
    Time criticality = (1, 2, 3, 5, 8, 13, 20)
    Risk reduction and/or Opportunity enablement = (1, 2, 3, 5, 8, 13, 20)

Wynik:
- Spriorytetyzowana lista zadan
- dodawanie informacji o statusie, mozliwosc zmiany statusu
- wyswietlanie w kolumnach (kanban):

-
'''

import os

cmd = "clear"
file_location = "."
tasks = list()

def createTask():

    '''
    def checkCorrcectValue(value):
        fibonnaci_values = [1, 2, 3, 5, 8, 13, 20]
        if value not in fibonnaci_values:
            print("please provide proper value: 1, 2, 3, 5, 8, 13, 20")
            #
    '''
    '''
    TODO: add task (summary, description, Cosy of delay, Job size, User-business Value, Time criticality, Risk reduction and/or Opportunity enablement)
    result: input data saved as list
    '''
    summary = input("summary: ")
    value = input("value: ")
    size = input("size: ")
    timeCriticality = input("time criticality: ")
    riskReduction = input("risk reduction: ")

    task = list()
    task.extend([summary, value, size, timeCriticality, riskReduction])
    tasks.append(task)

def editTask(task):
    '''
    TODO:
        1. indicate task
        2. change value(s)
        3. save task with new values
    result: task saved with new values for calculations
    '''
    pass

def calculateCostOfDelay(task, value, duration, risk):
    '''
    TODO: Cost of delay = User-business Value + Time criticality + Risk reduction and/or Opportunity enablement
    reult: [Task, CostOfDelay] list
    '''
    pass

def calulateWSJF(task, CostOfDelay, size):
    '''
    TODO: WSJF = Cost of delay / Job Duration (Job size)
    resuly: list task and wsjf
    '''
    pass

def prioritizeTasks(tasksList):
    '''
    TODO:
    '''
    pass

def changeStatus(task):
    '''
    TODO: change task status:
    todo | in progress | blocked | delegated | review | done
    '''
def saveToFile(file_location):
    '''
    TODO: save list "tasks" into file so that I can close the app and get back in future

    '''
    f = open("todo_wsfj", "a")
    for task in tasks:
        f.write(str(task)+"\n")

    f.close()

menu_options = {
    1: 'show tasks',
    2: 'add task',
    3: '(-) edit task',
    4: '(!) delete task',
    5: 'exit'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option1():

    os.system(cmd)

    print("Display tasks:")
    print()

    # TODO: change to read task from file
    if len(tasks) > 0:
        for i in range(len(tasks)):
            print(str(i)+" - "+str(tasks[i]))
            #for task in tasks:
            #    print(str(i)+" - "+ str(task))
    else:
        print("There are no tasks")

    '''
    TODO: print in table: https://www.educba.com/python-print-table/
    TODO: prioritizeTasks() by wsjf
    TODO: read all tasks from file
    TODO: enable inedex to manipulate tasks edit/delete
    '''

def option2():
    os.system(cmd)

    print("Add new task:")
    print()

    createTask()

def option3():
    os.system(cmd)

    print("Edit task:")
    print()
    print("Choose task id from list")
    for i in range(len(tasks)):
        print(str(i)+" - "+str(tasks[i]))

    id = int(input("Task to edit: "))
    print()
    print("You will edit task:")
    print(tasks[id])

    print("TODO def editTask(task_id)")

def option4():
    os.system(cmd)

    print("Delete task:")
    print()

    print("Handle option Option 4")

if __name__=='__main__':

    while(True):
        #os.system(cmd)
        print()
        print("Menu:")
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('saving...')
            saveToFile(file_location)
            print("work saved")
            print("closing")
            exit()
        else:
            os.system(cmd)
            print('Invalid option. Please enter a number between 1 and 5.')
