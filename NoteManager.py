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
            NoteManager.noteList = [NOTE()]

    def GetNoteList(self):
        return NoteManager.noteList

    def GetCurrentIndex(self):
        return self.currentIndex

    def CreateNoteList(self,count):
        if NoteManager.noteList !=None:
            NoteManager.noteList = [NOTE() for i in range(0,count)]
            self.maxElementCount = count

    def CheckCrushBoard(self):
        for i in range(0,self.maxElementCount):
            if NoteManager.noteList[i].LeftTopY<=0:               #note의 top이 0이하되면 노트 값 0
                NoteManager.noteList[i].isSelect = False
                NoteManager.noteList[i].height =0
                NoteManager.noteList[i].width =0
                NoteManager.noteList[i].inputX=0.0
                NoteManager.noteList[i].inputY =0.0
                NoteManager.noteList[i].LeftTopX =0.0
                NoteManager.noteList[i].LeftTopY =0.0
                NoteManager.noteList[i].speed =0



    def SetElementSelect(self):
        for i in range(0,self.maxElementCount):
            NoteManager.noteList[i].isSelect = True

        self.SelectElementCount = self.maxElementCount

    def SetNotePos(self):
        NoteManager.noteList[self.currentIndex].inputX=500
        NoteManager.noteList[self.currentIndex].inputY=600
        NoteManager.noteList[self.currentIndex].LeftTopX = NoteManager.noteList[self.currentIndex].inputX - NoteManager.noteList[self.currentIndex].width
        NoteManager.noteList[self.currentIndex].LeftTopY = NoteManager.noteList[self.currentIndex].inputY - NoteManager.noteList[self.currentIndex].height

    def NoteDown(self):
        if self.currentElementCount>=0:
            for i in range(0,self.currentIndex):
                NoteManager.noteList[i].LeftTopY -= self.noteList[i].speed             #각 개별 노트의 스피드만큼 떨어짐

    def UpCurrentIndex(self):
        self.currentIndex+=1


    def UpCurrentElementCount(self):
        self.currentElementCount+=1


    def SetNotePosZero(self):
        pass


    def SetNoteSpeed(self,speed):
        NoteManager.noteList[self.currentIndex].speed = speed                          #현재 활성화된 노트의 스피드값 부여



