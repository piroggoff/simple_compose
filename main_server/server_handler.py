from fastapi import FastAPI
from fastapi.responses import FileResponse
from data_methods import User, verify_logindata
from datetime import datetime


app = FastAPI()


@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/numbers/{number}")
async def read_root(number: int):
    return number

@app.post("/login")
async def login_in(data: User):
    if verify_logindata(data.name, data.password):
        return {"message": "Login successed", "data":data}
    return {"message":"Wrong credentials", "code":404}
