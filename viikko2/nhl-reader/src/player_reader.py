import requests

from player import Player


# pylint: disable=too-few-public-methods
class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()

        players_data = response.json()

        players = []

        for player_dict in players_data:
            player = Player(player_dict)
            players.append(player)

        return players
    