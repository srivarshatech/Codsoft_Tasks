tasks=[]
def display_menu():
    print("\n" + "=" * 40)
    print("          TO-DO LIST")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task_name = input("\nEnter the task: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    print("-" * 40)

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['task']}")

def complete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    while True:
        try:
            task_number = int(input("\nEnter task number to mark as completed: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number.")
                continue

            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
            break

        except ValueError:
            print("Please enter a valid number.")


def update_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    while True:
        try:
            task_number = int(input("\nEnter task number to update: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number.")
                continue

            new_task = input("Enter the new task: ").strip()

            if new_task == "":
                print("Task cannot be empty.")
                continue

            tasks[task_number - 1]["task"] = new_task
            print("Task updated successfully!")
            break

        except ValueError:
            print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    while True:
        try:
            task_number = int(input("\nEnter task number to delete: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number.")
                continue

            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
            break

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            update_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Thank you for using the To-Do List!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()