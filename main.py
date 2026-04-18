from speech.speech_to_text import listen
from speech.text_to_speech import speak
from brain.assistant import think
from vision.camera import capture_image

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