from models.players import Player
from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController():

    def __init__(self):
        self.view = TournamentView()

    def create_new_tournament(self):
        ''' Ask user to fill out information and save it '''
        questions = ['Name', 'Location name', 'Start date (DD/MM/YYYY)', 'Time control (Bullet, Blitz or Rapid)',
                     'Description', 'Number of round (4 by default)']
        results = []
        for question in questions:
            self.view.ask_information(question)
            result = input()
            results.append(result)

        self.model = Tournament(results[0], results[1], results[2], results[3], results[4], int(results[5]))

        if self.model.create_new_tournament(results[0], results[1], results[2],
                                            results[3], results[4], int(results[5])):
            self.view.display(f'Tournament: {results[0]} {results[1]} {results[2]} \n'
                              f'{results[3]} {results[4]} {results[5]} has been created.')
        else:
            self.view.display('Invalid data. try again')
            self.create_new_tournament()

    def add_players_to_tournament(self):
        ''' Ask user to add players to a valid tournament.'''
        tournaments_without_players = list(filter(lambda current_tournament: not current_tournament.player_list,
                                           Tournament.tournamentlist))

        if not tournaments_without_players:
            self.view.display('There is no tournaments to which you can add players')
            return

        if len(Player.playerlist) < 8:
            self.view.display('You need at least 8 players in the application to do this')
            return

        self.view.display_tournaments_name(tournaments_without_players)

        choice = ''
        while (not (choice.isdigit() and int(choice) >= 1 and int(choice) <= len(tournaments_without_players))):
            choice = input()

        tournament_to_modify: Tournament = tournaments_without_players[int(choice) - 1]

        self.view.display_players_name(Player.playerlist)

        is_input_correct = False
        while (not is_input_correct):
            is_input_correct = True
            choice = input()
            selected_numbers = choice.split(',')

            if not len(selected_numbers) == 8:
                is_input_correct = False
            elif any(selected_numbers.count(number) > 1 for number in selected_numbers):
                is_input_correct = False
            elif any(not (number.isdigit() and int(number) >= 1 and int(number) <= len(Player.playerlist))
                     for number in selected_numbers):
                is_input_correct = False

        tournament_to_modify.player_list = []
        for player_number in selected_numbers:
            tournament_to_modify.player_list.append(Player.playerlist[int(player_number) - 1])

        Tournament.save_tournaments()

    def start_tournament(self):
        ''' Start tournament '''
        tournaments_with_players = list(filter(lambda current_tournament: current_tournament.player_list
                                        and not current_tournament.round_list, Tournament.tournamentlist))

        if not tournaments_with_players:
            self.view.display('There is no tournaments that can be started')
            return

        self.view.display_tournaments_name(tournaments_with_players)

        correct = False
        while (not correct):
            selection = input()
            correct = selection.isdigit() and int(selection) >= 1 and int(selection) <= len(Tournament.tournamentlist)

        tournament_to_start: Tournament = tournaments_with_players[int(selection) - 1]
        tournament_to_start.create_new_round()

        Tournament.save_tournaments()

    def finish_in_progress_round(self):
        ''' Finish the round in progress '''
        tournaments_in_progress = list(filter(lambda current_tournament: current_tournament.round_list
                                              and not current_tournament.is_tournament_finished,
                                              Tournament.tournamentlist))

        if not tournaments_in_progress:
            self.view.display('There is no tournament in progress')
            return

        self.view.display_tournaments_name(tournaments_in_progress)

        correct = False
        while (not correct):
            selection = input()
            correct = selection.isdigit() and int(selection) >= 1 and int(selection) <= len(Tournament.tournamentlist)

        tournament_to_resume: Tournament = tournaments_in_progress[int(selection) - 1]
        tournament_to_resume.round_list[len(tournament_to_resume.round_list) - 1].finish_round()

        if tournament_to_resume.number_of_round <= len(tournament_to_resume.round_list):
            for player in tournament_to_resume.player_list:
                correct = False
                while (not correct):
                    sanitized_input = input(f'Enter the new rank for {player}:')
                    try:
                        if int(sanitized_input) > 0:
                            new_rank = sanitized_input
                            player.rank = int(new_rank)
                            player.update_player_rank()
                            self.view.display(f'{player} rank has been updated to {new_rank}')
                            correct = True
                        else:
                            self.view.display('Number must be greater than 0')
                    except ValueError:
                        self.view.display('Please only enter a number superior to 0')
            tournament_to_resume.is_tournament_finished = True
        else:
            tournament_to_resume.create_new_round()

        Tournament.save_tournaments()
