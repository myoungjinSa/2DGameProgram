import pico2d

class SOUND:
    music_list= ["Shape_of_you.wav","Han_ol.wav","Bolbbalgan.wav"]
    music = None

    def __init__(self):
        self.music_Time = 0.0           #사운드 타임
        self.SoundLength = 0.0          #사운드 길이
        self.index =0
        self.isChangeMusic = False      #음악의 변경이 있나 확인 변수


    def SetMusic(self,index):
        self.index = index
        pico2d.audio_on = True
        SOUND.music=pico2d.load_wav(SOUND.music_list[index])

    def IsChangeMusic(self,CurrMusicIndex):
        if self.index != CurrMusicIndex:
            return True
        else:
            return False

    def GetNextMusic(self):
        self.index = (self.index +1)%3


    def PlayMusic(self):
        if SOUND.music !=None:
            SOUND.music.play()


    def StopMusic(self):
        if SOUND.music != None:
            SOUND.music.stop()

    def RemoveMusic(self):
        if SOUND.music !=None:
            del(SOUND.music)



