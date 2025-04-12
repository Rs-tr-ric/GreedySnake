# GreedySnake

A terminal-based Snake game with real-time rendering. Control the snake to eat rewards and avoid collisions!

## Features
- 🕹️ ​**​Directional Control​**​: Use `W/A/S/D` to move
- 🎮 ​**​Real-time Rendering​**​: Dynamic terminal interface updates
- ⚡ ​**​Collision Detection​**​: Game over if snake hits walls/itself
- 🏆 ​**​Score System​**​: 1 point per reward, track your highest score
- 🎯 ​**​Auto-Respawn Rewards​**​: New rewards spawn in valid positions

## Installation
```bash
# Install dependencies
uv pip sync

# Run the game
uv python main.py
```

## How to Play
- **​​Start Game​​**: Run `uv run main.py`
- **​​Movement​​**: 
    - `W`: Move Up
    - `A`: Move Left
    - `S`: Move Down
    - `D`: Move Right
- **Win Condition​​**: Fill the entire map with snake body
- **​​Lose Condition​​**:
    - Collide with walls
    - Collide with self

## Example Interface
```text
 +--------------------+
 |                    |
 |                    |
 |                    |
 |                    |
 |                    |
 |                    |
 |                    |
 |  ████████          |
 |████          ❌    |
 |                    |
 +--------------------+
        SCORE: 4
```
