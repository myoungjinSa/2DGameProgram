import pico2d

class Sound:
    music_list= ["Shape_of_you.wav","Han_ol.wav","Bolbbalgan.wav"]
    music = None
    #음악 길이
    SHAPE_OF_YOU_LENGTH = 15.00
    MEET_ON_SPRING_LENGTH = 15.00
    BLUE_LENGTH =15.00

    def __init__(self):
        self.EndTime = 0.0           #사운드 타임
        self.StartTime = 0.0
        self.music_Time = 0.0
        self.SoundLength = 0.0          #사운드 길이
        self.isChangeMusic = False      #음악의 변경이 있나 확인 변수
        self.SoundLength = 0.0

    def SetSoundLength(self,index):
        if index == 0:
            self.SoundLength = Sound.SHAPE_OF_YOU_LENGTH
        elif index == 1:
            self.SoundLength = Sound.MEET_ON_SPRING_LENGTH
        elif index == 2:
            self.SoundLength =Sound.BLUE_LENGTH

    def SetTickStart(self):
        self.StartTime = pico2d.get_time()


    def SetTickEnd(self):
        self.EndTime = pico2d.get_time()


    def CheckMusicTime(self):
        self.music_Time = self.EndTime - self.StartTime
        if self.music_Time >=self.SoundLength:
            return True
        else:
            return False



    def SetMusic(self,index):
        self.index = index
        pico2d.audio_on = True

        Sound.music=pico2d.load_wav(Sound.music_list[index])



    def IsChangeMusic(self,CurrMusicIndex):
        if self.index != CurrMusicIndex:
            return True
        else:
            return False


    def GetNextMusic(self):
        self.index = (self.index +1)%3


    def PlayMusic(self):
        if Sound.music !=None:
            Sound.music.play()



    def StopMusic(self):
        if Sound.music != None:
            Sound.music.stop()


    def RemoveMusic(self):
        if Sound.music !=None:
            del(Sound.music)



