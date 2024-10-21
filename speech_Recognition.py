import pyttsx3
import speech_recognition as sr

class Command:
    
    def takeCommand(self):
        # '''this is take voice command from use by microphone'''
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"Use said: {query}")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
