from dataclasses import dataclass


@dataclass
class Tournament():
        name: str
        location: str
        start_date: str
        end_date: str
        player_list: list
        round_list: list
        control_time: int
        description: str
        id: int
        number_of_round: int = 4

def serialized_tournament(tournament):
    return {
        'name': tournament.name,
        'location': tournament.location,
        'start_date': tournament.start_date,
        'end_date': tournament.end_date,
        'player_list': tournament.player_list,
        'round_list': tournament.round_list,
        'control_time': tournament.control_time,
        'description': tournament.description,
        'id': tournament.id,
        'number_of_round': tournament.number_of_round,
    }