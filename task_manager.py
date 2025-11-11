# --------------------------------------------
# Simple Task Manager App
# Made by: [Your Name]
# --------------------------------------------

# Global list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\n========== TASK MANAGER ==========")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Exit")
    print("==================================")

# Function to add a new task
def add_task():
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("⚠️  Task cannot be empty.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task
def remove_task():
    if not tasks:
        print("⚠️  No tasks to remove.")
        return

    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"🗑️  Task '{removed}' removed successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

# Function to run the main app
def run_task_manager():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    run_task_manager()
