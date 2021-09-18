from models.players import Player


class PlayerView():

    def ask_information(self, dataRequested):
        print('Please type the ' + dataRequested)

    def display(self, message):
        print(message)

    def display_players_name(self, players_to_display: list[Player]):
        ''' '''
        for index, player in enumerate(players_to_display):
            print(f'{index + 1}: {player}')
