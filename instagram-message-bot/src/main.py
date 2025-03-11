from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user: str
    text: str

@app.post("/process-message/")
async def process_message(message: Message):
    response_message = f"Processed message: {message.text}"
    return {"response": response_message}

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}