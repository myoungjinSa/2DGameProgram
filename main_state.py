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
file_list =["Text\Shape_of_you_data.txt","Text\meet_on_spring.txt","Text\Blue.txt"]
Key_Status = {0:"SDLK_a",1:"SDLK_s",2:"SDLK_d",3:"SDLK_f",4:"SDLK_RETURN"}
Distance = 0.0
total_time = 0
music_data = None
music = Sound()
sound = None
isStart = False
ShowHitImageFlag =False
gameManager = None
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
#

def enter():
    global board,note_manager,note_list
    global guitar_list,Current_Time
    global music,music_data
    global gameManager
    global spectator
    global file_list
    #-------보드 위치 세팅----------------
    board = Board()
    board.CreateKeyBox()
    #-------노트 생성 매니저 클래스 생성----
    note_manager = NoteManager()
    note_manager.CreateNoteList(310)
    #--------시간 경과-----------
    Current_Time = get_time()
    #---------------------------
    #       기타리스트 객체 생성 후 위치 세팅
    guitar_list = Guitarlist()
    guitar_list.SetPosition(800,100)
    spectator = [Spectator(i) for i in range(0,Spectator.total_count)]


    for i in range(0,Spectator.total_count):
        spectator[i].SetPosition(900,600)

    #-------------------------------------
    #       음악 재생

    readFile = open("Text\SelMusic.txt","r")
    music_Num = json.load(readFile)
    readFile.close()

    music.SetMusic(int(music_Num))              # SOUND.music_list = ["Shape_of_you.mp3","Han_ol_meet_on_spring.mp3","Bol_bbalgan_Blue.mp3"]
    music.SetSoundLength(int(music_Num))
    #-------------------------------------
    #------음악 관련 데이타 불러오기---------
    text_data_file = open(file_list[music_Num],'r')
    music_data = json.load(text_data_file)
    text_data_file.close()

    #------------------------------------
    #------게임 매니저 변수 초기화---------
    gameManager = GameManager()
    gameManager.SetTotalCountZero()

    #-----------------------------------






def exit():
    global music,note_manager,guitar_list,gameManager,board
    del(music)
    del(note_manager)
    del(guitar_list)
    del(gameManager)
    del(board)




def pause():
   pass


def resume():
   pass


def handle_events(frame_time):
    global Key_Status,board,note_manager,music,gameManager,ShowHitImageFlag,total_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key== SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_a):
            board.GiveKeyBoxSelect(0)
            ShowHitImageFlag=note_manager.CheckCrushKeyBox(board, gameManager, 0)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_s):
            board.GiveKeyBoxSelect(1)
            ShowHitImageFlag=note_manager.CheckCrushKeyBox(board, gameManager, 1)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_d):
            board.GiveKeyBoxSelect(2)
            ShowHitImageFlag=note_manager.CheckCrushKeyBox(board, gameManager, 2)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_f):
            board.GiveKeyBoxSelect(3)
            ShowHitImageFlag=note_manager.CheckCrushKeyBox(board, gameManager, 3)

        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_RETURN):
            board.GiveKeyBoxSelect(4)
            ShowHitImageFlag=note_manager.CheckCrushKeyBox(board, gameManager, 4)

        elif event.type == SDL_KEYUP:
            for i in range(0,5):
                board.GiveKeyBoxUnSelect(i, gameManager)
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_q):
            music.StopMusic()


def update(frame_time):
    global music_time,note_manager,note_list,NoteCount,guitar_list,Current_Time
    global music,isStart,gameManager,ShowHitImageFlag,total_time,board,spectator,music_data


    if isStart ==False:                                     #초반 게임이 시작되고 3초정도 딜레이시간을 가진다
        delay(0.1)
        isStart = True
        music.PlayMusic()                                   #1초 정도 딜레이 후 음악 재생
        music.SetTickStart()

    if music_time >=0.0:
        music.SetTickEnd()                                      #끝 시간 체크
        if music.CheckMusicTime() ==True:
            isStart = False
            music_data =None
            music.RemoveMusic()
            max_total=open("Text\max_total.txt",'w')
            max_total.write("[")
            max_total.write(str(gameManager.MaxHitCount()))
            max_total.write(",")
            max_total.write(str(gameManager.GetTotal()))
            max_total.write("]")
            max_total.close()
            gameManager.SetTotalCountZero()
            game_framework.run(GameInfoState)
        else:
            note_manager.NoteDown(frame_time)                     #각 노트의 속도대로 떨어트려라
            note_manager.CheckCrushBoard(board, gameManager)
            hit=gameManager.CheckHitCount()

            for i in range(0,Spectator.total_count):
                spectator[i].SetShowFlagTrue(hit)


            if ShowHitImageFlag ==True:
                total_time =0
            else:
                if total_time >= 200:
                    ShowHitImageFlag = False
                    total_time =0
            total_time += 1


            if music_time %8 ==0:                           #기타리스트 애니메이션 시간 간격
                guitar_list.update()
                for i in range(0,Spectator.total_count):
                    if spectator[i].GetShowFlag() == True:
                        spectator[i].update(board,i,spectator)


            delay(0.01)                   #0.01초 마다
            if isStart == True:
                music_time = music_time + 1



def draw(frame_time):
    global music_time,board,note_manager,guitar_list,Frame_Rate,Frame_Time
    global music_data,gameManager,ShowHitImageFlag,spectator

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
        gameManager.draw(ShowHitImageFlag)



    guitar_list.draw()
    for i in range(0,Spectator.total_count):
        spectator[i].draw()

    for i in range(unselect,select):
        if local_manager[i].isSelect is True:
            local_manager[i].draw()

    update_canvas()
