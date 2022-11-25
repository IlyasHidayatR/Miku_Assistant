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
import pyautogui
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from chat import *
from facerecognition import *
from serial_esp32 import *
from masker import *
from recordface import *
from traningface import *
# from arduino_tools import *
from FaceRecognition import FaceRecognition


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
            return "None"
            
    query = query.lower()
    return query

# chatbot AI
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

def task():
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
        elif "open google" in query.lower():
            speak("Ok, master")
            url = "google.com"
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
        elif "mask face" in query.lower():
            speak("Ok, master")
            masker()
        elif "play music" in query.lower() or "play song" in query.lower():
            speak("Ok, master")
            songs_dir = "C:\\Users\\Ilyas Hidayat Rusdy\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))
        # hear music from youtube or local
        elif "hear music" in query.lower() or "hear a music" in query.lower():
            speak("Ok, master. Wheare do you want to hear music from? Youtube or local?")
            query = takeCommand()
            if "youtube" in query.lower():
                speak("Ok, master. What is the music name?")
                query = takeCommand()
                pywhatkit.playonyt(query)
            elif "local" in query.lower():
                speak("Ok, master. What is the music name?")
                query = takeCommand()
                songs_dir = "C:\\Users\\Ilyas Hidayat Rusdy\\Music"
                songs = os.listdir(songs_dir)
                print(songs)
                os.startfile(os.path.join(songs_dir, query))
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
        #open app in windows
        elif "open app" in query.lower() or "open application" in query.lower():
            speak("Ok, master. What app do you want to open?")
            app = takeCommand()
            #search app at search bar in windows and open it
            pyautogui.hotkey("win", "s")
            pyautogui.write(app)
            #choose the first app in the list
            pyautogui.press("enter")
        #close app in windows
        elif "close app" in query.lower() or "close application" in query.lower():
            speak("Ok, master. What app do you want to close?")
            app = takeCommand()
            #search app at search bar in windows and close it
            pyautogui.hotkey("win", "s")
            pyautogui.write(app)
            pyautogui.press("enter")
            pyautogui.hotkey("alt", "f4")
        #screen shot
        elif "screen shot" in query.lower() or "screenshot" in query.lower():
            speak("Ok, master")
            #take screen shot
            img = pyautogui.screenshot()
            #save screen shot in picture folder
            img.save("C:\\Users\\Ilyas Hidayat Rusdy\\Pictures\\screenshot.png")
        #volume up
        elif "volume up" in query.lower() or "increase volume" in query.lower():
            speak("Ok, master. How much do you want to increase the volume?")
            volume = takeCommand()
            #increase volume
            pyautogui.hotkey("volumeup", volume)
        #volume down
        elif "volume down" in query.lower() or "decrease volume" in query.lower():
            speak("Ok, master. How much do you want to decrease the volume?")
            volume = takeCommand()
            #decrease volume
            pyautogui.hotkey("volumedown", volume)
        #mute volume
        elif "mute volume" in query.lower() or "mute" in query.lower():
            speak("Ok, master")
            #mute volume
            pyautogui.hotkey("volumemute")
        #unmute volume
        elif "unmute volume" in query.lower() or "unmute" in query.lower():
            speak("Ok, master")
            #unmute volume
            pyautogui.hotkey("volumemute")
        #open facebook
        elif "open facebook" in query.lower() or "facebook" in query.lower():
            speak("Ok, master, please ferify your face")
            face_recognition(1)
            # if id == "open":
            speak("Welcome back, master")
            #open facebook dan masukkan username dan password dengan selenium
            driver = webdriver.Chrome(executable_path=r"C:\\chromedriver_win32\\chromedriver.exe")
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
            driver = webdriver.Chrome(executable_path=r"C:\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.instagram.com/")
            username = driver.find_element_by_name("username")
            username.send_keys("ilyashidayatrusdy@gmail.com")
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
        #close notepad if it is open
        elif "close notepad" in query.lower() or "close text editor" in query.lower():
            speak("Ok, master")
            os.system("taskkill /f /im notepad.exe")
        #regitraion face
        elif "registration face" in query.lower() or "register face" in query.lower():
            speak("Ok, master. Before you register new face, please ferify your face master")
            face_recognition(1)
            # if id == "open":
            speak("Welcome back, master. Please look at the camera and create new ID face")
            try:
                record_face()
                if valid == 1:
                    TrainingFace()
                    print("Face registration success. If you want the new face to be used, please add the new face ID and name in the variable recognize_ID at facerecognition.py and restart the program")
                    speak("Face registration success. If you want the new face to be used, please add the new face ID and name in the variable recognize_ID at facerecognition.py and restart the program")
                else:
                    print("Face registration failed")
                    speak("Face registration failed")
            except:
                print("Face registration failed")
                speak("Face registration failed")
            # else:
            #     speak("Sorry, you are not master")
        #make a note
        elif "make a note" in query.lower() or "make note" in query.lower():
            speak("Ok, master, what should i write?")
            note = takeCommand()
            if os.path.exists("note/note.txt"):
                with open("note/note.txt", "a") as f: #append
                    speak("Should i include date and time?") 
                    dt = takeCommand()
                    if "yes" in dt.lower() or "sure" in dt.lower():
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        f.write(strTime)
                        f.write(" :- ")
                        f.write(note)
                        speak("I have made a note")
                    else:
                        f.write(note)
                        speak("I have made a note")
            else:
                with open("note/note.txt", "w") as f:
                    speak("Should i include date and time?")
                    dt = takeCommand()
                    if "yes" in dt.lower() or "sure" in dt.lower():
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        f.write(strTime)
                        f.write(" :- ")
                        f.write(note)
                        speak("I have made a note")
                    else:
                        f.write(note)
                        speak("I have made a note")
        #read a note
        elif "read note" in query.lower() or "read my note" in query.lower():
            speak("Ok, master")
            file = open("note/note.txt", "r")
            # if note is empty
            if os.stat("note/note.txt").st_size == 0:
                speak("You have no note")
            else:
                note = file.read()
                speak(note)
                print(note)
        #set an alarm
        elif "set alarm" in query.lower() or "set an alarm" in query.lower():
            speak("Ok, master, at what time should i set the alarm?")
            alarm = takeCommand()
            speak("What should i say when the alarm rings?")
            alarmMessage = takeCommand()
            speak("Alarm is set for " + alarm)
            alarmHour = int(alarm.split(":")[0])
            alarmMinute = int(alarm.split(":")[1])
            #set alarm
            while True:
                if alarmHour == datetime.datetime.now().strftime("%H") and alarmMinute == datetime.datetime.now().strftime("%M"):
                    print("Alarm is ringing")
                    speak(alarmMessage)
                    break
        #set timer
        elif "set timer" in query.lower() or "set a timer" in query.lower():
            speak("Ok, master, for how many minutes should i set the timer?")
            timer = takeCommand()
            speak("Timer is set for " + timer + " minutes")
            timerMinute = int(timer)
            #set timer
            while True:
                if timerMinute == 0:
                    print("Timer is up")
                    speak("Timer is up")
                    break
                else:
                    timerMinute -= 1
                    time.sleep(60)
        #calculate
        elif "calculate" in query.lower() or "calculate something" in query.lower():
            speak("Ok, master, what should i calculate?")
            calc = takeCommand()
            app_id = "3R9RKJ-5EUG6R6K33"
            client = wolframalpha.Client(app_id)
            res = client.query(calc)
            answer = next(res.results).text
            print(answer)
            speak("The answer is " + answer)
        #open lock door selenoid
        elif "open the door" in query.lower() or "open door" in query.lower():
            speak("Ok, master, Identifying your face...")
            # FaceRecognition.face_recognition1(2)
            face_recognition1(2)
            # if id == "open":
            speak("Ok, master. Opening the door for 5 seconds")
            Operation(3)
            time.sleep(5)
            Operation(4)
            # else:
            #     speak("Sorry, You're not allowed to open the door")
        #on lampu
        elif "on the lamp" in query.lower() or "on the light" in query.lower():
            speak("Ok, master")
            Operation(1)
            speak("Lamp is on")
        #off lampu
        elif "off the lamp" in query.lower() or "off the light" in query.lower():
            speak("Ok, master")
            Operation(2)
            speak("Lamp is off")
        #give a joke
        elif "tell me a joke" in query.lower() or "joke" in query.lower():
            speak("Ok, master")
            joke = pyjokes.get_joke()
            speak(joke)
        #take a rest
        elif "take a rest" in query.lower() or "take rest" in query.lower():
            speak("Ok, master. If you need me, just call me")
            break
        #close aplication
        elif "close" in query.lower() or "exit" in query.lower():
            speak("Ok, master")
            exit()
        #Shutdown
        elif "shutdown" in query.lower() or "shut down" in query.lower():
            speak("Ok, master")
            os.system("shutdown /s /t 1")
        #Restart
        elif "restart" in query.lower() or "reboot" in query.lower():
            speak("Ok, master")
            os.system("shutdown /r /t 1")
        #Sleep
        elif "sleep" in query.lower() or "hibernate" in query.lower():
            speak("Ok, master")
            os.system("shutdown /h")
        #chat with Kaito
        elif "hikaru" in query.lower() or "kaito" in query.lower():
            chatbot(query)
        elif "none" in query.lower():
            speak("Sorry, i didn't get that")
        else:
            speak("sorry master, your order is not including my program")

