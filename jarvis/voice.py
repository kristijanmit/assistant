import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init()

def hear(retries=3):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    attempt = 0
    while attempt < retries:
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError as e:
            attempt += 1
            print(f"Could not request result; {e}. Retrying {attempt}/{retries}...")
            time.sleep(2)
    
    print("Failed to reach the server after multiple attempts.")
    return None

def speak(text):
    engine.say(text)
    engine.runAndWait()
