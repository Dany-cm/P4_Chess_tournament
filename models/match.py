from dataclasses import dataclass
from models.players import Player


@dataclass
class Match(object):
    match: tuple[list, list] = ([], [])

    def __init__(self, player1: Player, player2: Player):
        self.match[0].append(player1)
        self.match[1].append(player2)
        self.match[0].append(0)
        self.match[1].append(0)

    def __str__(self):
        return f'{self.match[0][0].firstname} {self.match[0][0].lastname} ({self.match[0][1]}) --- ' +\
            f'{self.match[1][0].firstname} {self.match[1][0].lastname} ({self.match[1][1]})'
