from controllers import match_controller
from dataclasses import dataclass, field
from datetime import datetime
from models.match import Match, PlayerNotFound
from models.players import Player


@dataclass
class Round():
    round_name: str
    match_list: list
    end_date: datetime = None
    start_date: datetime = field(default_factory=lambda: datetime.today().strftime('%d/%m/%Y %H:%M'))


    def finish_round(self):
        ''' On round end display end_date and send result'''
        self.end_date = datetime.today().strftime('%d/%m/%Y %H:%M')
        for match in self.match_list:
            match_controller.MatchController().ask_match_result(match)
    
    def get_player_score(self, player: Player):
        for match in self.match_list:
            try:
                return match.get_player_score(player)
            except PlayerNotFound:
                pass
        raise PlayerNotFound(player)