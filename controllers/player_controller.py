from models.players import Player
from views.player_view import PlayerView


class player_controller():

    def __init__(self):
        self.view = PlayerView()

    def create_new_player(self):
        self.view.ask_information('Last name')
        lastname = input()
        self.view.ask_information('First name')
        firstname = input()
        self.view.ask_information('Birth date (DD/MM/YYYY)')
        dob = input()
        self.view.ask_information('Sex (M/F)')
        sex = input()
        self.view.ask_information('Rank')
        rank = input()

        self.model = Player(lastname=lastname, firstname=firstname, dob=dob, sex=sex,  id=id, rank=rank)

        if  self.model.create_new_player(lastname, firstname, dob, sex, rank):
            self.view.display(f'{lastname} {firstname} has been created.')
        else:
            self.view.display('Invalid data. try again')
            self.create_new_player()
