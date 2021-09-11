from models.players import Player

class MatchView(object):

    def display_match_result_form(self, player1: Player, player2: Player):
        print('Please input the result of the match (1/2/3)')
        print(f'1 - {player1.firstname} {player1.lastname} Won')
        print(f'2 - {player2.firstname} {player2.lastname} Won')
        print('3 - Draw')
    
    def display(self, message):
        print(message)

