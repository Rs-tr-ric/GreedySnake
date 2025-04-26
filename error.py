class GameOver(Exception):
    def __init__(self, *args): # type: ignore
        super().__init__(*args)