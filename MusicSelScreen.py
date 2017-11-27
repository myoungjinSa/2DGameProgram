from pico2d import *
from gameManager import *

class MusicSelScreen:
    Sel_image = ["Resource\select_Ed_Sheeran.png","Resource\select_han_ol.png","Resource\select_Blue.png"]
    def __init__(self):
        self.drawX,self.drawY = 0.0,0.0
        self.width = 0
        self.height = 0
        self.curImage = load_image(MusicSelScreen.Sel_image[0])                                               #현재 그리고있는 이미지
        self.curMusic = 0


    def GetCurrentMusic(self):
        return self.curMusic

    def SetDrawPosX(self,x,y):
        self.drawX = x
        self.drawY = y


    def SetDrawWH(self,width,height):
        self.width = width/2
        self.height = height/2


    def upCurrentMusic(self):
        self.curMusic +=1


    def handle_events(self):
        pass

    def update(self,direction):
        if direction == "right":
            self.curMusic = (self.curMusic+1) %3
            self.curImage = load_image(MusicSelScreen.Sel_image[self.curMusic])
        elif direction == "left":
            self.curMusic = (self.curMusic-1)%3
            self.curImage = load_image(MusicSelScreen.Sel_image[self.curMusic])

    def draw(self):
        self.curImage.draw(580,375)




