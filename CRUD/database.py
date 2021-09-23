from peewee import *
import datetime
from .model import InputTodo, ShowTodo
db = SqliteDatabase('Todo.db')


class BaseModel(Model):
    class Meta:
        database = db


class Todo(BaseModel):
    id = AutoField()
    title = CharField(max_length=100)
    status = CharField(max_length=500)
    lastUpdate = DateTimeField(default=datetime.datetime.now)


def connectDb():
    global db
    db.connect()
    db.create_tables([Todo])


def add(InputTodo):
    todo = Todo.create(title=InputTodo.title, status=InputTodo.status)
    db.commit()
    return ShowTodo(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))


def update(id, InputTodo):
    todo = Todo.select().where(Todo.id == id).get()
    todo.title = InputTodo.title
    todo.status = InputTodo.status
    todo.lastUpdate = datetime.datetime.now()
    todo.save()
    db.commit()
    return ShowTodo(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))


def commitData():
    db.commit()


def delete(id):
    todo = Todo.delete().where(Todo.id == id).execute()


def get():
    todos = Todo.select()
    todoList = []
    for i in todos:
        todoList.append(ShowTodo(id=i.id, title=i.title, status=i.status, lastUpdate=(
            i.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S")))
    return todoList


def getID(id):
    todo = Todo.select().where(Todo.id == id).get()
    return ShowTodo(id=todo.id, title=todo.title, status=todo.status, lastUpdate=(todo.lastUpdate).strftime("%d/%m/%Y, %H:%M:%S"))
