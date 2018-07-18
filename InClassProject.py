def getList():
    print("Congradulations! You're running Mike's Task List Program.")
    print("What yould you like to do next?")
    print('1. List all tasks')
    print('2. Add task to list')
    print('3. Delete a task')
    print('q. To quit the program')

command = input()
ArrayOfTasks = []

while (command != 'q'):

if (command == '1'):
    for arrayitems in ArrayOfTasks:
        print(arrayitems)
        command = input()
if (command == '2'):
    newTask = input('New Task')
    ArrayOfTasks.append(newTask)
    command = input()
if (command == '3'):
    removeTask = input("Delete Task")
    ArrayOfTasks.pop(removeTask)
    command = input()
