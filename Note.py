from pico2d import *
import random


class NOTE:
    NoteImage= ["note_blue.png","note_red.png","note_grey.png","note_pink.png","note_orange.png"]
    def __init__(self):
        self.width = 120        #노트 너비
        self.height = 30        #노트 높이
        self.speed =0           #노트 스피드
        self.isHit = False      #노트 히트 검사 여부 플래그
        self.isSelect = False   #활성화 된 노트 플래그 True = 활성화 False = 비활성화
        #--------노트 이미지 변수-----------------------
        self.image =None
        #--------노트 위치정보 -------------------------
        self.LeftTopX = 20      #노트 왼쪽 x 좌표
        self.LeftTopY =300     #노트 왼쪽 y 좌표
        self.RightBottomX=self.LeftTopX + self.width #노트 오른쪽 아래 좌표
        self.RightBottomY = self.LeftTopY+self.height

    def SetImage(self):
        if self.image ==None:
            self.image = load_image(NOTE.NoteImage[random.randint(0,3)])   #노트 이미지 NoteImage 인덱스중에서 랜덤으로 로딩

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
        if self.isSelect == True:
            self.image.draw(self.LeftTopX,self.LeftTopY,self.width,self.height)











