#fonctions
def add_task():
    task=input("add your task : ")
    note=input("enter a note related to this task : ")
    task_info={"task":task,"completed":False,"note":note}
    tasks.append(task_info)
    print("task added to the list succesfully !")
def mark_task_complete():
    incomplete_tasks=[task for task in tasks if task["completed"]==False]
    if not incomplete_tasks:
        print("no tasks to mark as completed !")
        print("-"*30)
        return 
    for i ,task in enumerate(incomplete_tasks):
        print(f"{i+1}-{task['task']}")
        print("-"*30)
    task_number=int(input("choose the task to complete : "))
    incomplete_tasks[task_number -1]["completed"]=True
    print("task marked completed !")
    print("-"*30)  
def view_task():
    if tasks:
        for i ,task in enumerate(tasks):
            status="✅"if task["completed"] else"❎"
            print(f'{i+1}.{task["task"]}{status}')
    else:
        print("there is no tasks !")
        print("-"*30)
#the pricipal programme
tasks=[]
message="""1-add tasks to do
2-mark tasks as complete
3-view tasks
4-quit"""
while True:
    print(message)
    choice=input("enter your choice : ")
    if choice=="1":
        add_task()
    elif choice=="2":
        mark_task_complete()
    elif choice=="3":
        view_task()
    elif choice=="4":
        break 
    else:
        print("invalide choice , please enter a number between 1 and 4")