from models.players import Player
from models.tournament import Tournament
from views.report_view import ReportView
from tinydb import TinyDB


class ReportController():

    def __init__(self):
        self.view = ReportView()

    def get_all_players(self):
        db = TinyDB('players.json')
        player_data = db.table('players')
        players_in_database = player_data.all()
        players = []

        for player in players_in_database:
            player = Player.deserialize_player(player)
            players.append(player)
        return players
    
    def display_sorted_players_name(self):
        player_by_name = Player.sort_player_by_alphabetical_order(self.get_all_players())
        self.view.display('List of players sorted by alphabetical order')
        self.view.display_players_name(player_by_name)

    def display_sorted_player_ranks(self):
        player_by_rank = Player.sort_player_by_ranking_order(self.get_all_players())
        self.view.display('List of players sorted by rank')
        self.view.display_players_rank(player_by_rank)

    def get_all_players_from_tournament(self):
        db = TinyDB('tournament.json')
        player_data = db.table('tournament')
        db_players = player_data.all()
        tournaments = list()

        for tournament in db_players:
            tournament = Tournament.deserialize_tournament(tournament)
            tournaments.append(tournament)

        return tournaments

    def get_all_tournament(self):
        # TODO display all tournament
        pass

    def get_all_rounds_from_tournament(self):
        # TODO display all rounds from a tournament
        pass

    def get_all_match_from_tournament(self):
        # TODO display all matches from a tournament
        pass
