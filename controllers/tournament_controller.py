from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController():

    def __init__(self):
        self.view = TournamentView()

    def create_new_tournament(self):
        ''' Ask user to fill out information and save it '''
        questions = ['Name', 'Location name', 'Start date (DD/MM/YYYY)', 'End date (DD/MM/YYYY)',
                     'Time control (Bullet, Blitz or Rapid)', 'Description', 'Number of round (4 by default)']
        results = []
        for question in questions:
            self.view.ask_information(question)
            result = input()
            results.append(result)

        self.tournament = Tournament(result[0], result[1], result[2], result[3], result[4], result[5],
                                     result[6], result[7], result[8], result[9])

        self.view.display('test')

        # todo: add players, save tournament
