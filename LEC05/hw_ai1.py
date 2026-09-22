from pico2d import *


open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 경로의 네 꼭짓점 (왼쪽 아래 시작, 시계 방향: 오른쪽 → 위 → 왼쪽 → 아래)
LEFT_BOTTOM = (150, 150)
RIGHT_BOTTOM = (650, 150)
RIGHT_TOP = (650, 450)
LEFT_TOP = (150, 450)

# 현재 좌표와 이동 방향 상태
x, y = LEFT_BOTTOM
direction = 'right'   # 'right' | 'up' | 'left' | 'down'
SPEED = 4

while True:
    # 이동 방향 상태에 따라 x, y 변화량 결정
    if direction == 'right':
        dx, dy = SPEED, 0
    elif direction == 'up':
        dx, dy = 0, SPEED
    elif direction == 'left':
        dx, dy = -SPEED, 0
    else:  # 'down'
        dx, dy = 0, -SPEED

    x += dx
    y += dy

    # 꼭짓점에 도달하면 다음 변으로 이동 방향 변경
    if direction == 'right' and x >= RIGHT_BOTTOM[0]:
        x, y = RIGHT_BOTTOM
        direction = 'up'
    elif direction == 'up' and y >= RIGHT_TOP[1]:
        x, y = RIGHT_TOP
        direction = 'left'
    elif direction == 'left' and x <= LEFT_TOP[0]:
        x, y = LEFT_TOP
        direction = 'down'
    elif direction == 'down' and y <= LEFT_BOTTOM[1]:
        x, y = LEFT_BOTTOM   # 한 바퀴 완료, 시작 위치로 이어져 반복
        direction = 'right'

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

close_canvas()