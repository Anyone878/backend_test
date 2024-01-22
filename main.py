from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/plus_one/{number}")
def plus_one(number: int):
    return {"message": number + 1}

@app.post("/send_back_to_me")
def send_back(data: str):
    return data
