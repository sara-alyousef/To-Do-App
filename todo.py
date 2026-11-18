print("Welcome to the To-Do List App!")
print("1. Add tasks")
print("2. View tasks")
print("3. Remove tasks")
print("4. Quit")


def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.rstrip("\n"))
    except FileNotFoundError:
        pass
    return tasks

tasks = load_tasks()

def add_tasks(tasks):
    while True:
        task = input("Add a task (or type \"done\" to finish): ")
        if task.lower() == "done":
            break
        if task == "" or task.isspace():
            print("Task cannot be empty. Please try again.")
        else:
            tasks.append(task)

def view_tasks(tasks):
    if tasks:
        print(f"Your tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks to show yet.")


def remove_tasks(tasks):
    while True:
        task_remove = input("Remove a task (or type \"done\" to finish): ")
        if task_remove.lower() == "done":
                break
        for task in tasks:
            if task_remove.lower() == task.lower():
                print(f"Removing task: {task_remove}")
                tasks.remove(task)
                break 
        else:
            print("Task not found. Please try again.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    user_input = input("What would you like to do? ")
    if user_input == "1":
        add_tasks(tasks)
    elif user_input == "2":
        view_tasks(tasks)
    elif user_input == "3":
        remove_tasks(tasks)
    elif user_input == "4":
        print("Cya later!")
        save_tasks(tasks)
        break
    else:
        print("Please enter number 1, 2, 3, or 4.")
