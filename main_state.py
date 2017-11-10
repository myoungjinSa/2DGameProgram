from pico2d import *
import game_framework
from NoteManager import *
from Board import *
from GameCharacter import *
from Sound import *
import json



name = "MainState"

board = None
stage = None
music_time =0.0
note_manager = None
NoteCount =False
guitar_list = None
Key_Status = {0:"SDLK_a",1:"SDLK_s",2:"SDLK_d",3:"SDLK_f",4:"SDLK_RETURN"}
Distance = 0.0
Current_Time = 0.0
Frame_Time = 0.0
Frame_Rate = 0.0
music_data = None
music = SOUND()
sound = None
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
    #-------보드 위치 세팅----------------
    board = BOARD()
    board.CreateKeyBox()
    #-------노트 생성 매니저 클래스 생성----
    note_manager = NoteManager()
    note_manager.CreateNoteList(300)
    note_manager.SetElementSelect()
    #--------시간 경과-----------
    Current_Time = get_time()
    #---------------------------
    #       기타리스트 객체 생성 후 위치 세팅
    guitar_list = GuitarList()
    guitar_list.SetPosition(800,100)
    #-------------------------------------
    #       음악 재생
    music.SetMusic("Shape_of_you.mp3")
    music.PlayMusic()
    #-------------------------------------
    #------음악 관련 데이타 불러오기---------
    text_data_file = open("Shape_of_you_data.txt",'r')
    music_data = json.load(text_data_file)
    text_data_file.close()








def exit():
    pass


def pause():
   pass


def resume():
   pass


def handle_events():
    global Key_Status,board,note_manager,music
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_a):
            board.GiveKeyBoxSelect(0)
            note_manager.CheckCrushKeyBox(board,0)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_s):
            board.GiveKeyBoxSelect(1)
            note_manager.CheckCrushKeyBox(board,1)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            board.GiveKeyBoxSelect(2)
            note_manager.CheckCrushKeyBox(board,2)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_f):
            board.GiveKeyBoxSelect(3)
            note_manager.CheckCrushKeyBox(board,3)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            board.GiveKeyBoxSelect(4)
            note_manager.CheckCrushKeyBox(board,4)
        elif event.type == SDL_KEYUP:
            for i in range(0,5):
                board.GiveKeyBoxUnSelect(i)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_q):
            music.StopMusic()


def update():
    global music_time,note_manager,note_list,NoteCount,guitar_list,Current_Time
    Frame_Time = get_time() - Current_Time
    Frame_Rate = 1.0 / Frame_Time
    print("Frame Rate : %f fps,Frame Time : %f sec,"%(Frame_Rate,Frame_Time))

    Current_Time += Frame_Time

    if music_time >=0.0:
        note_manager.NoteDown()                     #각 노트의 속도대로 떨어트려라

    if music_time %8 ==0:                           #기타리스트 애니메이션 시간 간격
        guitar_list.update()

    delay(0.01)                             #0.01초 마다
    music_time = music_time + 1

def draw():
    global music_time,board,note_manager,guitar_list,Frame_Rate,Frame_Time
    global music_data

    #note_Name,Xpos,Speed =(music_data[],music_data[n])
    count = note_manager.GetCurrentIndex()
    if music_time % music_data[str(note_manager.GetCurrentIndex())]["Create_Sec"] == 0.0 :               #0.1초마다
        note_manager.SetNotePos(music_data[str(note_manager.GetCurrentIndex())]["Xpos"])
        note_manager.SetNoteSpeed(music_data[str(note_manager.GetCurrentIndex())]["Speed"])                #노트 속도가 5이면 대략 맨 위에서 맨 아래까지 가는 시간은 2.25초
        note_manager.UpCurrentIndex()
        note_manager.UpCurrentElementCount()
        music_time = 0.0                                                                                #한번 if문에 들어오면 다시 music_time 초기화

    local_manager=note_manager.GetNoteList()
    clear_canvas()
    board.draw(name)
    guitar_list.draw()
    #count = note_manager.GetCurrentIndex()
    print("Frame Rate : %f fps,Frame Time : %f sec," % (Frame_Rate, Frame_Time))
    for i in range(0,count):
        if local_manager[i].isSelect is True:
            local_manager[i].draw()

    update_canvas()
