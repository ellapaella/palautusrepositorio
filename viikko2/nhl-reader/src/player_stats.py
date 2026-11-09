class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)

        return sorted(nationality_players, key=lambda player: player.points(), reverse=True)