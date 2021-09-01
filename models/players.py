from dataclasses import dataclass
from tinydb import TinyDB
import datetime

playerlist = []

@dataclass
class Player():
    lastname: str
    firstname: str
    dob: str
    sex: str
    id: int
    rank: int

def serialize_player(player):
    return {
        'lastname': player.lastname,
        'firstname': player.firstname,
        'dob': player.dob,
        'sex': player.sex,
        'id': player.id,
        'rank': player.rank,
    }

def deserialize_player(serialize_player):
    lastname = serialize_player['lastname']
    firstname = serialize_player['firstname']
    dob = serialize_player['dob']
    sex = serialize_player['sex']
    id = serialize_player['id']
    rank = serialize_player['rank']
    return Player(lastname=lastname, firstname=firstname,dob=dob, sex=sex,id=id, rank=rank)

def save_player(player:Player):
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.insert(serialize_player(player))

def load_players():
    db = TinyDB('db.json')
    players_table = db.table('players')
    for serialized_player in players_table.all():
        playerlist.append(deserialize_player(serialized_player))

def validate_new_player(lastname:str,firstname:str,dob:str,sex:str):
    format = "%Y/%m/%d"
    try:
        datetime.datetime.strptime(dob, format)
    except ValueError:
        print(ValueError)
        return False

    if not lastname.isalpha():
        return False

    if not firstname.isalpha():
        return False

    if sex != 'M' and sex != 'F':
        return False

    return True

def create_new_player(lastname:str,firstname:str,dob:str,sex:str):
    if validate_new_player(lastname,firstname,dob,sex):
        id = len(playerlist) + 1
        rank = len(playerlist) + 1
        new_player = Player(lastname,firstname,dob,sex,id,rank)
        playerlist.append(new_player)
        save_player(new_player)