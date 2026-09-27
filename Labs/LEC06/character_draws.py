# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x,y)
    pass

def move_top():
    for y in range(100, 501, 5):
        draw_character(700, y)
    pass

def move_left():
    for x in range(700, 99, -5):
            draw_character(x, 500)
    pass

def move_bottom():
    for y in range(500, 99, -5):
            draw_character(100, y)
    pass

def move_right():
    for x in range(100, 701, 5):
                draw_character(x, 100)
    pass

def move_rectangle():
    move_top()
    move_left()
    move_bottom()
    move_right()
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    #move_circle()
    move_rectangle()
    #move_triangle()

close_canvas()