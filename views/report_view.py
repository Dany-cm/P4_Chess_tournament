from models.players import Player


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