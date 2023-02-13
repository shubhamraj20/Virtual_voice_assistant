import pyttsx3
import datetime
import wikipedia
import webbrowser
import os 
import speech_recognition as sr
  

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning sir: ")
    elif hour>=12 and hour <17:
        speak("Good afternoon sir: ")
    elif hour>=17 and hour <19:
        speak("Good evening sir: ")
    elif hour>=17 and hour <23:
        speak("Good evening sir: ")
    speak("Hello sir i am your voice assistant how may i help you")

def takeCommand():
    ''' It takes microphone input from the user and returns string as command'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print("User said :- ", query)
    except Exception as e:
        print("Say that again.....")
        return "None"

    return query


    



if __name__=="__main__":
    speak("Welcome Sir")
    wishMe()
    if 1:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("searching in wikipedia....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            print("According to Wikipedia...")
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif "quit" in query:
            print("Thanks for using me...., Have a Good Day")
            speak("Thanks for using me...., Have a Good Day")
            exit()
        elif "open youtube" in query:
           webbrowser.open("youtube.com")
        elif "open google" in query:
           webbrowser.open("google.com")
        elif "open facebook" in query:
           webbrowser.open("facebook.com")
        elif "open instagram" in query:
           webbrowser.open("instagram.com")
        elif "open gmail" in query:
           webbrowser.open("gmail.com")
       

        elif "play songs" in query:
            music_folder="C:\\Users\\sanus\\Music"
            songs=os.listdir(music_folder)
            print(songs)
            os.startfile(os.path.join(music_folder,songs[0]))
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            str_Time_hour=datetime.datetime.now().strftime("%H")
            str_Time_Minute=datetime.datetime.now().strftime("%M")
            print(strTime)
            speak(f"the time is{str_Time_hour} hour")
            speak(f"{str_Time_Minute} minutes")
        elif "open vs code" in query:
            code_Path="C:\\Users\\sanus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(os.path.join(code_Path))