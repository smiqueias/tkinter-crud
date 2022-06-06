from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("todo-crud.db")


def create_table_todo():
    connection.execute("""
    create table if not exists tasks (
        id_task integer primary key autoincrement,
        task text,
        done integer
    )
    """)


def add_task(task):
    connection.execute(
        "insert into tasks (task, done) values (?, 0)", (task, ))
    connection.commit()


def remover_tarefa(id):
    connection.execute("delete from tasks where id_task = ?", (id, ))
    connection.commit()


def get_tarefas():
    return connection.execute("select id_task, task, done from tasks")
