import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am spandy Mam. Please tell me how may I help you.")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'play music' in query:
            music_dir = r"C:\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {current_time}")

        elif 'open code' in query:
            code_path = r"C:\Users\adich\OneDrive\Documents\github\Oasis\OIBSIP.HQ"
            os.startfile(code_path)
