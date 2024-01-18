import sys

def display_tasks(tasks):
    """Display the current list of tasks."""
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)

def delete_task(tasks):
    """Delete a task from the list."""
    try:
        num = int(input("Enter the number of the task to delete: "))
        del tasks[num - 1]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number corresponding to a task.")

def mark_complete(tasks):
    """Mark a task as completed."""
    try:
        num = int(input("Enter the number of the task to mark as complete: "))
        tasks[num - 1] = f"{tasks[num - 1]} (completed)"
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number corresponding to a task.")

def main():
    """Main function to run the to-do list application."""
    tasks = []

    while True:
        display_tasks(tasks)
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Mark a task as complete")
        print("4. Quit")

        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number corresponding to an option.")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            delete_task(tasks)
        elif choice == 3:
            mark_complete(tasks)
        elif choice == 4:
            sys.exit(0)
        else:
            print("Invalid input. Please enter a number corresponding to an option.")

if __name__ == "__main__":
    main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 