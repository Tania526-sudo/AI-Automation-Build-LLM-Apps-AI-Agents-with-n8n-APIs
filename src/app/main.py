from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    prompt: str

@app.post("/process")
def process(data: InputData):
    return {"response": f"Processed: {data.prompt}"}