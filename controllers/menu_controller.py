from models.players import Player
from controllers.player_controller import player_controller
from views.menu_views import MenuViews


class menu_controller():

    def __init__(self):
        self.view = MenuViews()
        self.player_controller = player_controller()
        Player.load_players()

    def first_menu(self):
        self.view.main_menu()
        choice = input()

        if choice == '1':
            self.create_tournament()
        elif choice == '2':
            self.player_controller.create_new_player()
        else:
            self.first_menu()

    def create_tournament(self):
        self.view.create_tournament()

    def run_application(self):
        self.view.welcome()
        self.first_menu()
