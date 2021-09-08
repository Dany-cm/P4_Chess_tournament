from dataclasses import dataclass
from tinydb import TinyDB
import datetime



@dataclass
class Player(object):
    lastname: str
    firstname: str
    dob: str
    sex: str
    id: int
    rank: int
    playerlist = []


    def serialize_player(self, player):
        ''' Serialize player information '''
        return {
            'lastname': player.lastname,
            'firstname': player.firstname,
            'dob': player.dob,
            'sex': player.sex,
            'id': player.id,
            'rank': player.rank,
        }


    @staticmethod
    def deserialize_player(serialize_player):
        ''' Deserialize player information '''
        lastname = serialize_player['lastname']
        firstname = serialize_player['firstname']
        dob = serialize_player['dob']
        sex = serialize_player['sex']
        id = serialize_player['id']
        rank = serialize_player['rank']
        return Player(lastname=lastname, firstname=firstname, dob=dob, sex=sex, id=id, rank=rank)


    def save_player(self, player):
        ''' Save player in the database '''
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(self.serialize_player(player))

    @staticmethod
    def load_players():
        ''' Load players from datbase '''
        db = TinyDB('db.json')
        players_table = db.table('players')
        for serialized_player in players_table.all():
            Player.playerlist.append(Player.deserialize_player(serialized_player))


    def validate_new_player(self, lastname: str, firstname: str, dob: str, sex: str, rank: int):
        ''' Sanity check to make sure players input are correct, return true if criteria are met '''
        format = '%d/%m/%Y'
        try:
            datetime.datetime.strptime(dob, format)
        except ValueError:
            return False

        if not lastname.isalpha():
            return False

        if not firstname.isalpha():
            return False

        if sex != 'M'.casefold() and sex != 'F'.casefold():
            return False

        if not rank.isdigit() or int(rank) < 1:
            return False

        return True


    def create_new_player(self, lastname: str, firstname: str, dob: str, sex: str, rank: int):
        ''' Create a new player and save in the db '''
        if self.validate_new_player(lastname, firstname, dob, sex, rank):
            id = len(Player.playerlist) + 1
            new_player = Player(lastname, firstname, dob, sex, id, rank)
            Player.playerlist.append(new_player)
            self.save_player(new_player)
            return True
        return False
