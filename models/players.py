from dataclasses import dataclass
from tinydb import TinyDB

@dataclass
class Players():
    lastname: str
    firstname: str
    dob: str
    sex: str
    id: int = 0
    rank: int = 0
    score: int = 0

def serialized_players(player):
    return {
        'lastname': player.lastname,
        'firstname': player.firstname,
        'dob': player.dob,
        'sex': player.sex,
        'id': player.id,
        'rank': player.rank,
        'score': player.score,
    }

def invoke_serialized_players():
    # TODO: figure out what to do exactly
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()
    players_table.insert_multiple(serialized_players)