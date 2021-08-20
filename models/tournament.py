class Tournament:
    def __init__(self, name, location, date, player_list, control_time, description, number_of_round=4, round_list=None):

        self.name = name
        self.place = location
        self.date = date
        self.number_of_round = number_of_round
        self.round_list = round_list
        self.player_list = player_list
        self.control_time = control_time
        self.description = description