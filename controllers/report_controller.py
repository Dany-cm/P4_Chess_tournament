from models.players import Player
from views.report_view import ReportView


class ReportController():

    def __init__(self):
        self.view = ReportView()

    def get_all_players(self, player: Player):
        # TODO: abc & rank
        pass

    def get_all_players_from_tournament(self):
        # TODO abc & rank
        pass

    def get_all_tournament(self):
        # TODO display all tournament
        pass

    def get_all_rounds_from_tournament(self):
        # TODO display all rounds from a tournament
        pass

    def get_all_match_from_tournament(self):
        # TODO display all matches from a tournament
        pass