def main():
    speak("Hello my name is Hikaru Kaito, a virtual assistant. Before we start, please verify your identity")
    # FaceRecognition.face_recognition(1)
    face_recognition(1)
    speak("Your identity has been verified")
    wishMe()
    speak("If you need my help, please call me master")
    # wakeWord("hey hikaru") #for testing wake word
    while True:
        query1 = takeCommand().lower()
        # wakeWord("hey hikaru") #for testing wake word
        if "hikaru" in query1 or "kaito" in query1:
            speak("I'm listening")
            task()
        elif "none" in query1:
            speak("Sorry, i didn't get that")
        else:
            speak("sorry master, I can't hear you call me")
    

if __name__ == "__main__":
    #run main function with screen_main
    screen_main = tk.Tk()
    screen_main.title("Kaito")
    screen_main.geometry("500x500")
    screen_main.configure(background="black")
    screen_main.resizable(False, False)
    #create a label
    tk.Label(screen_main, text="Hikaru Kaito", bg="black", fg="white", font=("Calibri", 30)).pack()
    tk.Label(screen_main, text="Your Personal Assistant", bg="black", fg="white", font=("Calibri", 15)).pack()
    tk.Label(screen_main, text="", bg="black").pack()
    #create a button
    tk.Button(screen_main, text="Start", width=10, height=1, command=main).pack()
    #start gif animation image
    openImage = Image.open("Kaito.gif")

    frame = openImage.n_frames
    animation = [tk.PhotoImage(file="Kaito.gif", format=f"gif -index {i}") for i in range(frame)]
    def update(ind):
        im2 = animation[ind]
        ind += 1
        label.configure(image=im2)
        if ind == frame:
            ind = 0
        screen_main.after(100, update, ind)
    label = tk.Label(screen_main, bg="black")
    label.pack()
    screen_main.after(0, update, 0)
    #start the mainloop
    screen_main.mainloop()
