from pico2d import *

CANVAS_WIDTH = 960
CANVAS_HEIGHT = 720
SHEET_HEIGHT = 1024
FRAME_DELAY = 0.08
DISPLAY_HEIGHT = 520

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sprite_sheet = load_image('animation_sprite_sheet.png')

# The first frame is a measured (x, top, width, height) rectangle.
frame = (73, 50, 70, 119)

while True:
	clear_canvas()
	left, top, width, height = frame
	scale = DISPLAY_HEIGHT / height
	sprite_sheet.clip_draw(
		left,
		SHEET_HEIGHT - top - height,
		width,
		height,
		CANVAS_WIDTH // 2,
		CANVAS_HEIGHT // 2,
		int(width * scale),
		DISPLAY_HEIGHT,
	)
	update_canvas()
	delay(FRAME_DELAY)
