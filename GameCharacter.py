from pico2d import *

class GuitarList:
    Guitar_Image_List = ["Guitar_Boy_One.png","Guitar_Boy_Two.png","Guitar_Boy_Three.png","Guitar_Boy_Four.png","Guitar_Boy_Five.png","Guitar_Boy_Six.png"]
    Animate_Index =0
    def __init__(self):
        self.positionX,self.positionY =0.0 , 0.0
        self.width = 99
        self.height =87
        self.image = [load_image(GuitarList.Guitar_Image_List[i]) for i in range(0,6)]

    def SetPosition(self,x,y):
        self.positionX = x
        self.positionY = y

    def update(self):
        GuitarList.Animate_Index +=1
    def draw(self):
        self.image[GuitarList.Animate_Index%6].draw(self.positionX,self.positionY,self.width,self.height)



class SpecTator:
    pass