import pico2d

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def handle_events():
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            return False
    return True


def main():
    pico2d.open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        running = True
        while running:
            running = handle_events()
    finally:
        pico2d.close_canvas()


if __name__ == "__main__":
    main()