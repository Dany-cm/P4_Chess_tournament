from models.rounds import Round
from models.players import Player
from models.match import Match
from controllers.match_controller import MatchController


class Test(object):
    @staticmethod
    def test():

        player = Player('C', 'Dany', '10/10/1000', 'M', 1, 1)
        player2 = Player('Z', 'Q', '10/10/1000', 'M', 2, 2)
        player3 = Player('E', 'S', '10/10/1000', 'M', 2, 3)
        player4 = Player('R', 'D', '10/10/1000', 'M', 2, 4)
        player5 = Player('T', 'F', '10/10/1000', 'M', 2, 5)
        player6 = Player('Y', 'G', '10/10/1000', 'M', 2, 6)
        player7 = Player('fdfdf', 'rererer', '10/10/1000', 'M', 2, 7)

        match1 = Match(player, player2)
        match2 = Match(player3, player4)
        match3 = Match(player5, player6)

        testround = Round('test1', match_list=[match1, match2, match3])
        testround.finish_round()

        print(testround.get_player_score(player))
        print(testround.get_player_score(player3))
        print(testround.get_player_score(player7))