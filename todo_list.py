class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")

    def add_task(self, task_name):
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"Task '{task_name}' added to your to-do list.")

    def mark_task_completed(self, task_number):
        index = task_number - 1
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            print(f"Task '{self.tasks[index]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        index = task_number - 1
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task['name']}' removed from your to-do list.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
            
