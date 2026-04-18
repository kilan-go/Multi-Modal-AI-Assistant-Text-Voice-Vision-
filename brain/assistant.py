from transformers import pipeline
from brain.memory import get_context

chatbot = pipeline("text-generation", model="gpt2")

def think(prompt):
    context = get_context()
    full_prompt = context + "\nUser: " + prompt + "\nAI:"
    
    response = chatbot(full_prompt, max_length=150)
    return response[0]['generated_text']