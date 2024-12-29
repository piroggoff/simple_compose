from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from data_methods import User, verify_logindata
from logger_hand import logger


app = FastAPI()


@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/numbers/{number}")
async def read_root(number: int):
    return number

@app.post("/login")
async def login_in(userdata: User):
    if verify_logindata(userdata):
        return {"message": "Login successed", "data":userdata}
    return {"message":"Wrong credentials", "code":404}

@app.get("/health")
async def health_check():
    return Response(status_code=200)