from pathlib import Path

import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAME_DELAY = 1 / 60
FRAME_DURATION = 0.1
REST_DURATION = 1.0
DISPLAY_SCALE = 5
SCREEN_MARGIN = 24
MOVEMENT_WRAP_MARGIN = 120
REPETITIONS_PER_ANIMATION = 5
SPRITE_PATH = Path(__file__).with_name("sonic-sprite.png")

FRAME_ROWS = [
    (39, 39, ((1, 29), (31, 56), (58, 85), (86, 115), (118, 147), (150, 179), (182, 210), (211, 239), (240, 268), (270, 293), (302, 330))),
    (79, 39, ((8, 33), (37, 63), (65, 95), (97, 133), (135, 166), (170, 201), (206, 231), (238, 261), (263, 292), (295, 330), (334, 365), (370, 398))),
    (121, 43, ((1, 33), (39, 73), (89, 123), (130, 163), (181, 214), (228, 260))),
    (167, 33, ((1, 29), (35, 63), (67, 96), (98, 128), (131, 159), (162, 190), (193, 222), (230, 260), (268, 297))),
    (206, 27, ((1, 30), (36, 64), (70, 98), (105, 133), (139, 167), (174, 202))),
    (238, 36, ((1, 29), (36, 65), (74, 104), (111, 141), (149, 178), (186, 216))),
    (283, 35, ((1, 29), (36, 65), (72, 110), (123, 161), (172, 210), (218, 255))),
    (327, 44, ((1, 24), (31, 59), (65, 84), (90, 114), (119, 143), (149, 168), (184, 223), (232, 270))),
    (378, 39, ((1, 27), (31, 61), (64, 94), (99, 131), (136, 167), (176, 208), (217, 249), (254, 286))),
    (426, 43, ((6, 39), (49, 82), (96, 118), (125, 147))),
]


def build_frame_row(top, height, horizontal_bounds):
    return [
        (left, top, right - left + 1, height)
        for left, right in horizontal_bounds
    ]


ANIMATIONS = [
    (name, build_frame_row(top, height, bounds), movement_speed)
    for (top, height, bounds), (name, movement_speed) in zip(
        FRAME_ROWS,
        [
            ("걷기", 70),
            ("달리기", 150),
            ("대시", 180),
            ("구르기", 120),
            ("구르기", 120),
            ("달리기", 150),
            ("달리기", 150),
            ("제자리 동작", 0),
            ("표정", 0),
            ("표정", 0),
        ],
    )
]


def draw_frame(sprite_sheet, frame, center_x=WINDOW_WIDTH // 2):
    left, top, width, height = frame
    bottom = sprite_sheet.h - top - height
    scale = min(
        DISPLAY_SCALE,
        (WINDOW_WIDTH - SCREEN_MARGIN * 2) / width,
        (WINDOW_HEIGHT - SCREEN_MARGIN * 2) / height,
    )
    display_width = round(width * scale)
    display_height = round(height * scale)
    sprite_sheet.clip_draw(
        left,
        bottom,
        width,
        height,
        round(center_x),
        WINDOW_HEIGHT // 2,
        display_width,
        display_height,
    )


class AnimationPlayer:
    def __init__(self, animations):
        self.animations = animations
        self.animation_index = 0
        self.frame_index = 0
        self.completed_repetitions = 0
        self.frame_elapsed = 0
        self.is_resting = False
        self.rest_elapsed = 0
        self.position_x = WINDOW_WIDTH / 2

    @property
    def current_frame(self):
        return self.animations[self.animation_index][1][self.frame_index]

    @property
    def current_speed(self):
        return self.animations[self.animation_index][2]

    def update(self, delta_time):
        delta_time = max(0, delta_time)
        if self.is_resting:
            self.rest_elapsed += delta_time
            if self.rest_elapsed + 1e-9 >= REST_DURATION:
                self.rest_elapsed = 0
                self.is_resting = False
                self.animation_index = (self.animation_index + 1) % len(self.animations)
                self.frame_index = 0
                self.completed_repetitions = 0
                self.frame_elapsed = 0
            return

        self.position_x = (
            self.position_x
            + self.current_speed * delta_time
            + MOVEMENT_WRAP_MARGIN
        ) % (WINDOW_WIDTH + MOVEMENT_WRAP_MARGIN * 2) - MOVEMENT_WRAP_MARGIN
        self.frame_elapsed += delta_time
        frames = self.animations[self.animation_index][1]
        while self.frame_elapsed + 1e-9 >= FRAME_DURATION:
            self.frame_elapsed = max(0, self.frame_elapsed - FRAME_DURATION)
            self.frame_index += 1
            if self.frame_index == len(frames):
                self.completed_repetitions += 1
                if self.completed_repetitions >= REPETITIONS_PER_ANIMATION:
                    self.frame_index = len(frames) - 1
                    self.is_resting = True
                    self.rest_elapsed = 0
                    break
                self.frame_index = 0


def handle_events():
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            return False
    return True


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        sprite_sheet = pico2d.load_image(str(SPRITE_PATH))
        player = AnimationPlayer(ANIMATIONS)
        previous_time = pico2d.get_time()
        running = True
        while running:
            running = handle_events()
            current_time = pico2d.get_time()
            player.update(current_time - previous_time)
            previous_time = current_time
            pico2d.clear_canvas()
            draw_frame(sprite_sheet, player.current_frame, player.position_x)
            pico2d.update_canvas()
            pico2d.delay(FRAME_DELAY)
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()