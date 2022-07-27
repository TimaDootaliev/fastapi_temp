from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tasks.tasks import add
from tasks.tasks import divide

app = FastAPI(debug=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/add/{x}/{y}")
def add_numbers(x: int, y: int):
    return {"result": add.delay(x, y).get()}


@app.get("/divide/{x}/{y}")
def divide_numbers(x: int, y: int):
    return {"result": divide.delay(x, y).get()}
