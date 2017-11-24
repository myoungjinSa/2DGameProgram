from pico2d import *
from Font import *
import json
from gameManager import *

class GameInfoScreen:
    InfoImage = ["GameInfo_Animation_1.png","GameInfo_Animation_2.png","GameInfo_Animation_3.png","GameInfo_Animation_4.png"]

    def __init__(self):
        self.drawX,self.drawY = 0.0,0.0
        self.width = 0.0
        self.height = 0.0

        self.maxHit =0
        self.totalHit =0

        self.Animate_index = 0
        self.image = None
        self.max_hit_Image = load_image("max_hit.png")
        self.total_hit_Image =load_image("total_hit.png")
        self.Numfont = [FONT() for i in range(0, 3)]
        self.TotalNumfont = [FONT() for i in range(0,3)]

        if self.Numfont !=None:
            for i in range(0, 2):
                self.Numfont[i].NumFont = [load_image("Num_0.png"), load_image("Num_1.png"), load_image("Num_2.png"), load_image("Num_3.png"), load_image("Num_4.png"), load_image("Num_5.png"),
                                       load_image("Num_6.png"), load_image("Num_7.png")  , load_image("Num_8.png"), load_image("Num_9.png")]

        if self.TotalNumfont != None:
            for i in range(0,2):
                self.TotalNumfont[i].NumFont = [load_image("Num_0.png"), load_image("Num_1.png"), load_image("Num_2.png"), load_image("Num_3.png"), load_image("Num_4.png"), load_image("Num_5.png"),
                                       load_image("Num_6.png"), load_image("Num_7.png")  , load_image("Num_8.png"), load_image("Num_9.png")]


        self.Numfont[0].SetFontPos(650, 300)
        self.Numfont[0].SetFontWH(100, 100)
        self.Numfont[1].SetFontPos(600, 300)
        self.Numfont[1].SetFontWH(100, 100)
        self.Numfont[2].SetFontPos(550, 300)
        self.Numfont[2].SetFontWH(100, 100)

        self.TotalNumfont[0].SetFontPos(650, 500)
        self.TotalNumfont[0].SetFontWH(100, 100)
        self.TotalNumfont[1].SetFontPos(600, 500)
        self.TotalNumfont[1].SetFontWH(100, 100)
        self.TotalNumfont[2].SetFontPos(550, 500)
        self.TotalNumfont[2].SetFontWH(100, 100)



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
        text = open("max_total.txt","r")
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
        self.Animate_index = self.Animate_index + 1
        self.image = load_image(GameInfoScreen.InfoImage[self.Animate_index%4])

        delay(0.1)

    def draw(self):
        self.image.draw(self.width,self.height)                                     #0,0이 왼쪽 아래 축 기준이므로 오른쪽으로 width만큼 위쪽으로 height만큼 넘겨라
        self.max_hit_Image.draw(self.max_Font_PosX,self.max_Font_PosY)
        self.total_hit_Image.draw(self.total_Font_PosX,self.total_Font_PosY)

        if self.maxHit <10:
            self.Numfont[0].NumFont[self.maxHit].draw(self.Numfont[0].x, self.Numfont[0].y, self.Numfont[0].FontWidth,
                                                        self.Numfont[0].FontHeight)
        elif self.maxHit >=10 and self.maxHit <100 :
            GameManager.ten_digit = self.maxHit / 10
            self.Numfont[0].NumFont[self.maxHit % 10].draw(self.Numfont[0].x, self.Numfont[0].y,self.Numfont[0].FontWidth, self.Numfont[0].FontHeight)
            self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.Numfont[1].x, self.Numfont[1].y,self.Numfont[1].FontWidth,self.Numfont[1].FontHeight)

        elif self.maxHit >= 100 and self.maxHit < 1000:
            GameManager.hundred_digit = self.maxHit / 100
            self.Numfont[0].NumFont[self.maxHit % 10].draw(self.Numfont[0].x, self.Numfont[0].y,self.Numfont[0].FontWidth, self.Numfont[0].FontHeight)
            self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.Numfont[1].x, self.Numfont[1].y,self.Numfont[1].FontWidth,self.Numfont[1].FontHeight)
            self.Numfont[2].NumFont[int(GameManager.hundred_digit)].draw(self.Numfont[2].x, self.Numfont[2].y,self.Numfont[2].FontWidth,self.Numfont[2].FontHeight)


        if self.totalHit <10:
            self.Numfont[0].NumFont[self.totalHit].draw(self.TotalNumfont[0].x,self.TotalNumfont[0].y,self.TotalNumfont[0].FontWidth,self.TotalNumfont[0].FontHeight)

        elif self.totalHit >=10 and self.totalHit <100 :
            GameManager.ten_digit = self.totalHit / 10
            self.Numfont[0].NumFont[self.totalHit % 10].draw(self.TotalNumfont[0].x, self.TotalNumfont[0].y,self.TotalNumfont[0].FontWidth, self.TotalNumfont[0].FontHeight)
            self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.TotalNumfont[1].x, self.TotalNumfont[1].y,self.TotalNumfont[1].FontWidth,self.TotalNumfont[1].FontHeight)

        elif self.totalHit >= 100 and self.totalHit < 1000:
            GameManager.hundred_digit = self.totalHit / 100
            self.Numfont[0].NumFont[self.totalHit % 10].draw(self.TotalNumfont[0].x, self.TotalNumfont[0].y,self.TotalNumfont[0].FontWidth, self.TotalNumfont[0].FontHeight)
            self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.TotalNumfont[1].x, self.TotalNumfont[1].y,self.TotalNumfont[1].FontWidth,self.TotalNumfont[1].FontHeight)
            self.Numfont[2].NumFont[int(GameManager.hundred_digit)].draw(self.TotalNumfont[2].x, self.TotalNumfont[2].y,self.TotalNumfont[2].FontWidth,self.TotalNumfont[2].FontHeight)



