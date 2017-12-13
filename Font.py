from pico2d import *

mouseOnGameStart = False

class FONT:
    fontString = []
    count =13
    dir = 1
    def __init__(self):
        self.x = 0
        self.y = 0
        self.fontWidth = 0.0
        self.fontHeight = 0.0
        self.image = Image
        self.total =0
        self.hitFont = None
        self.numFont=None

    def SetImage(self,name):
        self.image = load_image(name)


    def SetFontPos(self,x,y):
        self.x=x
        self.y=y


    def SetFontWH(self,width, height):
        self.fontWidth = width
        self.fontHeight = height


    def draw(self):
        global mouseOnGameStart
        if mouseOnGameStart == True:
            self.image.opacify(0.5)
        else:
            self.image.opacify(1)
        self.image.draw(self.x, self.y, self.fontWidth, self.fontHeight)


    def update(self):
        self.total+=self.dir
        if self.total >50 :
            self.dir=-1
        elif self.total<0:
            self.dir=1
        self.y+=self.dir












