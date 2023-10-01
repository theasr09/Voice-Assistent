import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
from googlesearch import search
import webbrowser
import os
import smtplib
import time

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.getProperty("rate")
engine.setProperty("rate",150)


# this function will speak  what we provide to this function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# this function will give us the greatings
def wishes():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning Sir i am jack ")
        print("good morning Sir i am jack ")
    elif hour>12 and hour<16:
        speak("good afternoon Sir i am jack ")
        print("good afternoon Sir i am jack ")
    else:
        speak("good evening Sir i am jack ")
        print("good evening Sir i am jack ")

    speak("how may i help you  ")
    print("how may i help you  ")

# this function is take the audio what we said and convert that into string 
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recongnizing ....")
        query=r.recognize_google(audio,language="en-in")
        print("user said :",query)
    except Exception as e:
        print("say that again")
        return "None"

    return query


if __name__=="__main__":
    wishes()

    while True:
        query=take_command().lower()



            # searching on the wikipedia

        if "wikipedia" in query:
            speak("searching Wikipedia")
            print("seraching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif " who are you" in query:
            speak("my name is jack , i am a AI model and my inveter is MR. Your name")

        elif "How are you" in query:
            speak("I am fine, what about you")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
                music_dir = 'Paste your music directory here'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%I:%M %p")
            print(strtime)
            speak(strtime)

        elif "open vs code" in query:
            codePath="paste your vscode target here"
            os.startfile(codePath)

        elif "quit" in query:
            speak("Thank you and come again")
            print("Thank you and come again")
            break

        time.sleep(5)

