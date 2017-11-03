from pico2d import *

class Board:
    boardImage = None
    stageImage = None
    def __init__(self):
        self.BoardPosX, self.BoardPosY = 300, 370 #보드판이 그려질 위치
        self.BoardWidth, self.BoardHeight = 600, 761 #보드판의 사이즈
        self.StagePosX,self.StagePosY = 880,370 #스테이지 위치
        self.StageSizeX,self.StageSizeY = 561,761 #스테이지 이미지 사이즈
        self.BoardLeftTopX = self.BoardPosX-300
        self.BoardLeftTopY = self.BoardPosY-370
        if Board.boardImage == None and Board.stageImage ==None:
            Board.boardImage = load_image('board.png')
            Board.stageImage = load_image('stage_bitmap.png')

    def update(self):
        pass


    def draw(self):
        self.boardImage.draw(self.BoardPosX,self.BoardPosY,self.BoardWidth,self.BoardHeight)
        self.stageImage.draw(self.StagePosX,self.StagePosY,self.StageSizeX,self.StageSizeY)

