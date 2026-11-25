from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy
    boy = Boy()

    global grass
    grass = Grass()

    global balls
    balls = [Ball(random.randint(100, 1600-100), 60, 0) for _ in range(30)]


    game_world.add_oject(boy)
    game_world.add_oject(grass, 0)
    game_world.add_objects(balls, 1)

    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)

    # 소년과 공 사이의 충돌 페어를 등록
    game_world.add_collision_pair("boy:ball", boy, None)
    for ball in balls:
        game_world.add_collision_pair("boy:ball", None, ball)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    game_world.handle_collision()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()









