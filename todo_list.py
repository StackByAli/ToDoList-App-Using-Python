import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Function to display all tasks
def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

# Function to edit a task
def edit_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to edit: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num - 1] = new_task
        save_tasks(tasks)
        print(f"Task {task_num} updated.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task number.")

# Main function to handle user input
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
