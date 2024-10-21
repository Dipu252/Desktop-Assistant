import pyttsx3
import webbrowser
class Webbrowser:

    def open_webbrowser(self,query):
        if 'open youtube' in query:
            webbrowser.open('youtube.com')

        if 'open google' in query:
            webbrowser.open('google.com')
        
        if 'open leetcode' in query or 'open leet code' in query or 'open leed code' in query or 'open lead code' in query:
            webbrowser.open('https://leetcode.com//problemset//?sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkZST05URU5EX0lEIn1d&difficulty=EASY&page=1&listId=wpwgkgt')
        
        if 'open hackerrank' in query or 'open hacker rank' in query:
            webbrowser.open('https://www.hackerrank.com/dashboard')

        if "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
