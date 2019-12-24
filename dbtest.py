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

# Select all from responses table
def get_responses():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(BASE_DIR, "responsedb.db")
    conn = create_connection(db_file)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute('select * from tasks where completionStatus != 1 order by dueDate desc')
           #  c.execute('SELECT * FROM responses')
            all_rows = c.fetchall()
        except Error as e:
            print(e)
    else:
        print("No connection")
    conn.commit()
    conn.close()
    return all_rows

# responses = get_responses()
# print(responses)
