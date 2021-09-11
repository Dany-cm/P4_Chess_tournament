from dataclasses import dataclass


@dataclass
class Round():
    round_name: str
    match_list: list
    player: str
    start_date: str
    end_date: str
