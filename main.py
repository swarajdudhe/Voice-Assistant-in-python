
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try :
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understanding")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

  #  if sptext().lower() == "hey lisa" :

        while True:
            data1 = sptext().lower()

            if "hello" in data1:
                hello = "Hello dear, How can i help you?"
                speechtx(hello)

            if "your name" in data1:
                name = "my name is lisa"
                speechtx(name)

            elif "old are you" in data1:
                age = "i am 2 days old"
                speechtx(age)

            elif "current time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif "youtube" in data1:
                webbrowser.open('https://www.youtube.com/')

            elif "wikipedia" in data1:
                webbrowser.open('https://www.wikipedia.org/')

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)


            elif "play song" in data1:
                add = "D:/programming/machine_learning/voice_assistant_in_python/songs"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[1]))

            elif "exit" in data1:
                speechtx("thank you ")
                break

            elif "sleep" in data1:
                speechtx("thank you ")
                break

            time.sleep(5)

































