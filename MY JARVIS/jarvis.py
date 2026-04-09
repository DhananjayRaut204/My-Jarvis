import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
from reportlab.pdfgen import canvas


engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
 engine.say(text) 
 engine.runAndWait()

def take_command():
 r = sr.Recognizer() 
 with sr.Microphone() as source: 
    speak("Listening") 
    audio = r.listen(source)
    try: 
        command = r.recognize_google(audio) 
        return command.lower()
    except:
        return ""
    
while True:
 command = take_command()
 if "open youtube" in command:
     speak("Opening YouTube")
     pywhatkit.playonyt("youtube")
 elif "open google" in command:
     speak("Opening Google")
     os.system("start chrome")
 elif "make pdf" in command:
     c = canvas.Canvas("jarvis_created.pdf")
     c.drawString(100, 750, "PDF created by Jarvis")
     c.save()
     speak("PDF created successfully")
 elif "stop jarvis" in command:
     speak("Goodbye")
     break
