#from time import sleep
from googletrans import Translator
import googletrans
import pygame
from gtts import gTTS
import pyttsx3
import speech_recognition
import os
#from playsound import playsound
import time

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


def translategl(query):
    speak("sure sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language you want to translate")
    b = input("To Language : ")
    translator = Translator(service_urls=['translate.googleapis.com'])
    text_to_translate = translator.translate(query,src="auto",dest=b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        pygame.mixer.init()  # Initialize pygame mixer
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for playback to finish
            time.sleep(1)

        pygame.mixer.quit()  # Quit pygame mixer

        # Remove the audio file (check if it exists first)
        if os.path.exists("voice.mp3"):
            os.remove("voice.mp3")
    except:
        print("Unable to translate")


