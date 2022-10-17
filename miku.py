import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import numpy as np
import random
import pyjokes
import wolframalpha
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from chat import *
from facerecognition import *
from serial_esp32 import *
from masker import *
# from arduino_tools import *


print ("initializing Hikaru Kaito")

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

#chatbot AI
def chatbot(inp):
    results = model.predict([bag_of_words(inp, words)])
    results_index = np.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg["tag"] == tag:
            responses = tg["responses"]

    out = random.choice(responses)
    print(out)
    speak(out)

#main start here
if __name__ == "__main__":
    face_recognition(1)
    wishMe()
    speak("I am ready master" + MASTER)
    speak("Hello my name is Hikaru Kaito, Can I help you master?")

    #logic for tasks as command
    while True:
        query = takeCommand()
        INTRO = ["please introduce you","who are you"]
        if query.lower() in INTRO:
            speak("My name is Hikaru Kaito. I am the beta version of Miku Project. I was created in 2021 and my creator is named Ilyas Hidayat Rusdy. nice to meet you.")
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
        #pause and resume youtube if it is playing
        elif "pause youtube" in query.lower():
            speak("Ok master, pausing youtube...")
            pywhatkit.pauseonyt()
        elif "resume youtube" in query.lower():
            speak("Ok master, resuming youtube...")
            pywhatkit.resumeonyt()
        elif "time" in query.lower():
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            speak("time now is" + time)
        elif "open whatsapp" in query.lower():
            speak("Ok, master")
            url = "web.whatsapp.com"
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
        elif "google meet" in query.lower() or "meet" in query.lower():
            speak("Ok, master")
            url = "meet.google.com"
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
        elif "open mail" in query.lower() or "gmail" in query.lower():
            speak("Ok, master")
            url = "mail.google.com"
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
        elif "open drive" in query.lower() or "google drive" in query.lower():
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
            masker()
        elif "play music" in query.lower() or "play song" in query.lower():
            speak("Ok, master")
            songs_dir = "C:\\Users\\Ilyas Hidayat Rusdy\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
        #close music if it is playing
        elif "stop music" in query.lower() or "close music" in query.lower():
            speak("Ok, master")
            os.system("pkill -9 mplayer")
        #next song if it is playing
        elif "next song" in query.lower() or "next music" in query.lower():
            speak("Ok, master")
            os.system("mpc next")
        #open microsoft office word
        elif "open microsoft word" in query.lower() or "open word" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.EXE")
        #close microsoft office word if it is open
        elif "close microsoft word" in query.lower() or "close word" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im WINWORD.EXE")
        #open microsoft office excel
        elif "open microsoft excel" in query.lower() or "open excel" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE")
        #close microsoft office excel if it is open
        elif "close microsoft excel" in query.lower() or "close excel" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im EXCEL.EXE")
        #open microsoft office powerpoint
        elif "open microsoft powerpoint" in query.lower() or "open powerpoint" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.EXE")
        #close microsoft office powerpoint if it is open
        elif "close microsoft powerpoint" in query.lower() or "close powerpoint" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im POWERPNT.EXE")
        #open file explorer
        elif "open explorer" in query.lower() or "open file explorer" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Users\\Ilyas Hidayat Rusdy\\Desktop\\")
        #close file explorer if it is open
        elif "close explorer" in query.lower() or "close file explorer" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im explorer.exe")
        #open cmd
        elif "open cmd" in query.lower() or "open command prompt" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Windows\\System32\\cmd.exe")
        #close cmd if it is open
        elif "close cmd" in query.lower() or "close command prompt" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im cmd.exe")
        #open facebook
        elif "open facebook" in query.lower() or "facebook" in query.lower():
            speak("Ok, master, please ferify your face")
            face_recognition(1)
            # if id == "open":
            speak("Welcome back, master")
            #open facebook dan masukkan username dan password dengan selenium
            driver = webdriver.Chrome()
            driver.get("https://www.facebook.com/")
            username = driver.find_element_by_id("email")
            username.send_keys("ilyashidayatrusdy@yahoo.com")
            password = driver.find_element_by_id("pass")
            password.send_keys("16081999")
            password.send_keys(Keys.RETURN)
            # else:
            #     speak("Sorry, you are not master")
        #close facebook if it is open
        elif "close facebook" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im chrome.exe")
        #open instagram
        elif "open instagram" in query.lower() or "instagram" in query.lower():
            speak("Ok, master, please ferify your face")
            face_recognition(1)
            # if id == "open":
            speak("Welcome back, master")
            #open instagram dan masukkan username dan password dengan selenium
            driver = webdriver.Chrome()
            driver.get("https://www.instagram.com/")
            username = driver.find_element_by_name("username")
            username.send_keys("ilyashidayatrusdy@yahoo.com")
            password = driver.find_element_by_name("password")
            password.send_keys("Il16081999")
            password.send_keys(Keys.RETURN)
            # else:
            #     speak("Sorry, you are not master")
        #close instagram if it is open
        elif "close instagram" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im chrome.exe")
        #open notepad
        elif "open notepad" in query.lower() or "open text editor" in query.lower():
            speak("Ok, master")
            os.startfile("C:\\Windows\\System32\\notepad.exe")
        #make a note
        elif "make a note" in query.lower() or "make note" in query.lower():
            speak("Ok, master, what should i write?")
            note = takeCommand()
            file = open("note/note.txt", "w")
            speak("Should i include date and time?")
            snfm = takeCommand()
            if "yes" in snfm or "sure" in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        #read a note
        elif "read note" in query.lower() or "read my note" in query.lower():
            speak("Ok, master")
            file = open("note/note.txt", "r")
            print(file.read())
            speak(file.read(6))
        #set an alarm
        elif "set alarm" in query.lower() or "set an alarm" in query.lower():
            speak("Ok, master, at what time should i set the alarm?")
            alarm = takeCommand()
            speak("What should i say when the alarm rings?")
            alarmMessage = takeCommand()
            speak("Alarm is set for " + alarm)
            alarmHour = alarm.split(":")[0]
            alarmMinute = alarm.split(":")[1]
            while True:
                if alarmHour == datetime.datetime.now().strftime("%H") and alarmMinute == datetime.datetime.now().strftime("%M"):
                    print("Alarm is ringing")
                    speak(alarmMessage)
                    break
        #calculate
        elif "calculate" in query.lower() or "calculate something" in query.lower():
            speak("Ok, master, what should i calculate?")
            calc = takeCommand()
            app_id = "3R9RKJ-5EUG6R6K33"
            client = wolframalpha.Client(app_id)
            res = client.query(calc)
            answer = next(res.results).text
            print(answer)
            speak(answer)
        #open lock door selenoid
        elif "open lock door" in query.lower() or "open door" in query.lower():
            speak("Ok, master, Identifying your face...")
            face_recognition1(2)
            # if id == "open":
            speak("Ok, master, opening the door")
            Operation(3)
            time.sleep(5)
            Operation(4)
            # else:
            #     speak("Sorry, Your face is not allowed to open the door")
        #on lampu
        elif "on the lamp" in query.lower() or "on" in query.lower():
            speak("Ok, master")
            Operation(1)
            speak("Lamp is on")
        #off lampu
        elif "off the lamp" in query.lower() or "off" in query.lower():
            speak("Ok, master")
            Operation(2)
            speak("Lamp is off")
        #give a joke
        elif "tell me a joke" in query.lower() or "joke" in query.lower():
            speak("Ok, master")
            joke = pyjokes.get_joke()
            speak(joke)
        #close aplication
        elif "close" in query.lower() or "exit" in query.lower():
            speak("Ok, master")
            exit()
        #chat with Kaito
        elif "hikaru" in query.lower() or "kaito" in query.lower():
            chatbot(query)
        else:
            speak("sorry master, your order is not including my program")
