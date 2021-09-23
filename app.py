from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends
from CRUD.model import *
from CRUD.database import *
app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_gen(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.get("/")
def getAPI(token: str = Depends(oauth_scheme)):
    return get()


@app.get("/api/{id}")
def getIDAPI(id: int, token: str = Depends(oauth_scheme)):
    return getID(id)


@app.post("/api")
def addAPI(todo: InputTodo, token: str = Depends(oauth_scheme)):
    return add(todo)


@app.put("/api/{id}")
def updateAPI(id: int, todo: InputTodo, token: str = Depends(oauth_scheme)):
    return update(id, todo)


@app.delete("/api/{id}")
def deleteAPI(id: int, token: str = Depends(oauth_scheme)):
    todo = getID(id)
    delete(id)
    return todo


@app.on_event("startup")
async def startup_event():
    connectDb()
