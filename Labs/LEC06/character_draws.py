# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()

def move_circle():
    theta = math.radians(360)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    pass

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()