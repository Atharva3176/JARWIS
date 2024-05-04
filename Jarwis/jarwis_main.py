import pyttsx3
import speech_recognition
#from google.cloud import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest

for i in range(3):
    a = input("Enter password to open jarwis: ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("WELCOME SIR ! please speak wake up to load me up")
        break
    elif i == 2 and a != pw:
        exit()
    
    elif a!=pw:
        print("Try Again")

from intro import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening .......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-IN')
        print(f"You Said : {query}\n")
    except Exception as e:
        print(e)
        print("Please Say That Again")
        return "None"
    return query

def alarm(query):
    timehere = open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.system("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir , You can call me anytime")
                    break

                elif "change password" in query:
                    speak("What is the new password? ")
                    new = input("enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new)
                    new_password.close()
                    speak("Done Sir")
                    speak(f"Your New Password is {new}")

                elif "schedule my day" in query:
                    tasks = [] # empty list
                    speak("Do You want to clear old tasks (pls speak yes or no)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","r")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks : "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the number of tasks : "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.wav")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "translate" in query:
                    from traslater import translategl
                    query = query.replace("jarwis","")
                    query = query.replace("translate","")
                    translategl(query)


                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarwis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576        # 1MB = 1024*1024 bytes
                    download_net = wifi.download()/1048576
                    print("wifi download speed is",download_net)
                    print("wifi upload speed is",upload_net)
                    speak(f"wifi download speed is {download_net}")
                    speak(f"wifi upload speed is {upload_net}")

                elif "ipl score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soap = BeautifulSoup(page.text,"html.parser")
                    team1 = soap.find_all(class_ = "cb-col-50 cb-ovr-flo cb-hmscg-tm-name")[0].get_text()
                    team2 = soap.find_all(class_ = "cb-col-50 cb-ovr-flo cb-hmscg-tm-name")[1].get_text()
                    team1_score = soap.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soap.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE : ",
                        message  = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 10
                    )

                elif "play the game" in query:
                    from game import gameplay
                    gameplay()

                elif "screenshot" in query:
                    import pyautogui 
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile please")
                    pyautogui.press("enter")




                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("That's great Sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("You are welcome sir")

                elif "tired" in query:
                    speak("Playing Your Favourite Songs, Sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    print(b)
                    if b == 1:
                        webbrowser.open("https://youtu.be/B_6d3RBiEN0?si=MRN00oXcvJjKrFZq")
                    
                    elif b == 2:
                        webbrowser.open("https://youtu.be/r6SbfF9FjTg?si=n4fIyl8_GDjE6CES")

                    else :
                        webbrowser.open("https://youtu.be/535ZYgr5BeM?si=ZI0IY8RvZ_XoqTQF")
                        

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")


                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning Volume Up Sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning Volume Down Sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from searchnow import searchwikipedia
                    searchwikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from calculatenumbers import Wolframalpha
                    from calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarwis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from whatsapp import sendmessage
                    sendmessage()


                elif "temperature" in query:
                    search = "temperature in aurangabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "temperature in aurangabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")

                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    speak("done sir")
                    alarm(a)
                    

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep sir")
                    exit()

                elif "remember that" in query:
                    rememberMesssage = query.replace("remember that","")
                    rememberMesssage = query.replace("jarwis","")
                    speak("You Told me" + rememberMesssage)
                    remember = open("remember.txt","w")
                    remember.write(rememberMesssage)
                    remember.close()

                elif "what you remember" in query:
                    remember = open("remember.txt","r")
                    speak("You told me" + remember.read())

                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown the system")
                    shutdown = input("Do you want to shutdown the computer ? ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

