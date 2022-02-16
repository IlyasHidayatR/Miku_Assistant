import pyttsx3 #pip install di terminal
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import smtplib

print ("initializing Kaito")

MASTER = "ilyas"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning master" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Aternoon master" + MASTER)
    else:
        speak("Good Evening master" + MASTER)
        speak("")

#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognition...")
            query = r.recognize_google(audio, language="en-us")
            print(f"user said: {query}\n")

        except Exception as e:
            print("say that again please")
            speak("say that again please")
            query = None
    return query

#main start here
wishMe()
speak("Hello my name is Kaito, Can I help you master?")
query = takeCommand()

#logic for tasks as command
INTRO = ["please introduce you","who are you"]
if query.lower() in INTRO:
    speak("My name is Kaito. I am the beta version of Miku. I was created in 2021 and my creator is named Ilyas Hidayat Rusdy. nice to meet you.")
elif "wikipedia" in query.lower():
    speak("ok master, searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif "open youtube" in query.lower():
    speak("Ok, master")
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "google" in query.lower():
    speak("Ok master, searching google...")
    pywhatkit.search(query.replace("google", ""))
elif "youtube" in query.lower():
    speak("Ok master, searching youtube...")
    pywhatkit.playonyt(query.replace("youtube", ""))
elif "time" in query.lower():
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    speak("time now is" + time)
elif "open whatsapp" in query.lower():
    speak("Ok, master")
    url = "web.whatsapp.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "google meet" in query.lower():
    speak("Ok, master")
    url = "meet.google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "open mail" in query.lower():
    speak("Ok, master")
    url = "mail.google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "open drive" in query.lower():
    speak("Ok, master")
    url = "drive.google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "open google" in query.lower():
    speak("Ok, master")
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "mask face" in query.lower():
    speak("Ok, master")
    os.system("python masker.py")
elif "play music" in query.lower():
    speak("Ok, master")
    songs_dir = "C:\\Users\\Ilyas Hidayat Rusdy\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
#open microsoft office word
elif "open word" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.EXE")
#open microsoft office excel
elif "open excel" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE")
#open microsoft office powerpoint
elif "open powerpoint" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.EXE")
#open file explorer
elif "open explorer" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Users\\Ilyas Hidayat Rusdy\\Desktop\\")
#open cmd
elif "open cmd" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Windows\\System32\\cmd.exe")
#open notepad
elif "open notepad" in query.lower():
    speak("Ok, master")
    os.startfile("C:\\Windows\\System32\\notepad.exe")
#close aplication
elif "close" in query.lower():
    speak("Ok, master")
    exit()
else:
    speak("sorry master, your order is not including my program")
