from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.players import Player
from models.tournament import Tournament
from views.menu_views import MenuViews


class MenuController():

    def __init__(self):
        self.view = MenuViews()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def main_menu(self):
        ''' Main menu '''
        self.view.main_menu()
        choice = input()

        if choice == '1':
            self.tournament_menu()
        elif choice == '2':
            self.player_menu()
        elif choice == '3':
            self.report_menu()
        elif choice == '4':
            exit()
        else:
            self.main_menu()
    
    def tournament_menu(self):
        ''' Main menu '''
        self.view.tournament_menu()
        choice = input()

        if choice == '1':
            self.tournament_controller.create_new_tournament()
        elif choice == '2':
            self.tournament_controller.add_players_to_tournament()
        elif choice == '3':
            print('play a tournament todo')
        elif choice == '4':
            self.main_menu()
        else:
            self.tournament_menu()
    
    def player_menu(self):
        ''' Main menu '''
        self.view.player_menu()
        choice = input()

        if choice == '1':
            self.player_controller.create_new_player()
        elif choice == '2':
            print(' Edit player rank')
        elif choice == '3':
            self.main_menu()
        else:
            self.player_menu()
    
    def report_menu(self):
        ''' Second menu '''
        self.view.reports_menu()
        choice = input()

        if choice == '1':
            print('')
        elif choice == '2':
            print('')
        elif choice == '3':
            print('')
        elif choice == '5':
            print('')
        elif choice == '5':
            print('')
        elif choice == '6':
            self.report_menu()

    def run_application(self):
        ''' Welcome message when starting the app and redirect to first_menu'''
        self.load_data()
        self.view.welcome()
        self.main_menu()

    def load_data(self):
        Player.load_players()
        Tournament.load_tournaments()
