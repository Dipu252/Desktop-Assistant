import pyttsx3
import wikipedia
import speak

class Wikipedia:

    def __init__(self) -> None:
        self.sp=speak.Speak()

    def Search_wikipedia(self,query):
        self.sp.speak('Searching wikipedia')
        result=wikipedia.summary(query,sentences=2)
        query=query.replace('wikipedia','')
        self.sp.speak('According to wikipedia')
        print(result)
        self.sp.speak(result)
        return query

