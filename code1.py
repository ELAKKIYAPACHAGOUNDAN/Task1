tasks = []

def addtask(taskname):
    task = {"Taskname": taskname, "Completed": False}
    tasks.append(task)

def viewtask():
    for index, task in enumerate(tasks):
        status = "Done" if task["Completed"] else "Not Completed"
        print(f"{index + 1}. {task['Taskname']} - {status}")

def markasdone(taskindex):
    if 0 <= taskindex < len(tasks):
        tasks[taskindex]["Completed"] = True

def removetask(taskindex):
    if 0 <= taskindex < len(tasks):
        del tasks[taskindex]

while True:
    print("\nTo-do List:")
    print("i) Add the task")
    print("ii) View the tasks")
    print("iii) Mark task as done")
    print("iv) Delete a task")
    print("v) Windup")
    choice = input("Your choice: ")

    if choice == "i":
        taskname = input("Your task name is: ")
        addtask(taskname)
    elif choice == "ii":
        viewtask()
    elif choice == "iii":
        taskindex = int(input("Select the task to be marked as done: "))
        markasdone(taskindex - 1)
    elif choice == "iv":
        taskindex = int(input("Select the task to be removed: "))
        removetask(taskindex - 1)
    elif choice == "v":
        print("No task is there.. So, Add some task to inprove your skills!!..")
        break
    else:
        print("Enter the correct choice")
