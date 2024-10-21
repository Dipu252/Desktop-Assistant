import pyttsx3
import datetime
import speak

def wishMe():
    hour=int(datetime.datetime.now().hour)

    sp=speak.Speak()
    
    if hour>=0 and hour<12:
        sp.speak("Good morning!,sir")

    elif hour>=12 and hour<18:
        sp.speak("Good afternoon!,sir")
    
    else:
        sp.speak("Good evening!,sir")
    
    sp.speak("I am jarvis. Please tell me, how may i help you?")

    