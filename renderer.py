from game import Game
from config import GameConfig

import numpy as np # type: ignore


class Renderer(object):
    def __init__(self, game: Game) -> None:
        self.game = game

    def render(self) -> str:        
        render_map = np.full(shape=self.game.shape, fill_value=GameConfig.AIR)
        
        x, y = self.game.reward
        render_map[x, y] = GameConfig.REWARD

        for x, y in self.game.traverse_snake():
            match render_map[x, y]:
                case GameConfig.SNAKE:
                    self.game.game_over(GameConfig.GAME_OVER)
                case GameConfig.REWARD:
                    render_map[x, y] = GameConfig.SNAKE
                    self.game.receive_reward()
                case GameConfig.AIR:
                    render_map[x, y] = GameConfig.SNAKE
                case _:
                    raise KeyError(render_map[x, y])

        m, n = self.game.shape
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

        score_line = f'SCORE: {self.game.score}'.center(line_length)

        string += score_line

        return string
