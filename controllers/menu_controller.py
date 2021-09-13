from models.players import Player
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu_views import MenuViews


class MenuController():

    def __init__(self):
        self.view = MenuViews()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def first_menu(self):
        ''' Main menu '''
        self.view.main_menu()
        choice = input()

        if choice == '1':
            self.tournament_controller.create_new_tournament()
        elif choice == '2':
            self.player_controller.create_new_player()
        else:
            self.first_menu()

    def run_application(self):
        ''' Welcome message when starting the app and redirect to first_menu'''
        self.view.welcome()
        self.first_menu()
