from models.players import Player
from views.player_view import PlayerView


class PlayerController():

    def __init__(self):
        self.view = PlayerView()

    def create_new_player(self):
        ''' Ask user to fill out information and save it '''
        questions = ['Last name', 'First name', 'Birth date (DD/MM/YYYY)', 'Sex (M/F)', 'Rank']
        results = []
        for question in questions:
            self.view.ask_information(question)
            result = input()
            results.append(result)

        self.model = Player(results[0], results[1], results[2], results[3], results[4])

        if self.model.create_new_player(results[0], results[1], results[2], results[3], results[4]):
            self.view.display(f'{results[0]} {results[1]} has been created.')
        else:
            self.view.display('Invalid data. try again')
            self.create_new_player()
