from models.players import Player


class MatchView(object):

    def display_match_result_form(self, player1: Player, player2: Player):
        ''' Ask user to input info '''
        print('Please input the result (typing 1, 2 or 3) for the following match')
        print(f'{player1.firstname} {player1.lastname} vs {player2.firstname} {player2.lastname}')
        print(f'1 - {player1.firstname} {player1.lastname} won')
        print(f'2 - {player2.firstname} {player2.lastname} won')
        print('3 - Draw')

    def display(self, message):
        ''' Helper function to display a message '''
        print(message)
