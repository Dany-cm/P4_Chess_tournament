from models.match import Match
from views.match_view import MatchView


class MatchController(object):

    def __init__(self):
        self.view = MatchView()

    def ask_match_result(self, match: Match):
        ''' Update and display match result'''
        self.view.display_match_result_form(match.match[0][0], match.match[1][0])
        choice = input()

        if choice == '1' or choice == '2' or choice == '3':
            if choice == '1':
                match.match[0][1] = 1
                match.match[1][1] = 0
            elif choice == '2':
                match.match[0][1] = 0
                match.match[1][1] = 1
            elif choice == '3':
                match.match[0][1] = 0,5
                match.match[1][1] = 0,5
            self.view.display('Match result updated successfully')
        else:
            self.view.display('Invalid choice')
            self.ask_match_result(match)
