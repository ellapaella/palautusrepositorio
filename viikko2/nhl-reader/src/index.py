
from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()

    season, nationality = get_user_input()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        console.print("No players found!", style="bold red")
        return

    table = create_player_table(players, season, nationality)
    console.print(table)

def create_player_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Player", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="green", justify="right")
    table.add_column("Assists", style="green", justify="right")
    table.add_column("Points", style="green", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
        )

    return table

def get_user_input():
    season = input("Season (e.g. 2024-25): ")
    nationality = input("Nationality (e.g. FIN): ")

    return season, nationality

if __name__ == "__main__":
    main()
