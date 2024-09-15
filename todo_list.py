# Class to represent a task in the to-do list
class Task:
    def __init__(self, description):
        self.description = description
        self.is_complete = False
    
    def mark_complete(self):
        self.is_complete = True
    
    def update_description(self, new_description):
        self.description = new_description

# Class to represent the to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    # Add a new task
    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f'Task added: {description}')
    
    # Edit an existing task
    def edit_task(self, index, new_description):
        if index < len(self.tasks):
            self.tasks[index].update_description(new_description)
            print(f'Task updated to: {new_description}')
        else:
            print('Task not found')
    
    # Delete a task
    def delete_task(self, index):
        if index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task deleted: {removed_task.description}')
        else:
            print('Task not found')
    
    # Mark a task as complete
    def mark_task_complete(self, index):
        if index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f'Task marked as complete: {self.tasks[index].description}')
        else:
            print('Task not found')
    
    # Display all tasks
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Complete" if task.is_complete else "Incomplete"
                print(f"{i + 1}. {task.description} - {status}")

# Simple Menu for the To-Do List Application
def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Display All Tasks")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        
        elif choice == '2':
            index = int(input("Enter task number to edit: ")) - 1
            new_description = input("Enter new task description: ")
            todo_list.edit_task(index, new_description)
        
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        
        elif choice == '4':
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_task_complete(index)
        
        elif choice == '5':
            todo_list.display_tasks()
        
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
