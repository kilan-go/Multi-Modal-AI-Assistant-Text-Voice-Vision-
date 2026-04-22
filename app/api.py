from fastapi import FastAPI
from brain.assistant import think
from vision import detection
from brain.memory import add_to_memory

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Assistant Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(question: str):
    if "see" in question.lower() or "what do you see" in question.lower():
        objects = detection.detect_objects()
        response = f"I see: {', '.join(objects)}"
    else:
        response = think(question)

    add_to_memory(question, response)
    return {"response": response}