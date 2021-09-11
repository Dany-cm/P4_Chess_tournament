from dataclasses import dataclass
from tinydb import TinyDB
from datetime import datetime


@dataclass
class Tournament(object):
    name: str
    location: str
    start_date: datetime
    end_date: datetime
    player_list: list
    round_list: list
    control_time: int
    description: str
    id: int
    number_of_round: int = 4


    def serialize_tournament(self, tournament):
        '''
        Return serialized_tournament information
        '''
        return {
            'name': tournament.name,
            'location': tournament.location,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'player_list': tournament.player_list,
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
        player_list = serialize_tournament['player_list']
        round_list = serialize_tournament['round_list']
        control_time = serialize_tournament['control_time']
        description = serialize_tournament['description']
        id = serialize_tournament['id']
        number_of_round = serialize_tournament['number_of_round']
        return Tournament(name=name, location=location, start_date=start_date, end_date=end_date, player_list=player_list, round_list=round_list, control_time=control_time, description=description, id=id, number_of_round=number_of_round)

    
    def save_tournament(self, tournament):
        ''' Save tournament in the database '''
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        tournament_table.insert(self.serialize_tournament(tournament))

    @staticmethod
    def load_tournament():
        ''' Load tournament_table from datbase '''
        db = TinyDB('tournament.json')
        tournament_table = db.table('tournament')
        for serialized_tournament in tournament_table.all():
            Tournament.round_list.append(Tournament.deserialize_tournament(serialized_tournament))


    def sorted_player_rank(self):
        ''' Sort ranks by ascending order '''
        self.player_list = sorted(self.player_list, key=lambda player: player.rank)


    def create_player_pairs(self):
        """ if round == 0:
            self.player_list = sorted(self.player_list, key=lambda player: player.rank)
            length = len(self.player_list)
            middle_index = length // 2
            sup_half = self.player_list[:middle_index]
            inf_half = self.player_list[middle_index:] """
        pass
