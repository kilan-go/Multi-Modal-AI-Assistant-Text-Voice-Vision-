from transformers import pipeline
from utils.device import get_device

device = 0 if get_device() == "cuda" else -1

def load_text_model():
    return pipeline("text-generation", model="gpt2", device=device)