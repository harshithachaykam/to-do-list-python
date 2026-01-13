def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")


def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")


def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Error occurred!")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!")
