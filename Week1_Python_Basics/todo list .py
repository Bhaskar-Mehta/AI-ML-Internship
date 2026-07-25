"""
Week 1 - Simple CLI To-Do List
Supports: add, view, complete, delete tasks (in-memory)
"""

tasks = []


def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Added task: {title}")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}")
    print()


def complete_task(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        print(f"Marked '{tasks[index - 1]['title']}' as done.")
    else:
        print("Invalid task number.")


def delete_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")


def main():
    print("=== Simple CLI To-Do List ===")
    print("Commands: add, view, complete, delete, exit\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            title = input("Task title: ")
            add_task(title)

        elif command == "view":
            view_tasks()

        elif command == "complete":
            view_tasks()
            try:
                index = int(input("Task number to mark complete: "))
                complete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "delete":
            view_tasks()
            try:
                index = int(input("Task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Use: add, view, complete, delete, exit")


if __name__ == "__main__":
    main()