class GameConfig(object):
    AIR    = 0
    SNAKE  = 1
    REWARD = 2

    UP    = 0
    DOWN  = 1
    LEFT  = 2
    RIGHT = 3

    AIR_PATTERN    = '  '
    SNAKE_PATTERN  = '\u2588' * 2
    REWARD_PATTERN = '\u274c'
    LEFT_CORNER_PATTERN         = ' +'
    RIGHT_CORNER_PATTERN        = '+ '
    HORIZONTAL_BOUNDARY_PATTERN = '--'
    LEFT_VERTICAL_BOUNDARY_PATTERN  = ' |'
    RIGHT_VERTICAL_BOUNDARY_PATTERN = '| '

    GAME_OVER = 0
    VICTORY   = 1

    GAME_OVER_TEXT = '''
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                               
    '''

    VICTORY_TEXT = '''
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║
██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝
    '''

    KEYBOARD_INPUT_FPS = 60
    RENDER_FPS         = 10

    TIME_HISTORY_LEN = 10

    GAME_MAP_SHAPE = (20, 20)
    
    SNAKE_INIT_POS = (10, 10)
    SNAKE_INIT_LEN = 2
    SNAKE_INIT_FACING = UP

    GAME_GUIDE = '** w, a, s, d to move **'.center((GAME_MAP_SHAPE[0] + 2) * 2)