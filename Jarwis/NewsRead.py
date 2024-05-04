import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    apidict = {"buisness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=974fbf643aaf4b21a54a91a7f62c7b09",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=974fbf643aaf4b21a54a91a7f62c7b09",
               "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=974fbf643aaf4b21a54a91a7f62c7b09",
               "science" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=974fbf643aaf4b21a54a91a7f62c7b09",
               "sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=974fbf643aaf4b21a54a91a7f62c7b09",
               "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=974fbf643aaf4b21a54a91a7f62c7b09"}
    

    content = None
    url = None

    speak("Which Field news do you want, [buisness] , [entertainment] , [health] , [science] , [sports] , [technology]")
    field = input("Type the Field of the news that you want: ")
    for key , value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found ")
            break
        else :
            url = True
    if url is True:
                print("Url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info use news url: {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]")
        if str(a) == "1":
            pass

        elif str(a) == "2": 
            break

    speak("That's All")