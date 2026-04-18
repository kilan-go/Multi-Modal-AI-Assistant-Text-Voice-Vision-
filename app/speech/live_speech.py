import sounddevice as sd
import numpy as np
import whisper

model = whisper.load_model("base")

def listen_live(duration=5, fs=16000):
    print("Listening...")
    
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    audio = np.squeeze(audio)
    
    result = model.transcribe(audio)
    return result["text"]