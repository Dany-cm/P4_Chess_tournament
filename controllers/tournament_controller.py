from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController():

    def __init__(self):
        self.view = TournamentView()

    def create_new_tournament(self):
        ''' Ask user to fill out information and save it '''
        self.view.ask_information('Name')
        name = input()
        self.view.ask_information('Location')
        location = input()
        self.view.ask_information('Start date (DD/MM/YYYY)')
        start_date = input()
        self.view.ask_information('End date (DD/MM/YYYY)')
        end_date= input()
        self.view.ask_information('Time control (Bullet, Blitz or Rapid)')
        control_time = input()
        self.view.ask_information('Description')
        description = input()
        self.view.ask_information('Number of round (4 by default)')
        number_of_round = input()

        self.tournament = Tournament(name=name, location=location, start_date=start_date, end_date=end_date, player_list= None, round_list=None, control_time=control_time, description=description, id=id, number_of_round=number_of_round)

        self.view.display('test')

        # todo: add players, save tournament



