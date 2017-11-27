from Note import *
from pico2d import *

class Board:
    stageImage = None
    boardImage = None
    hitEffect = None
    keydown_flag = False
    def __init__(self):
        self.boardPosX, self.boardPosY = 300, 370 #보드판이 그려질 위치
        self.boardWidth, self.boardHeight = 600, 761 #보드판의 사이즈
        self.stagePosX, self.stagePosY = 880, 370 #스테이지 위치
        self.stageSizeX, self.stageSizeY = 561, 761 #스테이지 이미지 사이즈
        self.board_LeftTopX = self.boardPosX - 300
        self.board_LeftTopY = self.boardPosY - 370
        self.boardSeperateCount = 5                            #보드의 분할된 갯수
        self.keybox = None                         #키 박스 초기화
        self.hitEffectPosX =0.0                  #히트 이펙트가 그려질 X위치
        self.hitEffectPosY =78.0                #히트 이펙트가 그려질 Y위치
        self.hitEffectWidth =120
        self.hitEffectHeight = 100
        if Board.stageImage==None and Board.boardImage ==None:  #보드판과 키박스 이미지가 None 이면 이미지 삽입
            self.stageImage = load_image('Resource\stage_bitmap.png')
            self.boardImage = load_image('Resource\Board.png')
            self.hitEffect = load_image('Resource\Hit_Light.png')


    def CreateKeyBox(self):                                     #키박스 생성 함수
        if self.keybox == None:                                 #키박스가 없으면
            self.keybox = [Keybox() for i in range(0, 5)]      #KeyBox 5개 설정

        for i in range(0,5):
            #self.keybox[i].isKeyBox = True
            self.keybox[i].SetPosition(59 + (i * self.keybox[i].GetWidth()), 15)


    def GiveKeyBoxSelect(self,num):                                 #KeyBox 활성화하는 함수
        if self.keybox[num] != None:
            self.keybox[num].isSelect = True
            Board.keydown_flag = True
            self.hitEffectPosX = 59 + (num * self.hitEffectWidth)


    def GiveKeyBoxUnSelect(self,num,GameManager):                               #KeyBox 비활성화 함수
        if self.keybox[num] !=None:
            self.keybox[num].isSelect = False
            Board.keydown_flag = False



    def update(self):
        pass


    def SetIsHitTrue(self):
        if Board.is_Hit is False:
            Board.is_Hit = True


    def SetIsHitFalse(self):
        if Board.is_Hit is True:
            Board.is_Hit = False


    def draw(self):
        self.boardImage.draw(self.boardPosX, self.boardPosY, self.boardWidth, self.boardHeight)
        self.stageImage.draw(self.stagePosX, self.stagePosY, self.stageSizeX, self.stageSizeY)


        if self.keybox !=None:
            for i in range(0, self.boardSeperateCount):
                self.keybox[i].draw()

        if Board.keydown_flag == True:
            self.hitEffect.opacify(0.7)
            self.hitEffect.draw(self.hitEffectPosX, self.hitEffectPosY, self.hitEffectWidth, self.hitEffectHeight)


