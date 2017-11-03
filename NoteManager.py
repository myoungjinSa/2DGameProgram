from pico2d import *
from Note import *
import Board

class NoteManager:
    def __init__(self):
        self.maxElementCount = 0
        self.currentElementCount =0
        self.currentIndex = 0
        self.SelectElementCount =0
        self.noteList = [NOTE()]

    def GetNoteList(self):
        return self.noteList

    def GetCurrentIndex(self):
        return self.currentIndex

    def CreateNoteList(self,count):
        if self.noteList !=None:
            self.noteList = [NOTE() for i in range(0,count)]
            self.maxElementCount = count

    def SetElementSelect(self):
        for i in range(0,self.maxElementCount):
            self.noteList[i].isSelect = True

        self.SelectElementCount = self.maxElementCount

    def SetNotePos(self):
        self.noteList[self.currentIndex].LeftTopX=50
        self.noteList[self.currentIndex].LeftTopY=520

    def NoteDown(self):
        if self.currentElementCount>=0:
            for i in range(0,self.currentIndex):
                self.noteList[i].LeftTopY += self.noteList[i].speed             #각 개별 노트의 스피드만큼 떨어짐

    def UpCurrentIndex(self):
        self.currentIndex+=1


    def UpCurrentElementCount(self):
        self.currentElementCount+=1


    def SetNotePosZero(self):
        pass


    def SetNoteSpeed(self,speed):
        self.noteList[self.currentIndex].speed = speed                          #현재 활성화된 노트의 스피드값 부여



