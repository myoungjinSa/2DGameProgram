import pico2d

class SOUND:
    music=None
    def __init__(self):
        self.music_Time = 0.0           #사운드 타임
        self.SoundLength = 0.0          #사운드 길이


    def SetMusic(self,name):
        if SOUND.music == None:
            if pico2d.audio_on is False:
                pico2d.audio_on = True
                SOUND.music = pico2d.load_music(name)


    def PlayMusic(self):
        if SOUND.music !=None:
            SOUND.music.play()


    def StopMusic(self):
        if SOUND.music != None:
            SOUND.music.stop()

    def RemoveMusic(self):
        if SOUND.music !=None:
            del(SOUND.music)



