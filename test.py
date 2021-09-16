from models.rounds import Round
from models.players import Player
from models.match import Match
from models.tournament import Tournament
from controllers.match_controller import MatchController
import datetime


class Test(object):
    @staticmethod
    def test():

        player = Player('C', 'Dany', '10/10/1000', 'M', 1000, 1)
        player2 = Player('Z', 'Q', '10/10/1000', 'M', 2000, 2)
        player3 = Player('E', 'S', '10/10/1000', 'M', 5000, 3)
        player4 = Player('R', 'D', '10/10/1000', 'M', 3000, 4)
        player5 = Player('T', 'F', '10/10/1000', 'M', 9000, 5)
        player6 = Player('Y', 'G', '10/10/1000', 'M', 6000, 6)
        player7 = Player('fdfdf', 'rererer', '10/10/1000', 'M', 2, 7)

        match1 = Match(player, player2)
        match2 = Match(player3, player4)
        match3 = Match(player5, player6)

        match4 = Match(player5, player4)
        match5 = Match(player2, player3)
        match6 = Match(player, player6)

        testround = Round('test1', match_list=[match1, match2, match3])
        testround2 = Round('test2', match_list=[match4, match5, match6])
        testround.finish_round()
        testround2.finish_round()

        tournament1 = Tournament('test1', 'test', datetime.datetime.today(), datetime.datetime.now(), [player, player2, player3, player4, player5, player6], [testround, testround2], 'test','ee',1,4)

        print('d')
        tournament1.sorted_player_score()
        print(tournament1.player_list)
        """ print(testround.get_player_score(player))
        print(testround.get_player_score(player3))
        print(testround.get_player_score(player7)) """