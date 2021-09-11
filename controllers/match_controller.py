from models.match import Match
from views.match_view import MatchView

class MatchController(object):

    def __init__(self):
        self.view = MatchView()

    def ask_match_result(self, match: Match):
        self.view.display_match_result_form(match.match[0][0], match.match[1][0])
        choice = input()

        if choice == '1' or choice == '2' or choice == '3':
            self.view.display('Match result updated successfully')
        else:
            self.view.display('Invalid choice')
            self.ask_match_result(match)


