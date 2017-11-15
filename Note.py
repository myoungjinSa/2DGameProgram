from pico2d import *
import random


class NOTE:
    index =0                                                                    #KeyBox 이미지 삽입시 나머지 연산에 쓰일 클래스 변수
    NoteImage= ["note_blue.png","note_red.png","note_grey.png","note_pink.png","note_orange.png"]
    KeyBoxImage = {0: 'keyBox_Dark.png', 1: 'keyBox_Green.png', 2: 'keyBox_HotPink.png', 3: 'keyBox_Sand.png',4: 'keyBox_Sea.png'}
    def __init__(self,bool):                            #bool 값이 False 이면 일반 노트이미지를 로드하며 True 이면 KeyBox 이미지를 로드한다.
        self.width = 120        #노트 너비
        self.height = 30        #노트 높이
        self.speed = 0           #노트 스피드
        self.isHit = False      #노트 히트 검사 여부 플래그
        self.isSelect = False   #활성화 된 노트 플래그 True = 활성화 False = 비활성화
        self.isKeyBox = False   #KeyBox 가 아니면 False KeyBox 이면 True
        self.distance = 0.0
        #--------노트 이미지 변수-----------------------
        if bool == False:                                                       #bool 이 False 이면 일반 노트 이미지 로딩
            self.image =load_image(NOTE.NoteImage[random.randint(0,4)])         #image에 NoteImage 인덱스 0~3중 랜덤으로 이미지 삽입
        else:                                                                   #bool 이 True 이면 KeyBox 이미지 로딩
            self.image =load_image(NOTE.KeyBoxImage[NOTE.index%5])              #image에 KeyBoxImage 인덱스 5개를 인덱스 값을 증가시키며 나머지 연산으로 삽입
            NOTE.index+=1
        #--------노트 위치정보 -------------------------
        self.CenterX = 0.0     #노트 중심 x좌표
        self.CenterY = 0.0
        self.PrevY =735.0


   # def SetImage(self):
     #   if self.image ==None:
       #     self.image = load_image(NOTE.NoteImage[random.randint(0,3)])   #노트 이미지 NoteImage 인덱스중에서 랜덤으로 로딩

    def SetPosition(self, x , y):
        self.CenterX = x
        self.CenterY = y



    def SetSpeed(self):
        pass

    def DelNote(self):
        pass

    def Check_CrushBoard(self):
        if self.CenterY - self.height <=0:
            return True
        else:
            return False

    def update(self):
        self.CenterY = 735 - self.distance


    def draw(self):
        if self.isKeyBox is True:
            if self.isSelect is True:
                self.image.opacify(0.5)
            else:
                self.image.opacify(1)
        else:
            self.image.opacify(1)
        self.image.draw(self.CenterX, self.CenterY, self.width, self.height)


