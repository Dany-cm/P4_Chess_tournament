from dataclasses import dataclass
from models.players import Player


class PlayerNotFound(Exception):
    def __init__(self, player):
        super().__init__(f'{player} not found')


@dataclass
class Match(object):
    match: tuple[list, list]

    def __init__(self, player1: Player, player2: Player):
        self.match = ([player1, 0], [player2, 0])

    def __str__(self):
        return f'{self.match[0][0]} ({self.match[0][1]}) --- ' +\
            f'{self.match[1][0]} ({self.match[1][1]})'

    def get_player_score(self, player: Player):
        if player == self.match[0][0]:
            return self.match[0][1]
        elif player == self.match[1][0]:
            return self.match[1][1]
        raise PlayerNotFound(player)
