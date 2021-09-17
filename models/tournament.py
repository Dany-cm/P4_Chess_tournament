from dataclasses import dataclass, field
from models.players import Player
from models.rounds import Round
from models.match import Match
from tinydb import TinyDB
from datetime import datetime
import uuid


@dataclass
class Tournament(object):
    name: str
    location: str
    start_date: datetime
    control_time: str
    description: str
    number_of_round: int = 4
    end_date: datetime = None
    player_list: list = field(default_factory = lambda: [])
    round_list: list = None
    id: int = uuid.uuid1().urn.replace("urn:uuid:", "")
    tournamentlist = []

    @staticmethod
    def serialize_tournament(tournament):
        ''' Return serialized_tournament information '''
        return {
            'name': tournament.name,
            'location': tournament.location,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'player_list': list(player.id for player in tournament.player_list),
            'round_list': tournament.round_list,
            'control_time': tournament.control_time,
            'description': tournament.description,
            'id': tournament.id,
            'number_of_round': tournament.number_of_round,
        }

    @staticmethod
    def deserialize_tournament(serialize_tournament):
        ''' Deserialize player information '''
        name = serialize_tournament['name']
        location = serialize_tournament['location']
        start_date = serialize_tournament['start_date']
        end_date = serialize_tournament['end_date']
        player_list = []
        for serializedPlayer in serialize_tournament['player_list']:
            player_list.append(list(filter(lambda player: player.id == serializedPlayer, Player.playerlist))[0])
        round_list = serialize_tournament['round_list']
        control_time = serialize_tournament['control_time']
        description = serialize_tournament['description']
        id = serialize_tournament['id']
        number_of_round = serialize_tournament['number_of_round']
        return Tournament(name=name, location=location, start_date=start_date, end_date=end_date,
                          player_list=player_list, round_list=round_list, control_time=control_time,
                          description=description, id=id, number_of_round=number_of_round)
    @staticmethod
    def save_tournaments():
        ''' Save tournament in the database '''
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        tournament_table.truncate()
        for tournament in Tournament.tournamentlist:
            tournament_table.insert(Tournament.serialize_tournament(tournament))

    @staticmethod
    def load_tournaments():
        ''' Load tournament_table from database '''
        Tournament.tournamentlist = []
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        for serialized_tournament in tournament_table.all():
            Tournament.tournamentlist.append(Tournament.deserialize_tournament(serialized_tournament))

    def get_player_score(self, player: Player):
        ''' Get the player score '''
        return sum(x.get_player_score(player) for x in self.round_list)

    def sorted_player_score(self):
        ''' Sort player score and rank by descending order '''
        self.player_list.sort(key=lambda player: (self.get_player_score(player), player.rank), reverse=True)

    def create_new_round(self):
        ''' Create a new round '''
        round = Round(f'Round{len(self.round_list) +1}', matchlist=[])
        length = len(self.player_list)
        middle_index = length // 2
        sup_half = self.player_list[:middle_index]
        inf_half = self.player_list[middle_index:]

        for player_index in range(0, middle_index):
            round.match_list.append(Match(sup_half[player_index], inf_half[player_index]))

        self.round_list.append(round)

    def validate_new_tournament(self, name: str, location: str, start_date: datetime,
                                control_time: str, description: str, number_of_round: int):
        ''' Sanity check to make sure input are correct, return true if criteria are met'''
        if not all(name_check.isalpha() or name_check.isspace() for name_check in name):
            return False

        if not location.isalpha():
            return False

        format = '%d/%m/%Y'
        try:
            datetime.strptime(start_date, format)
        except ValueError:
            return False

        if not control_time.isalpha():
            return False

        if not description.isalpha():
            return False

        if not number_of_round.isdigit() or int(number_of_round) < 1:
            return False

        return True

    def create_new_tournament(self, name: str, location: str, start_date: datetime,
                              control_time: str, description: str, number_of_round: int):
        ''' Create a new tournament and save in the db'''
        if self.validate_new_tournament(name, location, start_date, control_time, description, number_of_round):
            new_tournament = Tournament(name, location, start_date, control_time, description, number_of_round)
            Tournament.tournamentlist.append(new_tournament)
            Tournament.save_tournaments()
            return True
        return False
