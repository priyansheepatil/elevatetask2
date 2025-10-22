tasks = []

def loadTask():
    try:
        with open("list.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Could not read from the file.\n")
def saveTask():
    try:
         with open("list.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except IOError:
        print("Could not save tasks to the file.\n")

       
def addTask():
    task = input("Please enter a task:\n")
    tasks.append(task)
    saveTask()
    print("Task added.\n")

def delTask():
    viewTask()
    try:
        taskToDel = int(input("Please enter the task you want to delete:\n"))
        if taskToDel > 0 and taskToDel <= len(tasks):
            tasks.pop(taskToDel - 1)
            saveTask()
            print("Task deleted.")
        else:
            print("Task not found.\n")
    except:
        print("Invalid input.")

def viewTask():
    if not tasks:
        print("No task found.\n")
    else:
        print("Your tasks:\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

loadTask()

while True:
    print("To-do list\n")
    print("1. Add a new task\n")
    print("2. Delete a task\n")
    print("3. View all tasks\n")
    print("4. Quit\n")

    c= int(input("Enter your choice:\n"))

    if(c == 1):
        addTask()
    elif(c == 2):
        delTask()
    elif(c == 3):
        viewTask()
    elif(c == 4):
        break
    else:
        print("Invalid choice.")