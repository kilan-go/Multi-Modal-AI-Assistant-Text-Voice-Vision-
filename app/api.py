from fastapi import FastAPI
from app.brain.assistant import think

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Assistant Running"}

@app.post("/ask")
def ask(question: str):
    if "what do you see" in question.lower():
        objects = detect_objects()
        return {"response": f"I see: {', '.join(objects)}"}
    
    response = think(question)
    return {"response": response}