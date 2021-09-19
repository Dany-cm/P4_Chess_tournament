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

        if self.model.create_new_player(results[0], results[1], results[2], results[3], int(results[4])):
            self.view.display(f'Player: {results[0]} {results[1]} has been created.')
        else:
            self.view.display('Invalid data. try again')
            self.create_new_player()

    def modify_player_rank(self):
        ''' Modify the rank of a selected player'''
        if len(Player.playerlist) <= 0:
            self.view.display('You need at least 1 player in the application to do this')
            return False

        self.view.display_players_name(Player.playerlist)
        self.view.display('Select the player number to modify their rank')

        player_list_index = [i for i, x in enumerate(Player.playerlist)]
        selected_player = input()

        if not(selected_player.isdigit() and int(selected_player) >= 1):
            self.view.display('Only numbers are allowed and it must greater than 0')
        elif not int(selected_player) <= len(player_list_index):
            self.view.display('Player does not exist')
        elif int(selected_player) > 0 and int(selected_player) <= len(player_list_index):
            sanitized_input = input('Enter the new rank for the player ')
            try:
                if int(sanitized_input) > 0:
                    new_rank = sanitized_input
                    Player.rank = int(new_rank)
                    Player.update_player_rank(int(selected_player))
                    self.view.display(f'Rank has been updated to {new_rank}')
                else:
                    self.view.display('Number must be greater than 0')
                    print('Number must be greater than 0')
            except ValueError:
                self.view.display('Please only enter a number superior to 0')
