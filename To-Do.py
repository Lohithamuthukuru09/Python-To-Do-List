tasks = []

def show_menu():
    print("\n--- Lohitha's To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Added: {task}")
    elif choice == '2':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete!")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid number!")
    elif choice == '4':
        print("Bye! Keep coding!")
        break
    else:
        print("Invalid choice! Try 1-4")
