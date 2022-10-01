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
import time
from tabulate import tabulate

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
    DONE: add task (summary, description, Cosy of delay, Job size, User-business Value, Time criticality, Risk reduction and/or Opportunity enablement)
    result: input data saved as list
    '''
    global summary
    summary = input("summary: ")
    global value
    value = int(input("value: "))
    global size
    size = int(input("size: "))
    global timeCriticality
    timeCriticality = int(input("time criticality: "))
    global riskReduction
    riskReduction = int(input("risk reduction: "))
    print()
    print("...task created")


    task = list()

    calculateCostOfDelay(value, size, timeCriticality, riskReduction)

    calulateWSJF(cost_of_delay, size)

    task.extend([summary, value, size, timeCriticality, riskReduction, cost_of_delay, wsjf])
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

def calculateCostOfDelay(value, size, duration, risk):
    '''
    DONE: Cost of delay = User-business Value + Time criticality + Risk reduction and/or Opportunity enablement
    reult: [Task, CostOfDelay] list
    '''
    global cost_of_delay
    cost_of_delay = int(value) + int(size) + int(timeCriticality) + int(riskReduction)

    return(cost_of_delay)

def calulateWSJF(cost_of_delay, size):
    '''
    DONE: WSJF = Cost of delay / Job Duration (Job size)
    resuly: list task and wsjf
    '''
    global wsjf
    wsjf = cost_of_delay / size

    return(wsjf)

def changeStatus(task):
    '''
    TODO: change task status:
    todo | in progress | blocked | delegated | review | done
    '''
def saveToFile(file_location):
    '''
    DONE: save list "tasks" into file so that I can close the app and get back in future
    '''
    f = open("todo_wsfj", "a")
    for task in tasks:
        f.write(str(task)+"\n")

    f.close()

def sortTasks(list):
    tasks.sort(key=lambda x:x[6])


menu_options = {
    1: 'show tasks',
    2: 'add task',
    3: 'edit task (in progress)',
    4: 'delete task (not started)',
    5: 'save and exit'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option1():

    os.system(cmd)

    print("Display tasks:")
    print()

    # TODO: change to read task from file
    sortTasks(tasks)
    tasks.reverse()

    '''
    if len(tasks) > 0:
        for i in range(len(tasks)):
            #print(str(i)+" - "+str(tasks[i][0]+" - "+str(tasks[i][6])))
            print(str(i)+" - "+str(tasks[i]))
            #for task in tasks:
            #    print(str(i)+" - "+ str(task))

    else:
        print("There are no tasks")
    '''

    ## Tables, take 1
    print (tabulate(tasks, headers=["Task", "Value", "Size", "Crit.", "Risk Red.", "CoD", "WSJF"]))



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

    os.system(cmd)

    while(True):
        #os.system(cmd)

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
           print()
        elif option == 2:
            option2()
            print()
        elif option == 3:
            option3()
            print()
        elif option == 4:
            option4()
            print()
        elif option == 5:
            print('...saving...')
            saveToFile(file_location)
            time.sleep(0.5)
            print("...work saved...")
            time.sleep(0.5)
            print("...closing")
            time.sleep(0.5)
            os.system(cmd)
            exit()
        else:
            os.system(cmd)
            print('Invalid option. Please enter a number between 1 and 5.')
