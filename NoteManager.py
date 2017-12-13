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
        self.unselectCount = 0
        self.selectElementCount =0

        if NoteManager.noteList ==None:
            NoteManager.noteList = [Note()]                                                    #일반 노트 생성

    def GetNoteList(self):
        return NoteManager.noteList

    def GetSelectElementCount(self):
        return self.selectElementCount


    def GetUnselectElementCount(self):
        return self.unselectCount

    def CreateNoteList(self,count):                                                                 #일반 노트를 생성하고 초기화하는 함수
        if NoteManager.noteList !=None:
            NoteManager.noteList = [Note() for i in range(0, count)]                            #count 만큼 일반노트 생성
            self.maxElementCount = count                                                            #최대 노트 개수를 count 값으로 세팅


    def CheckIsEnd(self):
        if self.selectElementCount>=253:                                                            #273
            return True
        else:
            return False


    def CheckCrushKeyBox(self,board,GameManager,index):
        if board.keybox[index] != None:
            if board.keybox[index].isSelect == True:
                for i in range(self.unselectCount, self.selectElementCount):
                    if self.noteList[i].isSelect ==True  and self.noteList[i].centerY-self.noteList[i].height/2 < board.keybox[index].centerY+self.noteList[i].height/2 +180              \
                    and self.noteList[i].centerX-1 == board.keybox[index].centerX:
                        self.SetElementUnselect(i)
                        self.SetNotePosZero(i)
                        GameManager.HitCount()
                        GameManager.HitTotalCount()
                        CrushFlag =True
                        GameManager.isHit =True
                        return CrushFlag


    def CheckCrushBoard(self,board,GameManager):
        global boolean
        for i in range(self.unselectCount, self.selectElementCount):
            if self.noteList[i].isSelect ==True and self.noteList[i].centerY <= 0:
                self.SetElementUnselect(i)
                self.SetNotePosZero(i)
                GameManager.SetZeroHitCount()
                GameManager.isHit =False





    def SetElementSelect(self):
        NoteManager.noteList[self.selectElementCount].isSelect = True

        self.selectElementCount +=1


    def SetElementUnselect(self,index):
        if NoteManager.noteList[index].isSelect is True:
            NoteManager.noteList[index].isSelect = False
            self.unselectCount+=1


    def SetNotePos(self,Xpos):
        if Xpos >=0 and Xpos<=4:
            NoteManager.noteList[self.selectElementCount].centerX = NoteManager.noteList[self.selectElementCount].width / 2 + (NoteManager.noteList[self.selectElementCount].width) * Xpos   #이미지의 그리는 기준이 중점이기 때문에 0 일경우 노트의 절반만 나오게된다
                                                                                                                                                                    #따라서 노트의 절반을 이동 시킨후 xpos의 값과 노트의 width를 곱해서
                                                                                                                                                                    #노트의 위치를 설정하게 된다.
            NoteManager.noteList[self.selectElementCount].centerY =735                                                                                                    #이미지의 가장 윗점 750 - Note.Height/2(15)  = 735
        elif Xpos == -1:
            NoteManager.noteList[self.selectElementCount].centerX =  -120
            NoteManager.noteList[self.selectElementCount].cetnerY = -30

    def NoteDown(self,frame_Time):
        if self.selectElementCount>=0:
            for i in range(self.unselectCount, self.selectElementCount):
                NoteManager.noteList[i].distance = frame_Time*NoteManager.noteList[i].speed                         # 거리 = 프레임 경과시간 * 각 개별 노드 속도
                NoteManager.noteList[i].centerY = NoteManager.noteList[i].centerY-NoteManager.noteList[i].distance  # 다음 프레임에서의 노드 위치 = 이전 프레임에서의 노드 위치 - 거리

    def GetCurrentNote(self):
        return self.currentIndex



    def SetNotePosZero(self,index):
        NoteManager.noteList[index].centerX =0
        NoteManager.noteList[index].centerY =0
        NoteManager.noteList[index].speed =0
        NoteManager.noteList[index].width = 0
        NoteManager.noteList[index].height = 0
        NoteManager.noteList[index].DelNote()


    def SetNoteSpeed(self,speed):
        NoteManager.noteList[self.selectElementCount].speed = speed                          #현재 활성화된 노트의 스피드값 부여 속도값을 1000으로 설정 0.735초만에 생성되서 끝까지 내려가게됨



