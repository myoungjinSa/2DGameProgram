from Sound import *
from gameManager import *
from pico2d import *

import game_framework

name = "Custom"


music = Sound()
file =None
current_Time =0.0
music_interval =0.0
start_time = 0.0
end_Time =0.0
music_length = 0.0
down_Count =0           #space 누르는 카운트 == 노드 개수

def enter():
    global music,file,start_time
    open_canvas(1160,760)
    start_time = float(get_time())
    music.SetMusic(2)
    music.PlayMusic()

    file = open("Text\BolBBalgan_Ctom.txt","w")


def handle_events(frame_time):
    global current_Time,music_interval,music_time,end_Time,music_length,start_time,down_Count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            end_Time = float("%0.2f"%(get_time()))
            down_Count +=1
            music_length = float("%0.2f"%(end_Time)) - float("%0.2f"%(start_time))
            #music_interval = Current_Time - music_time
            file.write(str(down_Count))
            file.write("  ")
            file.write(str(float("%0.2f"%(music_length))))

            file.write("\n")

def exit():
    close_canvas()
    file.close()

def pause():
    pass

def resume():
    pass


def update(frame_time):
    global current_Time
    current_Time = get_time()



def draw(frame_time):
    pass
