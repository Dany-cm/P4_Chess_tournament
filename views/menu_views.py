class MenuViews():

    def welcome(self):
        print('Welcome to the chess manager application')

    def main_menu(self):
        print('What do you want to do?')
        print('1: Manage tournaments')
        print('2: Manage players')
        print('3: Reports')
        print('4: Quit application')

    def tournament_menu(self):
        print('What do you want to do?')
        print('1: Create a tournament')
        print('2: Add 8 players to a tournament')
        print('3: Start a tournament')
        print('4: Resume a tournament')
        print('5: Back to previous menu')

    def player_menu(self):
        print('What do you want to do?')
        print('1: Create a new player')
        print('2: Edit a player rank')
        print('3: Back to the previous menu')

    def reports_menu(self):
        print('What do you want to do?')
        print('1: Show all players')
        print('2: Show all players in a tournament')
        print('3: Show all tournament')
        print('4: Show all rounds from a tournament')
        print('5: Show all matches from a tournament')
        print('6: Back to the previous menu')

    def report_menu_second(self):
        print('What do you want to do?')
        print('1: Show all players by alphabetic order')
        print('2: Show all players by ranking')
        print('3: Back to the previous menu')

    def report_menu_third(self):
        print('What do you want to do?')
        print('1: Show all players in tournaments by alphabetic order')
        print('2: Show all players in tournaments by ranking')
        print('3: Back to the previous menu')
