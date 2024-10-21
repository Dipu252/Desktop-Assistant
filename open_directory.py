import pyttsx3
import os

class Directory:
    def open_dir(self,query):

        if 'open vs code' in query:
            codePath='C:\\Users\\kushw\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'open chrome' in query or 'open google chrome' in query:
            chromePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chromePath)
        elif 'open vlc' in query:
            vlcPath='C:\\Program Files\\VideoLAN\VLC\\vlc.exe'
            os.startfile(vlcPath)

