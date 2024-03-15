from datetime import datetime, timedelta

class TodoList:
    def __init__(self):
        self.todo_dict = {}

    def add_task(self, date, task):
        current_date = datetime.now().date()
        if date < current_date:
            print("Error: Cannot add tasks for past dates.")
        elif date in self.todo_dict:
            self.todo_dict[date].append(task)
            self.todo_dict[date].sort()  # Ensure tasks are ordered
        else:
            self.todo_dict[date] = [task]

    def delete_task(self, date, index):
        current_date = datetime.now().date()
        if date < current_date:
            print("Error: Cannot modify tasks for past dates.")
            return
        if date in self.todo_dict and index < len(self.todo_dict[date]):
            del self.todo_dict[date][index]
        else:
            print("Error: Task index out of range or date not found.")

    def get_tasks(self, date):
        current_date = datetime.now().date()
        if date < current_date:
            print("Error: Cannot access tasks for past dates.")
            return []
        elif date > current_date:
            print("Error: Cannot access tasks for future dates.")
            return []
        elif date in self.todo_dict:
            return self.todo_dict[date]
        else:
            return []

# Example usage
todo_list = TodoList()

# Add tasks for today
todo_list.add_task(datetime.now().date(), "Complete assignment")
todo_list.add_task(datetime.now().date(), "Go for a run")

# Attempt to add task for past date (should return error)
todo_list.add_task(datetime.now().date() - timedelta(days=1), "Test")

# Attempt to add task for future date (should return error)
todo_list.add_task(datetime.now().date() + timedelta(days=1), "Plan for tomorrow")

# Print tasks for today
print("Tasks for today:", todo_list.get_tasks(datetime.now().date()))

# Delete a task from today's list
todo_list.delete_task(datetime.now().date(), 1)

# Print tasks for today after deletion
print("Tasks for today after deletion:", todo_list.get_tasks(datetime.now().date()))
