from dataclasses import dataclass
from tinydb import TinyDB, Query
import datetime
import uuid


@dataclass
class Player(object):
    lastname: str
    firstname: str
    dob: str
    sex: str
    rank: int
    id: int = uuid.uuid4().urn.replace("urn:uuid:", "")
    playerlist = []

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f'{self.lastname} {self.firstname}'

    @staticmethod
    def serialize_player(player):
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

    @staticmethod
    def save_players():
        ''' Save player in the database '''
        db = TinyDB('players.json')
        players_table = db.table('players')
        players_table.truncate()
        for player in Player.playerlist:
            players_table.insert(Player.serialize_player(player))

    @staticmethod
    def load_players():
        ''' Load players from datbase '''
        Player.playerlist = []
        db = TinyDB('players.json')
        players_table = db.table('players')
        for serialized_player in players_table.all():
            Player.playerlist.append(Player.deserialize_player(serialized_player))

    def update_player_rank(self):
        ''' Update a player rank'''
        db = TinyDB('players.json')
        players_table = db.table('players')
        players_table.update({'rank': self.rank}, Query()['id'] == f'{self.id}')

    @staticmethod
    def sort_player_by_alphabetical_order():
        ''' Sort player by alphabetical order'''
        return sorted(Player.playerlist, key=lambda x: x.lastname.upper())

    @staticmethod
    def sort_player_by_ranking_order():
        ''' Sort player by ranking order'''
        return sorted(Player.playerlist, key=lambda x: x.rank)

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

        if not int(rank) or int(rank) < 1:
            return False

        return True

    def create_new_player(self, lastname: str, firstname: str, dob: str, sex: str, rank: int):
        ''' Create a new player and save in the db '''
        if self.validate_new_player(lastname, firstname, dob, sex, rank):
            new_player = Player(lastname, firstname, dob, sex, rank)
            Player.playerlist.append(new_player)
            Player.save_players()
            return True
        return False
