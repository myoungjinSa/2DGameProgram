from pico2d import *
from Note import *
import Board

class NoteManager:
    noteList = None
    def __init__(self):
        self.maxElementCount = 0
        self.currentElementCount =0
        self.currentIndex = 0
        self.SelectElementCount =0
        if NoteManager.noteList ==None:
            NoteManager.noteList = [NOTE(False)]                                                    #일반 노트 생성

    def GetNoteList(self):
        return NoteManager.noteList

    def GetCurrentIndex(self):
        return self.currentIndex

    def CreateNoteList(self,count):                                                                 #일반 노트를 생성하고 초기화하는 함수
        if NoteManager.noteList !=None:
            NoteManager.noteList = [NOTE(False) for i in range(0,count)]                            #count 만큼 일반노트 생성
            self.maxElementCount = count                                                            #최대 노트 개수를 count 값으로 세팅

    def CheckCrushBoard(self):
        for i in range(0,self.maxElementCount):
            if NoteManager.noteList[i].CenterY<=0:               #note의 top이 0이하되면 노트 값 0
                NoteManager.noteList[i].isSelect = False
                NoteManager.noteList[i].height =0
                NoteManager.noteList[i].width =0
                NoteManager.noteList[i].inputX=0.0
                NoteManager.noteList[i].inputY =0.0
                NoteManager.noteList[i].CenterX =0.0
                NoteManager.noteList[i].CenterY =0.0
                NoteManager.noteList[i].speed = 0



    def SetElementSelect(self):
        for i in range(0,self.maxElementCount):
            NoteManager.noteList[i].isSelect = True

        self.SelectElementCount = self.maxElementCount

    def SetNotePos(self):
        NoteManager.noteList[self.currentIndex].inputX=540
        NoteManager.noteList[self.currentIndex].inputY=600
        NoteManager.noteList[self.currentIndex].CenterX = NoteManager.noteList[self.currentIndex].inputX - NoteManager.noteList[self.currentIndex].width
        NoteManager.noteList[self.currentIndex].CenterY = NoteManager.noteList[self.currentIndex].inputY - NoteManager.noteList[self.currentIndex].height

    def NoteDown(self):
        if self.currentElementCount>=0:
            for i in range(0,self.currentIndex):
                NoteManager.noteList[i].CenterY -= self.noteList[i].speed             #각 개별 노트의 스피드만큼 떨어짐

    def UpCurrentIndex(self):
        self.currentIndex+=1


    def UpCurrentElementCount(self):
        self.currentElementCount+=1


    def SetNotePosZero(self):
        pass


    def SetNoteSpeed(self,speed):
        NoteManager.noteList[self.currentIndex].speed = speed                          #현재 활성화된 노트의 스피드값 부여



