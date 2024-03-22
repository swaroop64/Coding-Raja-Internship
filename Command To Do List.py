import sqlite3
import datetime

# Database connection
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, task TEXT, priority TEXT, due_date TEXT)''')
conn.commit()

def add_task(task, priority, due_date):
    c.execute("INSERT INTO tasks (task, priority, due_date) VALUES (?, ?, ?)", (task, priority, due_date))
    conn.commit()
    print("Task added successfully!")

def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    print("ID | Task | Priority | Due Date")
    for task in tasks:
        print(task)

def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(task, priority, due_date)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = input("Enter ID of task to delete: ")
            delete_task(task_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

    conn.close()

if __name__ == "__main__":
    main()
