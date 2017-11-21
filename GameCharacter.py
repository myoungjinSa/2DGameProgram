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

    total_count = 40

    def __init__(self,index):
        self.positionX,self.positionY =0.0 , 0.0
        self.Frame = 0
        self.width = 63
        self.height= 68
        self.index = index
        self.image = [load_image(Spectator.Spectator_Image_list[index%7][i]) for i in range(0,3)]
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
            if index==0 or index ==8 or index == 16 or index ==24 or index ==32:
                if self.CmpPositionX(board.BoardPosX+board.BoardWidth/2)==True:
                    self.positionX -=5

                if index is 0:
                    if self.CmpPositionY(200) == True:
                        self.positionY -= 5

                if index is 8:
                    if self.CmpPositionY(260) == True:
                        self.positionY -=5

                if index is 16:
                    if self.CmpPositionY(320) ==True:
                        self.positionY -=5

                if index is 24:
                    if self.CmpPositionY(380) ==True:
                        self.positionY -=5

                if index is 32:
                    if self.CmpPositionY(440) ==True:
                        self.positionY -=5

                if index is 39:
                    if self.CmpPositionY(500) ==True:
                        self.positionY -=5

            if index !=0 and index != 8 and index != 16 and index != 24 and index != 32 and index !=40:
                if self.CmpPositionX(spectator[index-1].GetPositionX())==True:
                    self.positionX-=5
                else:
                    self.positionX+=5

                if index >=1 and index <=7:
                    if self.CmpPositionY(200)==True:
                        self.positionY -=5

                if index >= 9 and index <= 15 :
                    if self.CmpPositionY(260) == True:
                        self.positionY -=5
                if index >= 17 and index <=23:
                    if self.CmpPositionY(320) == True:
                        self.positionY -= 5

                if index >=25 and index <=31:
                    if self.CmpPositionY(380) == True:
                        self.positionY -=5

                if index >=33 and index <=39:
                    if self.CmpPositionY(440) == True:
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
            if hit >self.index:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==1:
            if hit > 5:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==2:
            if hit >8:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==3:
            if hit >10:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==4:
            if hit >12:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==5:
            if hit>16:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==6:
            if hit>17:
                if self.isShow is False:
                    self.isShow = True

        if self.index == 7:
            if hit > 19:
                if self.isShow is False:
                    self.isShow = True

        if self.index == 8:
            if hit>20:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 9:
            if hit>22:
                if self.isShow is False:
                    self.isShow = True

        if self.index == 10:
            if hit>24:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==11:
            if hit>26:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==12:
            if hit>29:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==13:
            if hit>32:
                if self.isShow is False:
                    self.isShow = True
        if self.index ==14:
            if hit>35:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==15:
            if hit >37:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==16:
            if hit >38:
                if self.isShow is False:
                    self.isShow = True
        if self.index ==17:
            if hit >40:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==18:
            if hit >42:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==19:
            if hit >44:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==20:
            if hit >46:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==21:
            if hit >48:
                if self.isShow is False:
                    self.isShow = True


        if self.index ==22:
            if hit >50:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==23:
            if hit >52:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==24:
            if hit >54:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==25:
            if hit >56:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==26:
            if hit >58:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==27:
            if hit >60:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==28:
            if hit >62:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==29:
            if hit >64:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==30:
            if hit >66:
                if self.isShow is False:
                    self.isShow = True

        if self.index ==31:
            if hit >68:
                if self.isShow is False:
                    self.isShow = True

        if self.index == 32:
            if hit > 70:
                if self.isShow is False:
                    self.isShow = True

        if self.index == 33:
            if hit > 72:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 34:
            if hit > 74:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 35:
            if hit > 76:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 36:
            if hit > 80:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 37:
            if hit > 82:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 38:
            if hit > 85:
                if self.isShow is False:
                    self.isShow =True

        if self.index == 39:
            if hit > 88:
                if self.isShow is False:
                    self.isShow =True

        if self.index ==40:
            if hit>90:
                if self.isShow is False:
                    self.isShow =True

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