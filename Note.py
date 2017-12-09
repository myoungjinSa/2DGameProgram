from pico2d import *
import random


class Note:
    NoteImage= ["Resource\Blue_note.png","Resource\Red_note.png","Resource\Grass_note.png","Resource\Pink_note.png","Resource\Orange_note.png"]
    def __init__(self):
        self.width = 120        #노트 너비
        self.height = 30        #노트 높이
        self.speed = 0           #노트 스피드
        self.isHit = False      #노트 히트 검사 여부 플래그
        self.isSelect = False   #활성화 된 노트 플래그 True = 활성화 False = 비활성화
        self.distance = 0.0
        #--------노트 이미지 변수-----------------------

        self.image =load_image(Note.NoteImage[random.randint(0, 4)])         #image에 NoteImage 인덱스 0~3중 랜덤으로 이미지 삽입

        #--------노트 위치정보 -------------------------
        self.CenterX = 0.0     #노트 중심 x좌표
        self.CenterY = 0.0
        self.PrevY =735.0


    def SetPosition(self, x , y):
        self.CenterX = x
        self.CenterY = y



    def SetSpeed(self):
        pass

    def DelNote(self):
        del(self)

    def Check_CrushBoard(self):
        if self.CenterY - self.height <=0:
            return True
        else:
            return False

    def update(self):
        self.CenterY = 735 - self.distance


    def draw(self):
        self.image.draw(self.CenterX, self.CenterY, self.width, self.height)



class Keybox:
    keybox_number =0
    KeyBoxImage = {0: 'Resource\keyBox_Dark.png', 1: 'Resource\keyBox_Green.png', 2: 'Resource\keyBox_HotPink.png', 3: 'Resource\keyBox_Sand.png',4: 'Resource\keyBox_Sea.png'}
    KEYBOX_WIDTH = 120
    KEYBOX_HEIGHT = 30
    def __init__(self):
        self.image = load_image(Keybox.KeyBoxImage[Keybox.keybox_number % 5])  # image에 KeyBoxImage 인덱스 5개를 인덱스 값을 증가시키며 나머지 연산으로 삽입
        self.width = Keybox.KEYBOX_WIDTH  # 노트 너비
        self.height = Keybox.KEYBOX_HEIGHT  # 노트 높이
        self.isHit = False  # 노트 히트 검사 여부 플래그
        self.isSelect = False  # 활성화 된 노트 플래그 True = 활성화 False = 비활성화
        Keybox.keybox_number += 1

    def SetPosition(self, x , y):
        self.CenterX = x
        self.CenterY = y


    def GetWidth(self):
        return self.width


    def draw(self):
        if self.isSelect is True:
            self.image.opacify(0.5)
        else:
            self.image.opacify(1)

        self.image.draw(self.CenterX, self.CenterY, self.width, self.height)