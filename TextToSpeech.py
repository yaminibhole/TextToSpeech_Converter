import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak("Welcome to RoboSpeaker. How can I help you?")
    while True:
        user_input = input("Enter what you want me to speak (type 'q' to quit): ")

        if user_input.lower() == "q":
            speak("Bye Bye")
            break

        speak(user_input)
