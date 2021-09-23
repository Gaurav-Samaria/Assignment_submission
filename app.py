from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException
from CRUD.model import *
from CRUD.database import *
app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_gen(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}


@app.get("/")
async def readAPI(token: str = Depends(oauth_scheme)):
    response = await fetch_all()
    return response


@app.get("/api/{title}", response_model = todo)
async def readIDAPI(title, token: str = Depends(oauth_scheme)):
    response = await fetch_by_id(title)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")


@app.post("/api", response_model=todo)
async def addAPI(todo:todo, token: str = Depends(oauth_scheme)):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@app.put("/api/{title}", response_model=todo)
async def updateAPI(title: str, desc:str, token: str = Depends(oauth_scheme)):
    response = await update(title,desc)
    if response:
        return response
    raise HTTPException(404, f"there is no todo item with title {title}")


@app.delete("/api/{title}")
async def deleteAPI(title, token: str = Depends(oauth_scheme)):
    response=await delete(title)
    if response:
        return "Succesfully deleted todo Item"
    raise HTTPException(404, f"there is no todo item with title {title}")