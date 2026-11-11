from pico2d import *
import game_framework
import game_world

pause_font = None


def init():
    global pause_font
    pause_font = load_font('..\\LEC16_Time\\ENCR10B.TTF', 36)


def finish():
    global pause_font
    del pause_font


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    pause_font.draw(320, 300, 'PAUSED', (255, 255, 0))
    update_canvas()
