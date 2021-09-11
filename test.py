from models.players import Player
from models.match import Match
from controllers.match_controller import MatchController


class Test(object):
    @staticmethod
    def test():

        player = Player('C','Dany','10/10/1000','M',1,4)
        player2 = Player('P','Kevin','10/10/1000','M',2,2)

        match = Match(player, player2)
        print(f'TEST : {match}')

        match1 = MatchController()
        match1.ask_match_result(match)
        print(match1)
