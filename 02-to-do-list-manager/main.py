from utils import generate_task_id, normalize_priority, normalize_status

tasks = []

def add_task():
    title = input("Enter the task: ").strip()
    if not title:
        print("❌ Task title cannot be empty")
        return
    
    priority_input = input("Enter priority (1=High, 2=Medium, 3=Low): ")
    priority = normalize_priority(priority_input)
    if priority is None:
        print("❌ Invalid priority")
        return
    
    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "status": "pending",
        "priority": priority
    }

    tasks.append(task)
    print(f"✅ Task added successfully (ID: {task['id']})")

def view_tasks():
    if not tasks:
        print("📭 No tasks available")
        return

    print("\nID | Title | Status | Priority")
    print("-" * 35)
    for task in tasks:
        print(
            f"{task['id']} | {task['title']} | {task['status']} | {task['priority']}"
        )     

def update_task_status():
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("❌ Invalid task ID")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            new_status_input = input("Enter new status (pending/done): ")
            new_status = normalize_status(new_status_input)

            if new_status is None:
                print("❌ Invalid status")
                return
            
            task["status"] = new_status
            print("✅ Task status updated")
            return
    
    print("❌ Task not found.")

def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("❌ Invalid task ID")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑️ Task deleted successfully")
            return

    print("❌ Task not found")

def main_menu():
    while True:
        print("\n📝 TO-DO LIST")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task status")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task_status()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List Manager")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main_menu()
