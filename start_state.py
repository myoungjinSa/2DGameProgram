import game_framework
from pico2d import *
import main_state
import Font
import Board
import MusicSelState



name = "StartState"

image = None
logo_time = 0.0
count = 10
fonts = ["Resource\p.png","Resource\L.png","Resource\A.png","Resource\Y_two.png","Resource\W_small.png","Resource\I_small.png","Resource\T.png","Resource\H.png","Resource\R.png",
         "Resource\Y_small.png","Resource\T_small.png","Resource\H_small.png","Resource\M.png"]
StartFont = Font.FONT()
font = [Font.FONT() for i in range(Font.FONT.count)]
mouseDown = False
Font.mouseOnGameStart =False
board = None

def SetPosition(font,startFont,x,y):
    font[0].SetFontPos(x, y)  # P 위치 세팅
    font[1].SetFontPos(x+30,y)    # L 위치 세팅
    font[2].SetFontPos(x+60,y)         # A 위치 세팅
    font[3].SetFontPos(x+90, y)  # Y 위치 세팅
    font[4].SetFontPos(x+130,y)         # W 위치 세팅
    font[5].SetFontPos(x+160,y)         # I 위치 세팅
    font[6].SetFontPos(x+190,y)         # T 위치 세팅
    font[7].SetFontPos(x+220,y)         # H 위치 세팅
    font[8].SetFontPos(x+260,y)         # R 위치 세팅
    font[9].SetFontPos(x+290,y)         # y 위치 세팅
    font[10].SetFontPos(x+320,y)         # t 위치 세팅
    font[11].SetFontPos(x+350,y)         # h 위치 세팅
    font[12].SetFontPos(x+380,y)         # M 위치 세팅

    startFont.SetFontPos(270,150)


def enter():
    global image,font,board,name
    open_canvas(1160,750)
    #board.boardImage = load_image('Board.png')
    #image = [load_image('Board.png'),load_image("stage_bitmap.png")]
    j =0
    for i in fonts:
        font[j].SetImage(i)                 #폰트 이미지 세팅
        font[j].SetFontWH(30,30)            #폰트 크기  60,30 세팅
        j+=1
    board = Board.Board()
    StartFont.SetImage("Resource\GameStart.png")     #게임시작 폰트 이미지 불러오기
    StartFont.SetFontWH(200,60)              #게임시작 폰트 크기 세팅
    SetPosition(font,StartFont,100,580)




def exit():
    global image,fonts,font,board
    del (image)
    del(fonts)
    del(font)
    del(board)

    close_canvas()



def update(frame_time):
    global mouseDown

    if mouseDown == True:
       # game_framework.quit()
        game_framework.run(MusicSelState)

    delay(0.01)

    for i in range(13):
        font[i].update()


def draw(frame_time):
    global image,font,StartFont,board,name
    board.draw()

    #image[0].draw(300,350)
    #image[1].draw(890,350)
    for i in range(13):
        font[i].draw()


    StartFont.draw()
    update_canvas()





def handle_events(frame_event):
    global mouseDown
    events = get_events()
    for event in events:
        if event.type==SDL_MOUSEBUTTONDOWN:
            x,y = event.x,729-event.y
            if x>120 and x <390 and y>115 and y<185:
                mouseDown = True
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x ,729-event.y
            if x > 120 and x < 390 and y > 115 and y < 185:
                Font.mouseOnGameStart = True
            else:
                Font.mouseOnGameStart = False

        elif event.type == SDL_QUIT:
            game_framework.quit()




def pause(): pass


def resume(): pass




