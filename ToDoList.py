#to do lits main function 
def ToDoList():
    enter = None
    while(enter!='exit' or '4'):
        print("--------------------------------------------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Exit")
        enter = input("choose anything: ")
        
        if enter =='1':
            addTask()
        elif enter == '2':
            removeTask()
        elif enter == '3':
            viewTask()
        elif enter == '4':
            break
        else:
            print("Enter valid number: ")

#adding a task to To DO List
def addTask():
    #TaskList = []
    task = input("Enter the task: ")
    print(f" '{task}' added to you TO DO LIST")
    TaskList.append(task)
    
    
#removing a task from To DO List
def removeTask():
    try:
        print("--------------------------------------------")
        viewTask()
        dlt = int(input('Enter task number you want to delete: '))
        print(f"'{TaskList[dlt-1]}' deleted succesfully..")
        TaskList.pop(dlt-1)

    except Exception:
        print(' Please enter valid number.. select among above')
        removeTask()
    
    
#showing all the tasks in To DO List
def viewTask():
    # print(TaskList)
    print("Your Task list is: ")
    for i,task in enumerate(TaskList, start=1):
        print(f"{i}. {task} ")
    #print("--------------------------------------------")


TaskList = []           #empty list
ToDoList()              #main function call


