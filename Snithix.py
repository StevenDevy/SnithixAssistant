from sys import path
import pyttsx3
import datetime
import speech_recognition as sr
import time
import os
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		speak("Listening....")
		r.pause_threshold = 1
		audio = r.listen(source,timeout = 10,phrase_time_limit=8)

	try:
		print("Recognizing....")
		query = r.recognize_google(audio, language='en-in')
		print(f"User Said : {query}")

	except Exception as e:
		speak("Can you repeat that please?")
		return "none"
	return query

def wish():
	hour = int(datetime.datetime.now().hour)
	tt = time.strftime("%I" + " %M" + " %p")

	if hour>=0 and hour<=12:
		speak("Good Morning,It is " + tt)
	elif hour>12 and hour<18:
		speak("Good Afternoon,It is " + tt)
	else:
		speak("Good Evening,It is " + tt)

if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Opened Notepad")

        elif "hello" in query:
            speak("Hello sir")

        elif "bye" in query or "stop" in query:
            speak("GoodBye sir")
            quit()

        elif "open youtube" in query:
            speak('Opened Youtube')
            webbrowser.open("youtube.com")

        elif 'code' in query:
            codePath = "Paste your vscode path"
            os.startfile(codePath)
            speak("Opeded Visual studio code")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif "google" in query:
            speak('Opened google')
            webbrowser.open("google.com")
        elif "github" in query:
            speak('Opened Github')
            webbrowser.open("https://github.com")
        if "unity" in query:
            speak('Opened Unity')
            webbrowser.open("Paste your unity path")

        if "android studio" in query:
            speak('Opened Android Studio. Your current project will be opened.')
            os.startfile("paste your android studio path")
