from models.players import Player
from views.player_view import PlayerView
import datetime


class PlayerController():

    def __init__(self):
        self.view = PlayerView()

    def check_last_name(self, lastname):
        if not lastname.isalpha():
            return False
        return True

    def check_first_name(self, firstname):
        if not firstname.isalpha():
            return False
        return True

    def check_birth_date(self, dob):
        format = '%d/%m/%Y'
        try:
            datetime.datetime.strptime(dob, format)
        except ValueError:
            return False
        return True

    def check_sex(self, sex):
        if sex != 'M'.casefold() and sex != 'F'.casefold():
            return False
        return True

    def check_rank(self, rank):
        if not rank.isdigit() or int(rank) < 1:
            return False
        return True

    def create_new_player(self):
        ''' Ask user to fill out information and save it '''
        questions = [('Last name', self.check_last_name), ('First name', self.check_first_name), ('Birth date (DD/MM/YYYY)', self.check_birth_date), ('Sex (M/F)', self.check_sex), ('Rank', self.check_rank)]
        results = []
        for question in questions:
            self.view.ask_information(question[0])
            is_correct = False
            while not is_correct:
                result = input()
                is_correct = question[1](result)
                if not is_correct:
                    self.view.display(f'{question[0]} is invalid, please try again')
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

        self.view.display('List of players')
        self.view.display_players_name(Player.playerlist)
        self.view.display('Select the player number to modify their rank (must be a number greater than 0)')

        player_list_index = [i for i, x in enumerate(Player.playerlist)]
        selected_player = input()

        if not(selected_player.isdigit() and int(selected_player) >= 1):
            self.view.display('Only numbers are allowed and it must greater than 0')
            self.modify_player_rank()
        elif not int(selected_player) <= len(player_list_index):
            self.view.display('Player does not exist')
            self.modify_player_rank()
        else:
            player_to_modify: Player = Player.playerlist[int(selected_player) - 1]
            sanitized_input = input('Enter the new rank for the player ')
            try:
                if int(sanitized_input) > 0:
                    new_rank = sanitized_input
                    player_to_modify.rank = int(new_rank)
                    player_to_modify.update_player_rank()
                    self.view.display(f'{player_to_modify} rank has been updated to {new_rank}')
                else:
                    self.view.display('Number must be greater than 0')
            except ValueError:
                self.view.display('Please only enter a number superior to 0')
                self.modify_player_rank()
