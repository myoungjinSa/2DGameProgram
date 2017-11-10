from pico2d import *
from Note import *
from main_state import *
from Board import *


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
                NoteManager.noteList[i].CenterX =0.0
                NoteManager.noteList[i].CenterY =0.0
                NoteManager.noteList[i].speed = 0


    def CheckCrushKeyBox(self,board,index):
        if board.KeyBox[index] != None:
            if board.KeyBox[index].isSelect == True:
                for i in range(0,self.currentIndex):
                    if self.noteList[i].CenterY-self.noteList[i].height/2 < board.KeyBox[index].CenterY+self.noteList[i].height/2 +50                 \
                    and self.noteList[i].CenterX-1 == board.KeyBox[index].CenterX :
                        self.SetElementUnselect(i)
                        self.SetNotePosZero(i)





    def SetElementSelect(self):
        for i in range(0,self.maxElementCount):
            NoteManager.noteList[i].isSelect = True

        self.SelectElementCount = self.maxElementCount


    def SetElementUnselect(self,index):
        if NoteManager.noteList[index].isSelect is True:
            NoteManager.noteList[index].isSelect = False
            self.SelectElementCount-=1


    def SetNotePos(self,Xpos):
        if Xpos >=0 and Xpos<=4:
            NoteManager.noteList[self.currentIndex].CenterX =NoteManager.noteList[self.currentIndex].width/2+(NoteManager.noteList[self.currentIndex].width)*Xpos   #이미지의 그리는 기준이 중점이기 때문에 0 일경우 노트의 절반만 나오게된다
                                                                                                                                                                    #따라서 노트의 절반을 이동 시킨후 xpos의 값과 노트의 width를 곱해서
                                                                                                                                                                    #노트의 위치를 설정하게 된다.
            NoteManager.noteList[self.currentIndex].CenterY =735                                                                                                    #이미지의 가장 윗점 750 - Note.Height/2(15)  = 735



    def NoteDown(self,):
        if self.currentElementCount>=0:
            for i in range(0,self.currentIndex):
                NoteManager.noteList[i].CenterY -= self.noteList[i].speed             #각 개별 노트의 스피드만큼 떨어짐

    def GetCurrentNote(self):
        return self.currentIndex

    def UpCurrentIndex(self):
        self.currentIndex+=1


    def UpCurrentElementCount(self):
        self.currentElementCount+=1


    def SetNotePosZero(self,index):
        NoteManager.noteList[index].CenterX =0
        NoteManager.noteList[index].CenterY =0
        NoteManager.noteList[index].speed =0
        NoteManager.noteList[index].width = 0
        NoteManager.noteList[index].height = 0


    def SetNoteSpeed(self,speed):
        NoteManager.noteList[self.currentIndex].speed = speed                          #현재 활성화된 노트의 스피드값 부여



