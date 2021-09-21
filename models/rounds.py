from controllers import match_controller
from dataclasses import dataclass, field
from datetime import datetime
from models.match import PlayerNotFound
from models.players import Player
from models.match import Match


@dataclass
class Round():
    round_name: str
    match_list: list = field(default_factory=lambda: [])
    end_date: datetime = None
    start_date: datetime = field(default_factory=lambda: datetime.today().strftime('%d/%m/%Y %H:%M'))

    @staticmethod
    def serialize_round(round):
        ''' Return serialized_round information '''
        return {
            'round_name': round.round_name,
            'match_list': list(Match.serialize_match(match) for match in round.match_list),
            'end_date': round.end_date,
            'start_date': round.start_date,
        }

    @staticmethod
    def deserialize_round(serialized_round):
        ''' Deserialize round information '''
        round_name = serialized_round['round_name']
        match_list = serialized_round['match_list']
        match_list = []
        for serialized_match in serialized_round['match_list']:
            match_list.append(Match.deserialize_match(serialized_match))
        end_date = serialized_round['end_date']
        start_date = serialized_round['start_date']
        return Round(round_name=round_name, match_list=match_list, end_date=end_date, start_date=start_date)

    def finish_round(self):
        ''' On round end display end_date and send result'''
        self.end_date = datetime.today().strftime('%d/%m/%Y %H:%M')
        for match in self.match_list:
            match_controller.MatchController().ask_match_result(match)

    def get_player_score(self, player: Player):
        ''' Get the player score'''
        for match in self.match_list:
            try:
                return match.get_player_score(player)
            except PlayerNotFound:
                pass
        raise PlayerNotFound(player)
