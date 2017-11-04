from pico2d import *
import random
import main_state

class NOTE:
    NoteImage= ["note_blue.png","note_red.png","note_grey.png","note_pink.png","note_orange.png"]
    def __init__(self):
        self.width = 120        #노트 너비
        self.height = 30        #노트 높이
        self.speed =0           #노트 스피드
        self.isHit = False      #노트 히트 검사 여부 플래그
        self.isSelect = False   #활성화 된 노트 플래그 True = 활성화 False = 비활성화
        #--------노트 이미지 변수-----------------------
        self.image =load_image(NOTE.NoteImage[random.randint(0,3)])
        #--------노트 위치정보 -------------------------
        self.inputX=0.0         #입력 x정보
        self.inputY=0.0         #입력 y정보
        self.LeftTopX = 0.0
        self.LeftTopY = 0.0


   # def SetImage(self):
     #   if self.image ==None:
       #     self.image = load_image(NOTE.NoteImage[random.randint(0,3)])   #노트 이미지 NoteImage 인덱스중에서 랜덤으로 로딩

    def SetPosition(self, x , y):
        self.LeftTopX = x
        self.LeftTopY = y


    def update(self):
        pass

    def SetSpeed(self):
        pass

    def DelNote(self):
        pass


    def draw(self):
        if self.isSelect is True:
            self.image.draw(self.LeftTopX,self.LeftTopY,self.width,self.height)











