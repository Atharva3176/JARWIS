import pyttsx3
import speech_recognition 
import random


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

def gameplay():
    speak("Let's play")
    print("play the rock paper scisssor game")
    i = 0
    my_score = 0
    com_score = 0

    while(i<5):
        choose = ("rock", "paper", "scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if query == "rock":
            if com_choose == "rock":
                speak("rock")
                print(f"Score : Me : {my_score} : Com : {com_score}")
            elif com_choose == "paper":
                speak("paper")
                com_score += 1
                print(f"Score : Me : {my_score} : Com : {com_score}")

            else:
                speak("Scissor")
                my_score +=1
                print(f"Score : Me : {my_score} : Com : {com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                my_score += 1
                print(f"Score:- ME :- {my_score+1} : COM :- {com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {my_score} : COM :- {com_score}")
            else:
                speak("Scissors")
                com_score += 1
                print(f"Score:- ME :- {my_score} : COM :- {com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                com_score += 1
                print(f"Score:- ME :- {my_score} : COM :- {com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                my_score += 1
                print(f"Score:- ME :- {my_score} : COM :- {com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {my_score} : COM :- {com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {my_score} : COM :- {com_score}")


