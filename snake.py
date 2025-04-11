from typing import Tuple
from config import GameConfig

from collections import deque
                
class Snake(object):
    def __init__(self, init_pos: Tuple[int, int] = GameConfig.SNAKE_INIT_POS, init_facing: int = GameConfig.SNAKE_INIT_FACING, init_len: int = GameConfig.SNAKE_INIT_LEN) -> None:
        self.snake = deque([init_facing] * init_len, maxlen=init_len)
        self.tail_pos = init_pos
        self.facing = init_facing
        # self.length = init_len
        
        self.lengthening = False
    
    # def __len__(self) -> int:
    #     return self.length

    def __map_facing(self, facing: int) -> int:
        match facing:
            case GameConfig.LEFT:
                return GameConfig.RIGHT
            case GameConfig.RIGHT:
                return GameConfig.LEFT
            case GameConfig.DOWN:
                return GameConfig.UP
            case GameConfig.UP:
                return GameConfig.DOWN
            case _:
                raise KeyError(facing)
    
    def turn_to(self, facing: int) -> None:
        if self.facing == self.__map_facing(facing):
            return
        
        if len(self.snake) > 1 and self.snake[-1] == self.__map_facing(facing):
            return
        
        self.facing = facing
    
    def lengthen(self) -> None:
        self.lengthening = True

    def answer_key(self, key: bytes) -> None:
        match key:
            case b'a':
                self.turn_to(GameConfig.LEFT)
            case b's':
                self.turn_to(GameConfig.DOWN)
            case b'd':
                self.turn_to(GameConfig.RIGHT)
            case b'w':
                self.turn_to(GameConfig.UP)
            case _:
                return
                
        self.tick(forward=False)

    def tick(self, forward: bool = True) -> None:
        if forward:
            if self.lengthening: # do not pop
                self.lengthening = False
                self.snake = deque(self.snake, maxlen=self.snake.maxlen + 1) # type: ignore
            else:
                x, y = self.tail_pos
                match self.snake[0]:
                    case GameConfig.UP:
                        x -= 1
                    case GameConfig.DOWN:
                        x += 1
                    case GameConfig.RIGHT:
                        y += 1
                    case GameConfig.LEFT:
                        y -= 1
                    case _:
                        raise KeyError(self.snake[0])
                    
                self.tail_pos = (x, y)

            self.snake.append(self.facing)

        elif self.snake:
            self.snake[-1] = self.facing