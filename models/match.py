from dataclasses import dataclass
from models.players import Player


class PlayerNotFound(Exception):
    def __init__(self, player):
        super().__init__(f'{player} not found')


@dataclass
class Match(object):
    match: tuple[list, list]

    def __init__(self, player1: Player, player2: Player, score1: int = 0, score2: int = 0):
        self.match = ([player1, score1], [player2, score2])

    def __str__(self):
        return f'{self.match[0][0]} ({self.match[0][1]}) --- ' +\
            f'{self.match[1][0]} ({self.match[1][1]})'

    @staticmethod
    def serialize_match(match):
        ''' Return serialized_match information '''
        return {
            'match': ([match.match[0][0].id, match.match[0][1]], [match.match[1][0].id, match.match[1][1]])
        }

    @staticmethod
    def deserialize_match(serialized_match):
        ''' Deserialize match information '''
        player1: Player = list(filter(lambda player: player.id == serialized_match['match'][0][0],
                                      Player.playerlist))[0]
        player2: Player = list(filter(lambda player: player.id == serialized_match['match'][1][0],
                                      Player.playerlist))[0]
        return Match(player1, player2, serialized_match['match'][0][1], serialized_match['match'][1][1])

    def get_player_score(self, player: Player):
        if player == self.match[0][0]:
            return self.match[0][1]
        elif player == self.match[1][0]:
            return self.match[1][1]
        raise PlayerNotFound(player)
