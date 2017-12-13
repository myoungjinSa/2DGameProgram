from pico2d import *
from Font import *
import json
from gameManager import *

class GameInfoScreen:
    InfoImage = ["Resource\GameInfo_Animation_1.png","Resource\GameInfo_Animation_2.png","Resource\GameInfo_Animation_3.png","Resource\GameInfo_Animation_4.png"]

    def __init__(self):
        self.drawX,self.drawY = 0.0,0.0
        self.width = 0.0
        self.height = 0.0

        self.maxHit =0
        self.totalHit =0

        self.animate_index = 0
        self.image = None
        self.max_hit_Image = load_image("Resource\max_hit.png")
        self.total_hit_Image =load_image("Resource\_total_hit.png")
        self.numfont = [FONT() for i in range(0, 3)]
        self.totalNumfont = [FONT() for i in range(0, 3)]

        if self.numfont !=None:
            for i in range(0, 3):
                self.numfont[i].numFont = [load_image("Resource\Zero.png"), load_image("Resource\One.png"), load_image("Resource\Two.png"), load_image("Resource\Three.png"),
                                           load_image("Resource\Four.png"), load_image("Resource\Five.png"), load_image("Resource\Six.png"),
                                           load_image("Resource\Seven.png")  , load_image("Resource\Eight.png"), load_image("Resource\_Nine.png")]

        if self.totalNumfont != None:
            for i in range(0,3):
                self.totalNumfont[i].numFont = [load_image("Resource\Zero.png"), load_image("Resource\One.png") , load_image("Resource\Two.png"), load_image("Resource\Three.png"),
                                                load_image("Resource\Four.png"), load_image("Resource\Five.png"), load_image("Resource\Six.png"),
                                                load_image("Resource\Seven.png")  , load_image("Resource\Eight.png"), load_image("Resource\_Nine.png")]


        self.numfont[0].SetFontPos(650, 300)
        self.numfont[0].SetFontWH(100, 100)
        self.numfont[1].SetFontPos(590, 300)
        self.numfont[1].SetFontWH(100, 100)
        self.numfont[2].SetFontPos(530, 300)
        self.numfont[2].SetFontWH(100, 100)

        self.totalNumfont[0].SetFontPos(650, 500)
        self.totalNumfont[0].SetFontWH(100, 100)
        self.totalNumfont[1].SetFontPos(590, 500)
        self.totalNumfont[1].SetFontWH(100, 100)
        self.totalNumfont[2].SetFontPos(530, 500)
        self.totalNumfont[2].SetFontWH(100, 100)



        self.max_Font_PosX,self.max_Font_PosY = 0.0,0.0
        self.total_Font_PosX,self.total_Font_PosY =0.0,0.0

    def SetMaxFontPos(self,x,y):
        self.max_Font_PosX = x
        self.max_Font_PosY = y

    def SetTotalFontPos(self,x,y):
        self.total_Font_PosX = x
        self.total_Font_PosY = y

    def SetInfoScreenPos(self,x,y):
        self.drawX = x
        self.drawY = y


    def ReadMaxTotalCount(self):
        text = open("Text\max_total.txt","r")
        maxTotal = json.load(text)
        self.maxHit = maxTotal[0]
        self.totalHit = maxTotal[1]
        text.close()


    def SetInfoScreenWH(self,width,height):
        self.width = width/2
        self.height = height/2



    def handle_events(self):
        pass

    def update(self):
        self.animate_index = self.animate_index + 1
        self.image = load_image(GameInfoScreen.InfoImage[self.animate_index % 4])

        delay(0.1)

    def draw(self):
        self.image.draw(self.width,self.height)                                     #0,0이 왼쪽 아래 축 기준이므로 오른쪽으로 width만큼 위쪽으로 height만큼 넘겨라
        self.max_hit_Image.draw(self.max_Font_PosX,self.max_Font_PosY)
        self.total_hit_Image.draw(self.total_Font_PosX,self.total_Font_PosY)

        if self.maxHit <10:
           self.numfont[0].numFont[self.maxHit].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
                                                        #self.Numfont[0].FontHeight)
        elif self.maxHit >=10 and self.maxHit <100 :
            ten_digit = self.maxHit / 10
            self.numfont[0].numFont[self.maxHit % 10].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
            self.numfont[1].numFont[int(ten_digit)].draw(self.numfont[1].x, self.numfont[1].y, self.numfont[1].fontWidth, self.numfont[1].fontHeight)

        elif self.maxHit >= 100 and self.maxHit < 1000:
            ten_digit = (self.maxHit%100)/10
            hundred_digit = self.maxHit/100
            self.numfont[0].numFont[self.maxHit % 10].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
            self.numfont[1].numFont[int(ten_digit)].draw(self.numfont[1].x, self.numfont[1].y, self.numfont[1].fontWidth, self.numfont[1].fontHeight)
            self.numfont[2].numFont[int(hundred_digit)].draw(self.numfont[2].x, self.numfont[2].y, self.numfont[2].fontWidth, self.numfont[2].fontHeight)


        if self.totalHit <10:
            self.totalNumfont[0].numFont[self.totalHit].draw(self.totalNumfont[0].x, self.totalNumfont[0].y, self.totalNumfont[0].fontWidth, self.totalNumfont[0].fontHeight)

        elif self.totalHit >=10 and self.totalHit <100 :
            ten_digit = self.totalHit / 10
            self.totalNumfont[0].numFont[self.totalHit % 10].draw(self.totalNumfont[0].x, self.totalNumfont[0].y, self.totalNumfont[0].fontWidth, self.totalNumfont[0].fontHeight)
            self.totalNumfont[1].numFont[int(ten_digit)].draw(self.totalNumfont[1].x, self.totalNumfont[1].y, self.totalNumfont[1].fontWidth, self.totalNumfont[1].fontHeight)

        elif self.totalHit >= 100 and self.totalHit < 1000:
            ten_digit = (self.totalHit%100)/10
            hundred_digit = self.totalHit/100
            self.totalNumfont[0].numFont[self.totalHit % 10].draw(self.totalNumfont[0].x, self.totalNumfont[0].y, self.totalNumfont[0].fontWidth, self.totalNumfont[0].fontHeight)
            self.totalNumfont[1].numFont[int(ten_digit)].draw(self.totalNumfont[1].x, self.totalNumfont[1].y, self.totalNumfont[1].fontWidth, self.totalNumfont[1].fontHeight)
            self.totalNumfont[2].numFont[int(hundred_digit)].draw(self.totalNumfont[2].x, self.totalNumfont[2].y, self.totalNumfont[2].fontHeight, self.totalNumfont[2].fontHeight)



