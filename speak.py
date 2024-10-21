import pyttsx3

class Speak:
    
    def __init__(self,gender=0) -> None:
        self.engine=pyttsx3.init('sapi5')
        voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[gender].id)

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()