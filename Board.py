import pico2d

class Board:
    def __init__(self):
        self.boardImage = pico2d.load_image('Board.bmp')   #보드판의 이미지 추가
        self.StageImage = pico2d.load_image('stage_bitmap.bmp') #스테이지 이미지 추가
        self.BoardPosX, self.BoardPosY = 300, 400 #보드판이 그려질 위치
        self.BoardSize.x, self.BoardSize.y = 600, 761 #보드판의 사이즈
        self.StagePosX,self.StagePosY = 900,400 #스테이지 위치
        self.StageSizeX,self.StageSizeY = 584,761 #스테이지 이미지 사이즈

    def update(self):
        pass


    def draw(self):
        pico2d.Font()

