from config import GameConfig
from error import GameOver
from snake import Snake
from game import Game
from renderer import Renderer

from collections import deque
import msvcrt
import time
import os


class FrequencyController(object):
    '''fps controller'''
    def __init__(self, fps: float | int) -> None:
        self.fps = fps
        self.interval = 1.0 / fps
        self.last_exec = time.perf_counter() - self.interval
        self.realtime_fps = fps
    
    def should_execute(self) -> bool:
        now = time.perf_counter()
        interval = now - self.last_exec
        if interval >= self.interval:
            self.realtime_fps = 1 / max(interval, 0)
            self.last_exec = now
            return True
        return False
    
    # def __str__(self) -> str:
    #     return f'realtime_fps={self.realtime_fps:.2f}'


def main() -> None:
    controller_keyboard = FrequencyController(GameConfig.KEYBOARD_INPUT_FPS)
    controller_render   = FrequencyController(GameConfig.RENDER_FPS)
    time_history = deque(maxlen=GameConfig.TIME_HISTORY_LEN) # type: deque

    snake    = Snake(GameConfig.SNAKE_INIT_POS)
    game     = Game(GameConfig.GAME_MAP_SHAPE, snake)
    renderer = Renderer(game)

    os.system('cls')

    print(renderer.render())
    print(GameConfig.GAME_GUIDE)
    print('press any key to start ...')

    key = msvcrt.getch()
    snake.answer_key(key)
    
    while True:
        loop_start = time.perf_counter()

        if controller_keyboard.should_execute():
            if msvcrt.kbhit():
                key = msvcrt.getch()
                snake.answer_key(key)
        
        if controller_render.should_execute():
            try:
                game.tick(forward=True)
                rendered_text = renderer.render()
                os.system('cls')
                print(rendered_text)
            except GameOver as game_over:
                print(game_over)
                return
            # print(controller_keyboard)
            # print(controller_render)
        
        elapsed = time.perf_counter() - loop_start
        time_history.append(elapsed)
        avg_time = sum(time_history) / len(time_history) if time_history else 0
        
        sleep_time = max(0, controller_keyboard.interval - avg_time)
        time.sleep(sleep_time)


# if __name__ == '__main__':
#     main()
main()