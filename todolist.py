# Simple To-Do List Application in Python

tasks = []  # empty list to store tasks

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet! Add some.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔️ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added!")

def remove_task():
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Task '{removed['title']}' removed!")
    except (ValueError, IndexError):
        print("Invalid choice!")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        print(f"Task '{tasks[num-1]['title']}' marked as done!")
    except (ValueError, IndexError):
        print("Invalid choice!")

while True:
    show_menu()
    choice = input("Choose option: ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye! ✅")
        break
    else:
        print("Invalid option, try again.")
