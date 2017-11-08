from pico2d import *
import game_framework
from NoteManager import *
from Board import *
from GameCharacter import *


name = "MainState"

board = None
stage = None
music_time =0.0
note_manager = None
NoteCount =False
guitar_list = None
Key_Status = {0:"SDLK_a",1:"SDLK_s",2:"SDLK_d",3:"SDLK_f",4:"SDLK_RETURN"}

def enter():
    global board,note_manager,note_list,guitar_list
    board = BOARD()
    board.CreateKeyBox()
    note_manager = NoteManager()
    note_manager.CreateNoteList(300)
    note_manager.SetElementSelect()
    guitar_list = GuitarList()
    guitar_list.SetPosition(800,100)





def exit():
    pass


def pause():
   pass


def resume():
   pass


def handle_events():
    global Key_Status,board,note_manager
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


def update():
    global music_time,note_manager,note_list,NoteCount,guitar_list


    if music_time >=0.0:
        note_manager.NoteDown()

    if music_time %8 ==0:                           #기타리스트 애니메이션 시간 간격
        guitar_list.update()


    delay(0.01)                             #0.01초 마다
    music_time = music_time + 1

def draw():
    global music_time,board,note_manager,guitar_list

    if music_time %100 == 0 :               #1초마다
        note_manager.SetNotePos(3)
        note_manager.SetNoteSpeed(5)
        note_manager.UpCurrentIndex()
        note_manager.UpCurrentElementCount()

    local_manager=note_manager.GetNoteList()
    clear_canvas()
    board.draw(name)
    guitar_list.draw()
    count = note_manager.GetCurrentIndex()
    for i in range(0,count):
        if local_manager[i].isSelect is True:
            local_manager[i].draw()

    update_canvas()
