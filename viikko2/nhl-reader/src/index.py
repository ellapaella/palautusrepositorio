
from player_reader import PlayerReader
from player_stats import PlayerStats

from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    # Ask the user for the season
    season = input("Season (e.g. 2024-25): ")

    # Ask the user for nationality
    nationality = input("Nationality (e.g. FIN): ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    # Create a Rich table
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Player", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="green", justify="right")
    table.add_column("Assists", style="green", justify="right")
    table.add_column("Points", style="green", justify="right")

    # Add players to the table
    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
        )

    # Display the table
    console.print(table)


if __name__ == "__main__":
    main()
