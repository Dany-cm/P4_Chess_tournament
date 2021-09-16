from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController():

    def __init__(self):
        self.view = TournamentView()

    def create_new_tournament(self):
        ''' Ask user to fill out information and save it '''
        questions = ['Name', 'Location name', 'Start date (DD/MM/YYYY)', 'Time control (Bullet, Blitz or Rapid)',
                     'Description', 'Number of round (4 by default)']
        results = []
        for question in questions:
            self.view.ask_information(question)
            result = input()
            results.append(result)

        self.model = Tournament(results[0], results[1], results[2], results[3], results[4], results[5])

        if self.model.create_new_tournament(results[0], results[1], results[2], results[3], results[4], results[5]):
            self.view.display(f'Tournament: {results[0]} {results[1]} {results[2]} \n'
                              f'{results[3]} {results[4]} {results[5]} has been created.')
        else:
            self.view.display('Invalid data. try again')
            self.create_new_tournament()
