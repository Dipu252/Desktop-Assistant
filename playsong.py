import pyttsx3
import os
import speak

class Playsond:

    def __init__(self) -> None:
        self.sp=speak.Speak()

    def music_player(self):

        music_dic='D:\\music'
        songs=os.listdir(music_dic)
        print(list(enumerate(songs,1)))
        self.sp.speak('Which song number should i play?')
        n=int(input('Song number: '))
        os.startfile(os.path.join(music_dic,songs[n-1]))
