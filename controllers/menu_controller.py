from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController
from models.players import Player
from models.tournament import Tournament
from views.menu_views import MenuViews


class MenuController():

    def __init__(self):
        self.view = MenuViews()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.report_controller = ReportController()

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
            Tournament.save_tournaments()
            Player.save_players()
            exit()
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
            self.tournament_controller.start_tournament()
        elif choice == '4':
            self.tournament_controller.finish_in_progress_round()
        elif choice == '5':
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
            self.player_controller.modify_player_rank()
        elif choice == '3':
            self.main_menu()
        else:
            self.player_menu()

    def report_menu(self):
        ''' Main menu '''
        self.view.reports_menu()
        choice = input()

        if choice == '1':
            self.report_menu_second()
        elif choice == '2':
            self.report_menu_third()
        elif choice == '3':
            self.report_controller.get_all_tournament()
        elif choice == '4':
            self.report_controller.get_all_rounds_from_tournament()
        elif choice == '5':
            self.report_controller.get_all_matchs_from_tournament()
        elif choice == '6':
            self.report_menu()

    def report_menu_second(self):
        ''' Main menu '''
        self.view.report_menu_second()
        choice = input()

        if choice == '1':
            self.report_controller.display_sorted_players_name()
        elif choice == '2':
            self.report_controller.display_sorted_player_ranks()
        elif choice == '3':
            self.report_menu()

    def report_menu_third(self):
        ''' Main menu '''
        self.view.report_menu_third()
        choice = input()

        if choice == '1':
            self.report_controller.display_sorted_player_from_tournament_by_alphabetical_order()
        elif choice == '2':
            self.report_controller.display_sorted_player_from_tournament_by_rank_order()
        elif choice == '3':
            self.report_menu()

    def run_application(self):
        ''' Welcome message when starting the app and redirect to first_menu'''
        self.load_data()
        self.view.welcome()
        self.main_menu()

    def load_data(self):
        Player.load_players()
        Tournament.load_tournaments()
