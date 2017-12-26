from pico2d import *
from Font import *

class GameManager:
    one_digit =0
    ten_digit =0
    hundred_digit =0
    def __init__(self):
        self.level = ["Level_One","Level_Two","Level_Three"]
        self.hitcount =0          #히트 카운트 변수
        self.hitMax =0             #실패하지않고 최대 히트한수
        self.hitTotal =0           #총 히트수
        self.pRevHit =0             #0으로 세팅되기전 hit수를 담는 변수
        self.font = FONT()          #글자 출력 폰트
        self.numfont =[FONT() for i in range(0, 3)]       #히트 수 출력 폰트
        self.font.SetFontPos(320,500)
        self.font.SetFontWH(200,75)
        self.numfont[0].SetFontPos(300, 400)
        self.numfont[0].SetFontWH(100, 100)
        self.numfont[1].SetFontPos(250, 400)
        self.numfont[1].SetFontWH(100, 100)
        self.numfont[2].SetFontPos(200, 400)
        self.numfont[2].SetFontWH(100, 100)
        if self.font.hitFont == None:
            self.font.hitFont = [load_image("Resource\HIT_Font.png"), load_image("Resource\miss.png")]
            for i in range(0,3):
                self.numfont[i].numFont = [load_image("Resource\Zero.png"), load_image("Resource\One.png"), load_image("Resource\Two.png"),
                                           load_image("Resource\Three.png"), load_image("Resource\Four.png"), load_image("Resource\Five.png"), load_image("Resource\Six.png"),
                                           load_image("Resource\Seven.png"), load_image("Resource\Eight.png"), load_image("Resource\_Nine.png")]


        self.isHit = False



    def SetStageLevel(self,level):  #stage level 별로 난이도 설정할수 있게 함수 구현
        self.level = level


    def CheckHitCount(self):
        self.MaxHitCount()

        return self.hitcount

    def GetHitCount(self):
        return self.hitcount


    def GetReturnIsHit(self):
        return self.isHit

    def MaxHitCount(self):
        if self.pRevHit > self.hitcount:
            self.hitMax = self.pRevHit
        else:
            self.hitMax = self.hitcount

        return self.hitMax


    def SetTotalCountZero(self):        #총 히트수 초기화 해주는 함수
        self.hitTotal =0

    def GetTotal(self):
        return self.hitTotal

    def HitTotalCount(self):    #총 히트수 증가 함수
        self.hitTotal+=1


    def HitCount(self):         #히트수 증가 함수
        self.hitcount +=1



    def SetMusicStatus(self,num):      #음악
        pass


    def GameInfoDraw(self):             #게임 정보 그리기
        print("HIT:%d",self.hitcount)


    def ChangeGameStatus(self,status):
        pass


    def SetZeroHitCount(self):
        if self.hitcount != 0:
            if self.hitcount >= self.pRevHit:
                self.pRevHit = self.hitcount

            self.hitcount =0


    def draw(self,boolean):
        if boolean ==1:
            if self.isHit == True:
                self.font.hitFont[0].draw(self.font.x, self.font.y, self.font.fontWidth, self.font.fontHeight)
                if self.hitcount < 10:
                    self.numfont[0].numFont[self.hitcount].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
                if self.hitcount>=10 and self.hitcount <100:
                    GameManager.ten_digit = self.hitcount/10
                    self.numfont[0].numFont[self.hitcount % 10].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
                    self.numfont[1].numFont[int(GameManager.ten_digit)].draw(self.numfont[1].x, self.numfont[1].y, self.numfont[1].fontWidth, self.numfont[1].fontHeight)
                if self.hitcount >=100 and self.hitcount <1000:
                    GameManager.ten_digit = (self.hitcount % 100) / 10
                    hundred_digit = self.hitcount/100
                    self.numfont[0].numFont[self.hitcount % 10].draw(self.numfont[0].x, self.numfont[0].y, self.numfont[0].fontWidth, self.numfont[0].fontHeight)
                    self.numfont[1].numFont[int(GameManager.ten_digit)].draw(self.numfont[1].x, self.numfont[1].y, self.numfont[1].fontWidth, self.numfont[1].fontHeight)
                    self.numfont[2].numFont[int(hundred_digit)].draw(self.numfont[2].x, self.numfont[2].y, self.numfont[2].fontWidth, self.numfont[2].fontHeight)
            elif self.isHit==False:
                self.font.hitFont[1].draw(self.font.x, self.font.y, self.font.fontWidth, self.font.fontHeight)

        elif boolean == 2:
            pass



