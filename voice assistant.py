import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        process_query(query)
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError:
        print("Sorry, I'm currently unavailable.")

def process_query(query):
    if "hello" in query:
        speak("hello Boss,How can I assist you?")
    
    elif "time" in query:
        current_time = datetime.now().strftime("")
        speak(f"The current time is {current_time}.")
   
    elif"open Youtube" in query:
        open_youtube()
        exit()
    elif "thanks" in query:
        speak("your welcome ")
        exit()
    else:
        speak("Sorry, I cannot help with that.")


def open_youtube():
  browser = webbrowser.get()
  browser.open("https://www.youtube.com/")

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

while True:
    listen()
  
