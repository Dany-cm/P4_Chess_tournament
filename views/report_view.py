from models.players import Player
from models.tournament import Tournament


class ReportView:
    def __init__(self):
        pass

    def display(self, message):
        print(message)

    def display_players_name(self, players_to_display: list[Player]):
        ''' Display the index and the list of players'''
        for index, player in enumerate(players_to_display):
            print(f'{index + 1}: {player}')

    def display_players_rank(self, players_to_display: Player):
        ''' Display the index and the list of players'''
        for index, player in enumerate(players_to_display):
            print(f'{index + 1}: {player} = {player.rank}')

    def display_tournaments_name(self, tournaments_to_display: list[Tournament]):
        ''' Display tournament names'''
        for index, tournament in enumerate(tournaments_to_display):
            print(f'{index + 1}: {tournament.name}')

    def display_tournament_rounds_name(self, tournament: Tournament):
        ''' Display tournament rounds name'''
        for index, round in enumerate(tournament.round_list):
            print(f'{index + 1}: {round.round_name}')

    def display_tournament_matchs_name(self, tournament: Tournament):
        ''' Display tournament matchs name'''
        for round in tournament.round_list:
            for match in round.match_list:
                print(f'{round.round_name}: {match}')
