import pyttsx3

import speech_recognition as sr 
import datetime
import pyaudio
import wikipedia
import sys
import os

import smtplib

import webbrowser

#import pyautogui 
import psutil

import requests

from bs4 import BeautifulSoup

from youtube_search import YoutubeSearch


# to make speak function


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


# to make battery percentage

battery = psutil.sensors_battery()

current_battery = battery.percent


def speak(text):

    engine.say(text)

    engine.runAndWait()



def takeCammand():


    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("listening....")
        audio = r.listen(source, timeout=None, phrase_time_limit=None)

    try:

        print("recognizing....")

        query = r.recognize_google(audio, language='en-in')

        print(f" user said that {query}")


    except Exception as e:

        speak("say that again please")

        return 'none'


    return query


def wishMe():

    hour= int(datetime.datetime.now().hour)


    if hour >=0 and hour <12:

        speak(f"good mmorning sir and the current timing is {hour} AM")


    elif hour >=12 and hour <18:

        speak(f"good after noon sir the current timing is {hour} AM")


    elif hour >=18 and hour <22:

        speak(f"good evening sir and the current timing is {hour} PM")


    else:

        speak(f"it is time to sleep sir and the current timing is {hour} PM")




wishMe()



def BEST_START():

    query = takeCammand().lower()




    if 'wake up jarvis' in query or 'jarvis' in query or "let's go jarvis" in query:

        speak("i am ready sir ")


        hour = int(datetime.datetime.now().hour)

            # time = int(datetime.datetime().now().time)

                #speak("time")


        if hour >=0 and hour <12:

            speak(f"good morning sir, i am ready, system power is {current_battery} pecent and current time is {hour}")
        


        elif hour >=12 and hour <18:

            speak(f"good after noon sir i am ready  and system power is {current_battery} pecent and current time is {hour}")
        


        elif hour >=18 and hour <22:

            speak(f"good evening sir i am ready and system power is {current_battery} pecent and current time is {hour}")
        

        else:

            speak(f"it is time to sleep sir and current time is {hour}")

            speak("do you want to work")



    while True:


        query = takeCammand().lower()
     

    # _____________________________________hello function_______________________________________________________

        if 'hello' in query:

            speak("hello sir i am ready to your camaand")


    #______________________________________volume control_______________________________________________________

    #__________volumer up ________________


        elif 'volume up' in query:

            pyautogui.press("volume up")


    # __________volume down______________


        elif 'volume down' in query:

            pyautogui.press("volume down")


    #_____________volume mute____________


        elif 'mute' in query:

            pyautogui.press("volume mute")


    #____________________________________________________Wikipedia____________________________________________________


        elif 'wikipedia' in query:

            speak("searching wikipedia sir......")

            query = query.replace("wikkipedia", "")

            result = wikipedia.summary(query, sentences=2)
            print(result)

            speak(result)


    #_________________________________________________opening youtube_________________________________________________


        elif 'open youtube' in query:

            speak("opening youtube sir please wait.....")

            webbrowser.open("https://www.youtube.com/")


    #_________________________________________________music on youtube__________________________________________________


        elif 'play music on youtube' in query:

            speak("playing song on youtube sir please wait.........")

            webbrowser.open("https://www.youtube.com/results?search_query=brown+munde")


    #_______________________________when i dont have work my jarvis should sleep_____________________________________       

        elif ' you can sleep now' in query or 'shut up' in query:

            speak("sir i am going to sleep do you have any other task")

            query = takeCammand().lower()

            if 'yes' in query or 'i have task for you' in query:

                speak("ok sir i am with you sir")

            else:

                sys.exit()


    #_________________________________________________weather report________________________________________________


        elif 'temperature' in query:

            speak("tell me the place sir")

            search = takeCammand().lower()

            if 'place' in query:

                url = f"https://www.google.com/search?q={search}"

                r = requests.get(url)

                data = BeautifulSoup(r.text,"html.parser")

                temp = data.find("div",class_="BNeawe").text


            else:

                continue


    #___________________________________________________system exit function____________________________________________


        elif 'you can sleep now' in query or 'shut up' in query:

            speak("sir i am going to sleep do you have any other work for me")
            

            query = takeCammand().lower()


            if 'no' in query:

                speak("ok good day sir i am going to sleep")

                sys.exit()

            else:

                continue

            print(temp)




BEST_START()


    
        



