import json
import os

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists("todo.json"):
        return []
    with open("todo.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open("todo.json", "w") as file:
        json.dump(tasks, file, indent=4)

def list_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n📝 No tasks found.")
    else:
        print("\n📋 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("✅ Task added.")
    else:
        print("⚠ Task cannot be empty.")

def mark_task(tasks):
    """Mark a task as completed."""
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list."""
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """Main function to run the to-do app."""
    tasks = load_tasks()
    while True:
        print("\n📌 MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":

    main()
