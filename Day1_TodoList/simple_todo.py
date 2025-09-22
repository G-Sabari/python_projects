

tasks = [] #empty list to store tasks

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    task = input ("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')


def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter a valid number!")


while True:
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()    
    elif choice == '2':
        add_task(tasks)
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")

