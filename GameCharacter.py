from pico2d import *
import json

class GuitarList:
    Guitar_Image_List = ["Guitar_Boy_One.png","Guitar_Boy_Two.png","Guitar_Boy_Three.png","Guitar_Boy_Four.png","Guitar_Boy_Five.png","Guitar_Boy_Six.png"]
    Animate_Index =0
    def __init__(self):
        self.positionX,self.positionY =0.0 , 0.0
        self.width = 99
        self.height= 87
        self.image = [load_image(GuitarList.Guitar_Image_List[i]) for i in range(0,6)]

    def SetPosition(self,x,y):
        self.positionX = x
        self.positionY = y



    def GetGuitarListPositionY(self):
        return self.positionY


    def GetGuitarListPositionX(self):
        return self.positionX


    def update(self):
        GuitarList.Animate_Index +=1
    def draw(self):
        self.image[GuitarList.Animate_Index%6].draw(self.positionX,self.positionY,self.width,self.height)



class Spectator:
    Spectator_Image_list =[("Boy_front_1.png","Boy_front_2.png","Boy_front_3.png"),("Boy2_front_1.png","Boy2_front_2.png","Boy2_front_2.png"),
                           ("Boy3_front_1.png","Boy3_front_2.png","Boy3_front_3.png"),("Boy4_front_1.png","Boy4_front_2.png","Boy4_front_3.png"),
                           ("Boy5_front_1.png","Boy5_front_2.png","Boy5_front_3.png"),("Boy6_front_1.png","Boy6_front_2.png","Boy6_front_3.png"),
                           ("Boy7_front_1.png","Boy7_front_2.png","Boy7_front_3.png")]

    total_count = 7

    def __init__(self,index):
        self.positionX,self.positionY =0.0 , 0.0
        self.Frame = 0
        self.width = 63
        self.height= 68
        self.index = index
        self.image = [load_image(Spectator.Spectator_Image_list[index][i]) for i in range(0,3)]
        self.isShow = False


    def SetPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def GetPositionX(self):
        return self.positionX

    def GetPositionY(self):
        return self.positionY


    def MovePosition(self,board,index,spectator):
        if self.isShow is True:
            if index==0:
                if self.CmpPositionX(board.BoardPosX+board.BoardWidth/2)==True:
                    self.positionX -=5

                if self.CmpPositionY(200) == True:
                    self.positionY -= 5

            if index==1 or index==2 or index ==3 or index ==4 or index ==5 or index ==6:
                if self.CmpPositionX(spectator[index-1].GetPositionX())==True:
                    self.positionX-=5
                else:
                    self.positionX+=5

                if self.CmpPositionY(200)==True:
                    self.positionY -=5



    def CmpPositionX(self,Xpos):
        if self.positionX-self.width > Xpos:
            return True
        else:
            return False

    def CmpPositionY(self,Ypos):
        if self.positionY > Ypos:
            return True
        else:
            return False

    def SetShowFlagTrue(self,hit):
        if self.index ==0:
            if hit >5:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==1:
            if hit > 10:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==2:
            if hit >11:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==3:
            if hit >15:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==4:
            if hit >16:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==5:
            if hit>17:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==6:
            if hit>19:
                if self.isShow is False:
                    self.isShow = True



    def GetShowFlag(self):
        return self.isShow


    def update(self,board,index,spectator):
        self.MovePosition(board,index,spectator)
        self.Frame +=  1


    def draw(self):
        if self.isShow == True:
            self.image[self.Frame%2].draw(self.positionX,self.positionY,self.width,self.height)
        else:
            pass