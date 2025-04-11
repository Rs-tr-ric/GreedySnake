from typing import Tuple, Iterable
from snake import Snake
from error import GameOver
from config import GameConfig

import numpy as np # type: ignore
import random

class GameMap(object):
    def __init__(self, shape: Tuple[int, int], snake: Snake) -> None:
        self.shape = shape
        self.snake = snake
        self.score = 0

        self.reward = self.generate_reward()

    def tick(self, forward: bool = True) -> None:
        self.snake.tick(forward)
    
    def render(self) -> str:
        if self.score >= (self.shape[0] * self.shape[1]) - 1:
            raise GameOver(GameConfig.VICTORY)
        render_map = np.full(shape=self.shape, fill_value=GameConfig.AIR)
        
        x, y = self.reward
        render_map[x, y] = GameConfig.REWARD

        for x, y in self.traverse_snake():
            match render_map[x, y]:
                case GameConfig.SNAKE:
                    raise GameOver(GameConfig.GAMEOVER)
                case GameConfig.REWARD:
                    render_map[x, y] = GameConfig.SNAKE
                    self.reward = self.generate_reward()
                    self.snake.lengthen()
                    self.score += 1
                case GameConfig.AIR:
                    render_map[x, y] = GameConfig.SNAKE
                case _:
                    raise KeyError(render_map[x, y])

        m, n = self.shape
        string = (
            GameConfig.LEFT_CORNER_PATTERN + 
            GameConfig.HORIZONTAL_BOUNDARY_PATTERN * n + 
            GameConfig.RIGHT_CORNER_PATTERN + '\n'
        )
        line_length = len(string) - 1

        for i in range(m):
            string += GameConfig.LEFT_VERTICAL_BOUNDARY_PATTERN
            for j in range(n):
                match render_map[i, j]:
                    case GameConfig.AIR:
                        string += GameConfig.AIR_PATTERN
                    case GameConfig.SNAKE:
                        string += GameConfig.SNAKE_PATTERN
                    case GameConfig.REWARD:
                        string += GameConfig.REWARD_PATTERN
                    case _:
                        raise KeyError(render_map[i, j])
            string += GameConfig.RIGHT_VERTICAL_BOUNDARY_PATTERN + '\n'
        
        string += (
            GameConfig.LEFT_CORNER_PATTERN + 
            GameConfig.HORIZONTAL_BOUNDARY_PATTERN * n + 
            GameConfig.RIGHT_CORNER_PATTERN + '\n'
        )

        score_line = f'SCORE: {self.score}'.center(line_length)

        string += score_line

        return string

    def generate_reward(self) -> Tuple[int, int]:
        m, n = self.shape

        # generate valid points; convert to 1D indices; sort
        excluded_indices = set()
        for (x, y) in self.traverse_snake():
            excluded_indices.add(x * n + y)
        sorted_excluded = sorted(excluded_indices)
        total_available = m * n - len(sorted_excluded)
        
        if total_available <= 0:
            raise ValueError('no valid points')
        
        # generate random position and map to index
        r = random.randint(0, total_available - 1)
        current_pos, remaining_r = 0, r
        sorted_excluded.append(m * n)  # add sentinel
        
        # interval jumping algorithm
        for excl in sorted_excluded:
            available_in_segment = excl - current_pos
            if available_in_segment > remaining_r:
                selected_index = current_pos + remaining_r
                return (selected_index // n, selected_index % n)
            remaining_r -= available_in_segment
            current_pos = excl + 1
        
        raise RuntimeError('failed to generate a reward point')

    def traverse_snake(self) -> Iterable[tuple[int, int]]:
        m, n = self.shape
        x, y = self.snake.tail_pos
        for facing in self.snake.snake:
            if not 0 <= x < m:
                raise GameOver(GameConfig.GAMEOVER)
            if not 0 <= y < n:
                raise GameOver(GameConfig.GAMEOVER)
            
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
