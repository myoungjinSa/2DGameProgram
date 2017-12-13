import pico2d

class Sound:
    music_list= ["Shape_of_you.wav","Han_ol.wav","Bolbbalgan.wav"]
    music = None
    #음악 길이
    SHAPE_OF_YOU_LENGTH = 75.00
    MEET_ON_SPRING_LENGTH = 85.00
    BLUE_LENGTH =75.00

    def __init__(self):
        self.endTime = 0.0           #사운드 타임
        self.startTime = 0.0
        self.music_Time = 0.0
        self.soundLength = 0.0          #사운드 길이
        self.isChangeMusic = False      #음악의 변경이 있나 확인 변수
        self.soundLength = 0.0

    def SetSoundLength(self,index):
        if index == 0:
            self.soundLength = Sound.SHAPE_OF_YOU_LENGTH
        elif index == 1:
            self.soundLength = Sound.MEET_ON_SPRING_LENGTH
        elif index == 2:
            self.soundLength =Sound.BLUE_LENGTH

    def SetTickStart(self):
        self.startTime = pico2d.get_time()


    def SetTickEnd(self):
        self.endTime = pico2d.get_time()


    def CheckMusicTime(self):
        self.music_Time = self.endTime - self.startTime
        if self.music_Time >=self.soundLength:
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



