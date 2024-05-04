import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarwis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")
    alarmtime = str(timenow)
    print(alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == alarmtime:
            speak("Alarm ringing sir")
            os.startfile("arambh.mp3")

        elif currenttime + "00:00:30" == alarmtime:
            exit()

ring(time)