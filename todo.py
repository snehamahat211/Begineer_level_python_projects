to_do_list=[]
def display_tasks():
    if not to_do_list:
        print ("No tasks to display")
    else:
        print("your tasks:")
        for i,task in enumerate(to_do_list, 1):
             print(f"{i}. {task}")
def add_task():
    task=input("Enter task")
    to_do_list.append(task)
    print(f"Task '{task}' added.")
def remove_task():
    tasknum=input("Enter task number")
    if 0<tasknum<=len(to_do_list):
        remove_task=to_do_list.pop(tasknum-1)
        print(f"Task '{remove_task}' removed.")
    else:
        print("Invalid task number.")
while True:

    print("1. Display")
    print("2.Add tasks")
    print("3.Remove tasks")
    print("4.Quit")
    choice = input("Choose an option: ")

    if choice =="1":
        display_tasks()
    elif choice =="2":
        add_task()
    elif choice =="3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select again.")




