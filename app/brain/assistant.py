from transformers import pipeline
from brain.memory import get_context

chatbot = pipeline("text-generation", model="gpt2")

def think(prompt):
    context = get_context()
    full_prompt = context + "\nUser: " + prompt + "\nAI:"

    result = chatbot(full_prompt, max_length=150, num_return_sequences=1)
    return result[0]["generated_text"]