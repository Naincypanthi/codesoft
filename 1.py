
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}: {todo_list[task]}")


def add_task(todo_list):
    task = input("Enter task: ")
    description = input("Enter description: ")
    todo_list[task] = description
    print(f"Task '{task}' added to the to-do list.")


def remove_task(todo_list):
    task = input("Enter the task to remove: ")
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


def main():
    todo_list = {}

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
