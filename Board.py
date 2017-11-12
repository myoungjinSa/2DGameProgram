from Note import *
from pico2d import *

class BOARD:
    stageImage = None
    boardImage = None
    Hit_Effect = None
    isKey_Down = False
    def __init__(self):
        self.BoardPosX, self.BoardPosY = 300, 370 #보드판이 그려질 위치
        self.BoardWidth, self.BoardHeight = 600, 761 #보드판의 사이즈
        self.StagePosX,self.StagePosY = 880,370 #스테이지 위치
        self.StageSizeX,self.StageSizeY = 561,761 #스테이지 이미지 사이즈
        self.BoardLeftTopX = self.BoardPosX-300
        self.BoardLeftTopY = self.BoardPosY-370
        self.count = 5                            #보드의 분할된 갯수
        self.KeyBox = None                         #키 박스 초기화
        self.Hit_Effect_PosX =0.0                  #히트 이펙트가 그려질 X위치
        self.Hit_Effect_PosY =105.0                #히트 이펙트가 그려질 Y위치
        self.Hit_Effect_Width =120
        self.Hit_Effect_Height = 150
        if BOARD.stageImage==None and BOARD.boardImage ==None:  #보드판과 키박스 이미지가 None 이면 이미지 삽입
            self.stageImage = load_image('stage_bitmap.png')
            self.boardImage = load_image('board.png')
            self.Hit_Effect = load_image('Hit_Light.png')


    def CreateKeyBox(self):                                     #키박스 생성 함수
        if self.KeyBox == None:                                 #키박스가 없으면
            self.KeyBox = [NOTE(True) for i in range(0,5)]      #KeyBox 5개 설정

        for i in range(0,5):
            self.KeyBox[i].isKeyBox = True
            self.KeyBox[i].SetPosition(59+(i*self.KeyBox[i].width),15)


    def GiveKeyBoxSelect(self,num):                                 #KeyBox 활성화하는 함수
        if self.KeyBox[num] != None:
            self.KeyBox[num].isSelect = True
            BOARD.isKey_Down = True
            self.Hit_Effect_PosX = 59+(num*self.Hit_Effect_Width)


    def GiveKeyBoxUnSelect(self,num):                               #KeyBox 비활성화 함수
        if self.KeyBox[num] !=None:
            self.KeyBox[num].isSelect = False
            BOARD.isKey_Down = False


    def update(self):
        pass



    def draw(self,name):
        self.boardImage.draw(self.BoardPosX,self.BoardPosY,self.BoardWidth,self.BoardHeight)
        self.stageImage.draw(self.StagePosX,self.StagePosY,self.StageSizeX,self.StageSizeY)

        if self.KeyBox !=None:
            for i in range(0,self.count):
                self.KeyBox[i].draw()

        if BOARD.isKey_Down == True:
            self.Hit_Effect.opacify(0.5)
            self.Hit_Effect.draw(self.Hit_Effect_PosX,self.Hit_Effect_PosY,self.Hit_Effect_Width,self.Hit_Effect_Height)



