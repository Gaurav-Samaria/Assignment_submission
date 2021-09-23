from .model import todo

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoDatabase
collection = database.todo


async def fetch_by_id(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result

async def update(title, desc):
    await collection.update_one({"title":title},{"$set":{
        "description":desc
        }})
    document = await collection.find_one({"title":title})
    return document

async def delete(title):
    await collection.delete_one({"title":title})
    return True
