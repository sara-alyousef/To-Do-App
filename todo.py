print("Welcome to the To-Do List App!")

def menu():
    print("\n--- MENU ---")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Quit\n")


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
        print("\n--- YOUR TASKS ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to show yet.")


def remove_tasks(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    
    while tasks:

        user_choice = input("\nRemove a task by entering its number (or type \"done\" to finish): ").strip()
        if user_choice.lower() == "done":
            break
        
        try:
            task_number = int(user_choice)
            if task_number < 1:
                print("Please enter a number starting from 1.")
                continue

            task_index = task_number - 1
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task}")

        except ValueError:
            print("Please enter a number.")
        except IndexError:
            print("That task number isn't on the list.")

    if not tasks:
        print("No tasks left.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    menu()
    user_input = input("What would you like to do? ")
    if user_input == "1":
        add_tasks(tasks)
    elif user_input == "2":
        view_tasks(tasks)
        input("\nPress Enter to return to the menu...")
    elif user_input == "3":
        remove_tasks(tasks)
    elif user_input == "4":
        print("Cya later!")
        save_tasks(tasks)
        break
    else:
        print("Please enter number 1, 2, 3, or 4.")
