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
        player_by_name = Player.sort_player_by_alphabetical_order()
        self.view.display('List of players sorted by alphabetical order')
        self.view.display_players_name(player_by_name)

    def display_sorted_player_ranks(self):
        player_by_rank = Player.sort_player_by_ranking_order()
        self.view.display('List of players sorted by rank')
        self.view.display_players_rank(player_by_rank)

    def select_tournament(self):
        self.view.display_tournaments_name(Tournament.tournamentlist)

        correct = False
        while (not correct):
            selection = input()
            correct = selection.isdigit() and int(selection) >= 1 and int(selection) <= len(Tournament.tournamentlist)

            if not correct:
                self.view.display('Please enter only a number matching a tournament')

        return Tournament.tournamentlist[int(selection) - 1]

    def display_sorted_player_from_tournament_by_alphabetical_order(self):
        tournament_to_display: Tournament = self.select_tournament()
        player_by_name = tournament_to_display.sort_player_from_tournament_by_alphabetical_order()
        self.view.display('List of players sorted by name')
        self.view.display_players_name(player_by_name)

    def display_sorted_player_from_tournament_by_rank_order(self):
        tournament_to_display: Tournament = self.select_tournament()
        player_by_rank = tournament_to_display.sort_player_from_tournament_by_rank_order()
        self.view.display('List of players sorted by rank')
        self.view.display_players_rank(player_by_rank)

    def get_all_tournament(self):
        self.view.display('List of tournaments')
        self.view.display_tournaments_name(Tournament.tournamentlist)

    def get_all_rounds_from_tournament(self):
        self.view.display('List of all rounds from a tournament')
        tournament_to_display: Tournament = self.select_tournament()
        self.view.display_tournament_rounds_name(tournament_to_display)

    def get_all_matchs_from_tournament(self):
        self.view.display('List of all matchs from a tournament')
        tournament_to_display: Tournament = self.select_tournament()
        self.view.display_tournament_matchs_name(tournament_to_display)
