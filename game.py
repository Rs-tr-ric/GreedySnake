from typing import Tuple, Iterable
from snake import Snake
from error import GameOver
from config import GameConfig

import random

class Game(object):
    def __init__(self, shape: Tuple[int, int], snake: Snake) -> None:
        self.shape = shape
        self.snake = snake
        self.score = 0

        self.spawn_reward()

    def tick(self, forward: bool = True) -> None:
        if self.score >= (self.shape[0] * self.shape[1]) - 1:
            self.game_over(GameConfig.VICTORY)
        
        self.snake.tick(forward)
    
    def receive_reward(self) -> None:
        self.spawn_reward()
        self.lengthen_snake()
        self.score += 1

    def lengthen_snake(self) -> None:
        self.snake.lengthen()

    def spawn_reward(self) -> None:
        m, n = self.shape

        # generate valid points; convert to 1D indices; sort
        excluded_indices: set[int] = set() 
        for (x, y) in self.traverse_snake():
            excluded_indices.add(x * n + y)
        sorted_excluded = sorted(excluded_indices)
        total_available = m * n - len(sorted_excluded)
        
        if total_available <= 0:
            self.game_over(GameConfig.VICTORY)
        
        # generate random position and map to index
        r = random.randint(0, total_available - 1)
        current_pos, remaining_r = 0, r
        sorted_excluded.append(m * n)  # add sentinel
        
        # interval jumping algorithm
        for excl in sorted_excluded:
            available_in_segment = excl - current_pos
            if available_in_segment > remaining_r:
                selected_index = current_pos + remaining_r
                self.reward = (selected_index // n, selected_index % n)
                return
            remaining_r -= available_in_segment
            current_pos = excl + 1
        
        raise RuntimeError('failed to generate a reward point')

    def traverse_snake(self) -> Iterable[tuple[int, int]]:
        m, n = self.shape
        x, y = self.snake.tail_pos
        for facing in self.snake.snake:
            if not (0 <= x < m and 0 <= y < n):
                self.game_over(GameConfig.GAME_OVER)
            
            yield x, y

            match facing:
                case GameConfig.UP:
                    x -= 1
                case GameConfig.DOWN:
                    x += 1
                case GameConfig.RIGHT:
                    y += 1
                case GameConfig.LEFT:
                    y -= 1
                case _:
                    raise KeyError(facing)
    
    def game_over(self, state: int) -> None:
        match state:
            case GameConfig.GAME_OVER:
                raise GameOver(GameConfig.GAME_OVER_TEXT)
            case GameConfig.VICTORY:
                raise GameOver(GameConfig.VICTORY_TEXT)
            case _:
                return
