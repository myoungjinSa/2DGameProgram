from pico2d import *
from Font import *

class GameManager:
    one_digit =0
    ten_digit =0
    hundred_digit =0
    def __init__(self):
        self.level = ["Level_One","Level_Two","Level_Three"]
        self.hitcount =0          #히트 카운트 변수
        self.HitMax =0             #실패하지않고 최대 히트한수
        self.HitTotal =0           #총 히트수
        self.pRevHit =0             #0으로 세팅되기전 hit수를 담는 변수
        self.font = FONT()          #글자 출력 폰트
        self.Numfont =[FONT() for i in range(0,3)]       #히트 수 출력 폰트
        self.font.SetFontPos(320,500)
        self.font.SetFontWH(200,75)
        self.Numfont[0].SetFontPos(300,400)
        self.Numfont[0].SetFontWH(100,100)
        self.Numfont[1].SetFontPos(250,400)
        self.Numfont[1].SetFontWH(100,100)
        self.Numfont[2].SetFontPos(150,400)
        self.Numfont[2].SetFontWH(100,100)
        if self.font.HitFont == None:
            self.font.HitFont = [load_image("HIT_Font.png"),load_image("miss.png")]
            for i in range(0,2):
                self.Numfont[i].NumFont = [load_image("Num_0.png"),load_image("Num_1.png"),load_image("Num_2.png"),load_image("Num_3.png"),load_image("Num_4.png"),load_image("Num_5.png"),load_image("Num_6.png"),load_image("Num_7.png")\
            ,load_image("Num_8.png"),load_image("Num_9.png")]


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
            self.HitMax = self.pRevHit
        else:
            self.HitMax = self.hitcount

        return self.HitMax


    def TotalZero(self):        #총 히트수 초기화 해주는 함수
        self.HitTotal =0

    def GetTotal(self):
        return self.HitTotal

    def HitTotalCount(self):    #총 히트수 증가 함수
        self.HitTotal+=1


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
        if boolean ==True:
            if self.isHit == True:
                self.font.HitFont[0].draw(self.font.x,self.font.y,self.font.FontWidth,self.font.FontHeight)
                if self.hitcount < 10:
                    self.Numfont[0].NumFont[self.hitcount].draw(self.Numfont[0].x,self.Numfont[0].y,self.Numfont[0].FontWidth,self.Numfont[0].FontHeight)
                if self.hitcount>=10 and self.hitcount <100:
                    GameManager.ten_digit = self.hitcount/10
                    self.Numfont[0].NumFont[self.hitcount%10].draw(self.Numfont[0].x, self.Numfont[0].y,self.Numfont[0].FontWidth, self.Numfont[0].FontHeight)
                    self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.Numfont[1].x, self.Numfont[1].y,self.Numfont[1].FontWidth, self.Numfont[1].FontHeight)
                if self.hitcount >=100 and self.hitcount <1000:
                    GameManager.hundred_digit = self.hitcount/100
                    self.Numfont[0].NumFont[self.hitcount % 10].draw(self.Numfont[0].x, self.Numfont[0].y, self.Numfont[0].FontWidth,self.Numfont[0].FontHeight)
                    self.Numfont[1].NumFont[int(GameManager.ten_digit)].draw(self.Numfont[1].x, self.Numfont[1].y,self.Numfont[1].FontWidth,self.Numfont[1].FontHeight)
                    self.Numfont[2].NumFont[int(GameManager.hundred_digit)].draw(self.Numfont[2].x, self.Numfont[2].y,self.Numfont[2].FontWidth,self.Numfont[2].FontHeight)
            elif self.isHit==False:
                #self.font.HitFont[1].draw(self.font.x,self.font.y,self.font.FontWidth,self.font.FontHeight)
                pass
        else:
            pass


