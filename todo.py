import os
import sqlite3
import fire

# create data dir if not existed
try:
    os.makedirs(os.getcwd() + "/data", exist_ok=True)
except FileExistsError:
    raise

# for (root, dirs, files) in os.walk('python-todoList.github.io'):
#     print(root)
#     print(dirs)
#     print(files)
#     print('--------------------------------')

# create a default path to connect to and create (if necessary) a database
# os.path.dirname(filename) + os.path.basename(filename) == filename
# why do I need os.path.dirname instead of using abspath ?
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "database.sqlite3")
# print(DEFAULT_PATH)
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))

conn = sqlite3.connect(DEFAULT_PATH)

sql = """
    CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY,
        todo_text TEXT NOT NULL
    )
"""

cur = conn.cursor()
cur.execute(sql)

cur.execute("""
INSERT INTO todos (todo_text) VALUES ('finish the sql lab')
""")
conn.commit()

print("commit a query sucessfully")
conn.close()

def add_todo(name):
    return 'Hello {username}'.format(name=name)

if __name__ == "__main__":
    fire.Fire({
        'add_todo' : add_todo
    })