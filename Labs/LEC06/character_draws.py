# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')
grass = load_image('grass.png')

def draw_character(x,y):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,y)
    update_canvas()
    delay(0.01)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x,y)

def move_top():
    for y in range(100, 501, 5):
        draw_character(700, y)

def move_left():
    for x in range(700, 99, -5):
            draw_character(x, 500)

def move_bottom():
    for y in range(500, 99, -5):
            draw_character(100, y)

def move_right():
    for x in range(100, 701, 5):
                draw_character(x, 100)

def move_rectangle():
    move_top()
    move_left()
    move_bottom()
    move_right()

def move_lefttop():
    y = 100
    for x in range(700, 399, -3):
         y += 4
         draw_character(x,y)

def move_leftbottom():
    y = 500
    for x in range(400, 99, -3):
             y -= 4
             draw_character(x,y)

def move_triangle():
    move_lefttop()
    move_leftbottom()
    move_right()

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()