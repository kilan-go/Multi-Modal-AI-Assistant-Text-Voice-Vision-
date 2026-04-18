from app.speech.speech_to_text import listen
from app.speech.text_to_speech import speak
from app.brain.assistant import think
from app.vision.camera import capture_image

def main():
    while True:
        user_input = listen()
        
        if "see" in user_input.lower():
            img = capture_image()
            response = f"I captured an image: {img}"
        else:
            response = think(user_input)
        
        speak(response)

if __name__ == "__main__":
    main()