from pico2d import *
from Font import *

class GameManager:

    def __init__(self):
        self.level = ["Level_One","Level_Two","Level_Three"]
        self.hitcount =0          #히트 카운트 변수
        self.HitMax =0             #실패하지않고 최대 히트한수
        self.HitTotal =0           #총 히트수
        self.pRevHit =0             #0으로 세팅되기전 hit수를 담는 변수
        self.font = FONT()
        self.font.SetFontPos(300,500)
        self.font.SetFontWH(200,100)
        if self.font.HitFont == None:
            self.font.HitFont = [load_image("HIT_Font.png"),load_image("miss.png")]

        self.isHit = False



    def SetStageLevel(self,level):  #stage level 별로 난이도 설정할수 있게 함수 구현
        self.level = level



    def GetHitCount(self):
        return self.hitcount


    def GetReturnIsHit(self):
        return self.isHit

    def MaxHitCount(self):
        if self.pRevHit > self.hitcount:
            self.HitMax = self.pRevHit
        else:
            self.HitMax = self.hitcount


    def TotalZero(self):        #총 히트수 초기화 해주는 함수
        self.HitTotal =0

    def HitTotalCount(self):    #총 히트수 증가 함수
        self.HitTotal+=1

        return self.HitTotal

    def HitCount(self):         #히트수 증가 함수
        self.hitcount +=1


    def ShowGameResult(self):
        pass

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


    def draw(self):
        if self.isHit == True:
            self.font.HitFont[0].draw(self.font.x,self.font.y,self.font.FontWidth,self.font.FontHeight)
        elif self.isHit==False:
            self.font.HitFont[1].draw(self.font.x,self.font.y,self.font.FontWidth,self.font.FontHeight)



