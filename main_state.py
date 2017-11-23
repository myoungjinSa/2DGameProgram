from pico2d import *
import game_framework
from NoteManager import *
from Board import *
from GameCharacter import *
from Sound import *
from gameManager import  *
from GameInfoState import *
import GameInfoState
import json



name = "MainState"

board = None
stage = None
music_time =0.0
note_manager = None
NoteCount =False
guitar_list = None
spectator =None
Key_Status = {0:"SDLK_a",1:"SDLK_s",2:"SDLK_d",3:"SDLK_f",4:"SDLK_RETURN"}
Distance = 0.0
Current_Time = 0.0
Frame_Time = 0.0
Frame_Rate = 0.0
music_data = None
music = SOUND()
sound = None
isStart = False
boolean =False
GM = None
#-----------------------------------------
#               시간
#보드의 세로 높이는     750
#일단 노트의 세로 두께는 30
#FramePerSec = 1/Frame_Time
#거리 = 경과시간 * 속도
#위치 = 초기위치 + 거리
#다음 프레임 x = 현재 프레임 x + (객체의 속도 * 경과시간)
#내가 구현해야 될것은
#-----------------------------------------


def enter():
    global board,note_manager,note_list
    global guitar_list,Current_Time
    global music,music_data
    global GM
    global spectator
    #-------보드 위치 세팅----------------
    board = BOARD()
    board.CreateKeyBox()
    #-------노트 생성 매니저 클래스 생성----
    note_manager = NoteManager()
    note_manager.CreateNoteList(310)
    #--------시간 경과-----------
    Current_Time = get_time()
    #---------------------------
    #       기타리스트 객체 생성 후 위치 세팅
    guitar_list = GuitarList()
    guitar_list.SetPosition(800,100)
    spectator = [Spectator(i) for i in range(0,Spectator.total_count)]


    for i in range(0,Spectator.total_count):
        spectator[i].SetPosition(900,600)

    #-------------------------------------
    #       음악 재생
    music.SetMusic("Shape_of_you.mp3")
    #-------------------------------------
    #------음악 관련 데이타 불러오기---------
    text_data_file = open("Shape_of_you_data.txt",'r')
    music_data = json.load(text_data_file)
    text_data_file.close()

    #------------------------------------
    #------게임 매니저 변수 초기화---------
    GM = GameManager()

    #-----------------------------------






def exit():
    global music,note_manager,guitar_list,GM,board
    del(music)
    del(note_manager)
    del(guitar_list)
    del(GM)
    del(board)



def pause():
   pass


def resume():
   pass


def handle_events():
    global Key_Status,board,note_manager,music,GM,boolean
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_a):
            board.GiveKeyBoxSelect(0)
            boolean=note_manager.CheckCrushKeyBox(board,GM,0)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_s):
            board.GiveKeyBoxSelect(1)
            boolean=note_manager.CheckCrushKeyBox(board,GM,1)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            board.GiveKeyBoxSelect(2)
            boolean=note_manager.CheckCrushKeyBox(board,GM,2)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_f):
            board.GiveKeyBoxSelect(3)
            boolean=note_manager.CheckCrushKeyBox(board,GM,3)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            board.GiveKeyBoxSelect(4)
            boolean=note_manager.CheckCrushKeyBox(board,GM,4)

        elif event.type == SDL_KEYUP:
            for i in range(0,5):
                board.GiveKeyBoxUnSelect(i,GM)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_q):
            music.StopMusic()

total_time=0
def update():
    global music_time,note_manager,note_list,NoteCount,guitar_list,Current_Time
    global music,isStart,GM,boolean,total_time,board,spectator,music_data
    Frame_Time = get_time() - Current_Time
    Frame_Rate = 1.0 / Frame_Time
    print("Frame Rate : %f fps,Frame Time : %f sec,"%(Frame_Rate,Frame_Time))

    if isStart ==False:                                     #초반 게임이 시작되고 3초정도 딜레이시간을 가진다
        music_time +=1

        delay(0.1)
        isStart = True
        music.PlayMusic()                                   #3초 정도 딜레이 후 음악 재생


    if music_time >=0.0:
        if note_manager.CheckIsEnd() ==True:
            isStart = False
            music_data =None
            music.RemoveMusic()
            max_total=open("max_total.txt",'w')
            max_total.write("[")
            max_total.write(str(GM.MaxHitCount()))
            max_total.write(",")
            max_total.write(str(GM.GetTotal()))
            max_total.write("]")
            max_total.close()
            game_framework.run(GameInfoState)
        else:
            note_manager.NoteDown(Frame_Time)                     #각 노트의 속도대로 떨어트려라
            note_manager.CheckCrushBoard(board,GM)
            hit=GM.CheckHitCount()

            for i in range(0,Spectator.total_count):
                spectator[i].SetShowFlagTrue(hit)


            if boolean ==True:
                total_time =0
            else:
                if total_time >= 200:
                    boolean = False
                    total_time =0
            total_time += 1


            if music_time %8 ==0:                           #기타리스트 애니메이션 시간 간격
                guitar_list.update()
                for i in range(0,Spectator.total_count):
                    if spectator[i].GetShowFlag() == True:
                        spectator[i].update(board,i,spectator)

            delay(0.01)                   #0.01초 마다
            Current_Time += Frame_Time
            if isStart == True:
                music_time = music_time + 1



def draw():
    global music_time,board,note_manager,guitar_list,Frame_Rate,Frame_Time
    global music_data,GM,boolean,spectator

    select = note_manager.GetSelectElementCount()
    unselect = note_manager.GetUnselectElementCount()
    if isStart is True:

        if music_time % music_data[str(note_manager.GetSelectElementCount())]["Create_Sec"] == 0.0 :              #0.1초마다
            note_manager.SetNotePos(music_data[str(note_manager.GetSelectElementCount())]["Xpos"])
            note_manager.SetNoteSpeed(music_data[str(note_manager.GetSelectElementCount())]["Speed"])             #노트 속도가 5이면 대략 맨 위에서 맨 아래까지 가는 시간은 2.25초
            note_manager.SetElementSelect()
            music_time = 0.0                                                                                        #한번 if문에 들어오면 다시 music_time 초기화


    local_manager=note_manager.GetNoteList()
    clear_canvas()
    board.draw()
    if isStart == True:
        GM.draw(boolean)



    guitar_list.draw()
    for i in range(0,Spectator.total_count):
        spectator[i].draw()
    #print("Frame Rate : %f fps,Frame Time : %f sec," % (Frame_Rate, Frame_Time))
    for i in range(unselect,select):
        if local_manager[i].isSelect is True:
            local_manager[i].draw()

    update_canvas()
