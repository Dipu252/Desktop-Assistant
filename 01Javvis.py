import pyttsx3
import datetime
import wish
import speech_recognition as sr
import speak
import speech_Recognition as sR
import search_wikipedia as sw
import playsong
import seach_webbrowser as sb
import open_directory as opd

def stop():
    sp=speak.Speak()
    query='Dipu'
    while "hello jarvis" not in query:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1
            r.energy_threshold=300
            audio=r.listen(source)
            try:
                query=r.recognize_google(audio,language="en-in")
                query=query.lower()
            except Exception as e:
                pass
    sp.speak('Hello sir!, Please tell me. How may i help you?')


if __name__=='__main__':
    wish.wishMe()

    while True:
        takecommand=sR.Command()
        query=takecommand.takeCommand().lower()

        if 'quite' in query:
            break

        if 'stop jarvis' in query:
            stop()

        if 'wikipedia' in query:
            wiki=sw.Wikipedia()
            query=wiki.Search_wikipedia(query)

        elif 'play song' in query or 'play music' in query:
            py=playsong.Playsond()
            py.music_player()

        elif 'browser' in query:
            browser=sb.Webbrowser()
            browser.open_webbrowser(query)

        elif 'open' in query:
            directroy=opd.Directory()
            directroy.open_dir(query)