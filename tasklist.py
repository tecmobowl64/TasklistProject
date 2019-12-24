# Import OS and sqlite for the program to use
import sqlite3
import os

# Database connection
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None

# Function to select all tasks
def get_all_tasks():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(BASE_DIR, "todo.db")
    conn = create_connection(db_file)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute('select * from tasks where completionStatus != 1')
            all_rows = c.fetchall()
        except Error as e:
            print(e)
    else:
        print("No connection")
    conn.commit()
    conn.close()
    # return all_rows
    for line in all_rows:
        print(*line)

# Function to select all completed tasks
def get_completed_tasks():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(BASE_DIR, "todo.db")
    conn = create_connection(db_file)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute('select * from tasks where completionStatus = 1')
            all_rows = c.fetchall()
        except Error as e:
            print(e)
    else:
        print("No connection")
    conn.commit()
    conn.close()
    # return all_rows
    for line in all_rows:
        print(*line)

# Function to add a new task
def addTask():
    print("Adding new task...")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(BASE_DIR, "todo.db")
    conn = create_connection(db_file)
    if conn is not None:
        try:
            task_lnum = input("List Number:")
            task_desc = input("Description:")
            task_pri = input("Priority:")
            task_cat1 = input("Category 1:")
            task_cat2 = input("Category 2:")
            task_due = input("Due Date:")
            addScript = 'insert into tasks (listId,description,priority,category1,category2,dueDate,completionStatus) values (?,?,?,?,?,?,0)'
            c = conn.cursor()
            c.execute(addScript, (task_lnum,task_desc,task_pri,task_cat1,task_cat2,task_due))
            print("Task successfully added.")
        except Exception as e:
            print(e)
    else:
        print("No connection")
    conn.commit()
    conn.close()
    return "Task added!"

# Function to mark task as complete
def markComplete():
    print("Mark task as complete...")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(BASE_DIR, "todo.db")
    conn = create_connection(db_file)
    if conn is not None:
        try:
            task_num = input("Type some or part of the task description: ")
            c = conn.cursor()
            c.execute('update tasks set completionStatus=1 where description like ?', ('%'+task_num+'%',))
            print("Task marked as complete!")
        except Exception as e:
            print(e)
    else:
        print("No connection")
    conn.commit()
    conn.close()
    return "Task complete!"

# print(get_all_tasks())
# markComplete()
