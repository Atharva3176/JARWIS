import wolframalpha
import pyttsx3
#import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wolframalpha(query):
    #PRR4JW-4V6AWX5YHX
    apikey = "PRR4JW-4V6AWX5YHX"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarwis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("plus","+")

    Final = str(Term)
    try :
        result = Wolframalpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")


