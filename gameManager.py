import pico2d

class GameManager:
    def __init__(self):
        self.level = ["Level_One","Level_Two","Level_Three"]
        self.HitCount =0          #히트 카운트 변수
        self.HitMax =0             #실패하지않고 최대 히트한수
        self.HitTotal =0           #총 히트수



    def SetStageLevel(self,level):  #stage level 별로 난이도 설정할수 있게 함수 구현
        self.level = level


    def TotalZero(self):        #총 히트수 초기화 해주는 함수
        self.HitTotal =0

    def HitTotalCount(self):    #총 히트수 증가 함수
        self.HitTotal+=1

        return self.HitTotal

    def HitCount(self):         #히트수 증가 함수
        self.Hit +=1


    def ShowGameResult(self):
        pass

    def SetMusicStatus(self,num):      #음악
        pass


    def GameInfoDraw(self):             #게임 정보 그리기
        pass


    def ChangeGameStatus(self,status):
        pass


    def SetZeroHitCount(self):
        if(self.HitCount != 0  ):
            self.HitCount =0








