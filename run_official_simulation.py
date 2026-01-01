#!/usr/bin/env python3
"""
Run simulations using only official Cosmic Encounter aliens.

This script runs games for each player count (2-6) and generates
a detailed statistics table with win rates.
"""

import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from cosmic.simulation.runner import Simulator
from cosmic.types import GameConfig, SimulationConfig
from cosmic.aliens import AlienRegistry
from cosmic.aliens.official_aliens import (
    is_official_alien,
    get_alien_expansion,
    get_all_official_aliens,
    OFFICIAL_ALIENS,
    ALIEN_POWER_DESCRIPTIONS,
)


@dataclass
class OfficialAlienStats:
    """Track statistics for an official alien."""
    name: str
    expansion: str
    description: str = ""

    # Per-player-count stats: {player_count: (wins, games)}
    stats_by_players: Dict[int, Tuple[int, int]] = field(default_factory=dict)

    def add_game(self, player_count: int, won: bool) -> None:
        """Record a game result."""
        if player_count not in self.stats_by_players:
            self.stats_by_players[player_count] = (0, 0)
        wins, games = self.stats_by_players[player_count]
        if won:
            wins += 1
        self.stats_by_players[player_count] = (wins, games + 1)

    def get_win_rate(self, player_count: int) -> float:
        """Get win rate for a specific player count."""
        if player_count not in self.stats_by_players:
            return 0.0
        wins, games = self.stats_by_players[player_count]
        return wins / games if games > 0 else 0.0

    @property
    def total_wins(self) -> int:
        return sum(w for w, g in self.stats_by_players.values())

    @property
    def total_games(self) -> int:
        return sum(g for w, g in self.stats_by_players.values())

    @property
    def overall_win_rate(self) -> float:
        return self.total_wins / self.total_games if self.total_games > 0 else 0.0


def get_official_powers() -> List[str]:
    """Get list of official alien power names that are registered."""
    registered = set(AlienRegistry.get_names())
    official = []

    for alien in get_all_official_aliens():
        # Check various name formats
        names_to_check = [
            alien,
            alien.replace("-", ""),
            alien.replace(" ", ""),
            alien.replace("The ", ""),
            alien.replace(" (Alt)", "_Alt"),
        ]

        for name in names_to_check:
            if name in registered:
                official.append(name)
                break
            # Case-insensitive check
            for reg_name in registered:
                if reg_name.lower() == name.lower():
                    official.append(reg_name)
                    break

    return list(set(official))


def run_simulations(
    games_per_player_count: int = 5000,
    player_counts: List[int] = [2, 3, 4, 5, 6],
) -> Dict[str, OfficialAlienStats]:
    """
    Run simulations for official aliens across player counts.

    Returns dict mapping alien name to OfficialAlienStats.
    """
    # Get official powers that are registered
    official_powers = get_official_powers()
    print(f"Found {len(official_powers)} official aliens registered")

    if not official_powers:
        print("ERROR: No official aliens found in registry!")
        return {}

    # Initialize stats tracking
    alien_stats: Dict[str, OfficialAlienStats] = {}
    for name in official_powers:
        expansion = get_alien_expansion(name) or "Unknown"
        description = ALIEN_POWER_DESCRIPTIONS.get(name, "")
        alien_stats[name] = OfficialAlienStats(
            name=name,
            expansion=expansion,
            description=description,
        )

    total_games = len(player_counts) * games_per_player_count
    games_completed = 0
    start_time = time.time()

    print(f"\nRunning {total_games:,} total games...")
    print(f"  Player counts: {player_counts}")
    print(f"  Games per count: {games_per_player_count:,}")
    print()

    for player_count in player_counts:
        print(f"\n{player_count} players: Running {games_per_player_count:,} games...")
        count_start = time.time()

        config = SimulationConfig(
            num_games=games_per_player_count,
            game_config=GameConfig(num_players=player_count),
            show_progress=False,
            catch_errors=True,
        )

        # Set powers to test to only official ones
        config.powers_to_test = official_powers

        simulator = Simulator(config=config)
        result = simulator.run()

        # Extract per-alien results
        for alien_name, stats in result.statistics.alien_stats.items():
            if alien_name in alien_stats:
                # Record wins and games
                wins_by_count = result.statistics.wins_by_player_count.get(player_count, {})
                wins = wins_by_count.get(alien_name, 0)
                games = stats.games_played

                if games > 0:
                    alien_stats[alien_name].stats_by_players[player_count] = (wins, games)

        count_time = time.time() - count_start
        games_completed += games_per_player_count
        rate = games_per_player_count / count_time if count_time > 0 else 0
        print(f"  Completed in {count_time:.1f}s ({rate:.0f} games/s)")

    total_time = time.time() - start_time
    print(f"\nTotal time: {total_time:.1f}s")
    print(f"Overall speed: {games_completed/total_time:.0f} games/s")

    return alien_stats


def generate_markdown_table(
    alien_stats: Dict[str, OfficialAlienStats],
    player_counts: List[int] = [2, 3, 4, 5, 6],
) -> str:
    """Generate the markdown table with win rate statistics."""

    # Sort by overall win rate
    sorted_aliens = sorted(
        alien_stats.values(),
        key=lambda a: a.overall_win_rate,
        reverse=True
    )

    # Filter to aliens with actual games
    sorted_aliens = [a for a in sorted_aliens if a.total_games > 0]

    lines = []

    # Column explanations
    lines.append("## Win Rate Statistics by Player Count")
    lines.append("")
    lines.append("### Column Descriptions")
    lines.append("")
    lines.append("| Column | Description |")
    lines.append("|--------|-------------|")
    lines.append("| **Rank** | Overall ranking by win rate across all player counts |")
    lines.append("| **Power** | Alien power name (links to detailed rules section) |")
    lines.append("| **Set** | Expansion the alien is from (Base Game, Cosmic Incursion, etc.) |")
    lines.append("| **Overall** | Average win rate across all player counts |")
    lines.append("| **2P** | Win rate in 2-player games (expected: 50%) |")
    lines.append("| **3P** | Win rate in 3-player games (expected: 33%) |")
    lines.append("| **4P** | Win rate in 4-player games (expected: 25%) |")
    lines.append("| **5P** | Win rate in 5-player games (expected: 20%) |")
    lines.append("| **6P** | Win rate in 6-player games (expected: 17%) |")
    lines.append("| **Games** | Total number of games simulated with this alien |")
    lines.append("")
    lines.append("*Note: Win rates above the expected value indicate stronger aliens for that player count.*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table header
    lines.append("### Alien Power Rankings")
    lines.append("")
    header = "| Rank | Power | Set | Overall | 2P | 3P | 4P | 5P | 6P | Games |"
    lines.append(header)
    lines.append("|-----:|:------|:----|--------:|---:|---:|---:|---:|---:|------:|")

    # Table rows
    for rank, alien in enumerate(sorted_aliens, 1):
        power_link = f"[{alien.name}](#{alien.name.lower().replace(' ', '-')})"

        # Format win rates as percentages
        def fmt_rate(rate: float) -> str:
            if rate == 0:
                return "-"
            return f"{rate*100:.1f}%"

        overall = fmt_rate(alien.overall_win_rate)
        rates = [fmt_rate(alien.get_win_rate(pc)) for pc in player_counts]

        row = f"| {rank} | {power_link} | {alien.expansion} | {overall} | "
        row += " | ".join(rates)
        row += f" | {alien.total_games:,} |"
        lines.append(row)

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed rules section
    lines.append("## Alien Power Details")
    lines.append("")

    for alien in sorted_aliens:
        lines.append(f"### {alien.name}")
        lines.append("")
        lines.append(f"**Set:** {alien.expansion}")
        lines.append("")
        if alien.description:
            lines.append(f"**Power:** {alien.description}")
            lines.append("")

        # Stats summary
        lines.append("**Statistics:**")
        lines.append(f"- Overall Win Rate: {alien.overall_win_rate*100:.1f}%")
        lines.append(f"- Total Games: {alien.total_games:,}")
        for pc in player_counts:
            if pc in alien.stats_by_players:
                wins, games = alien.stats_by_players[pc]
                rate = alien.get_win_rate(pc) * 100
                lines.append(f"- {pc}P: {rate:.1f}% ({wins}/{games})")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Run simulations with official Cosmic Encounter aliens"
    )
    parser.add_argument(
        "-n", "--games-per-count",
        type=int,
        default=5000,
        help="Games per player count (default: 5000)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="STATISTICS.md",
        help="Output markdown file (default: STATISTICS.md)"
    )
    parser.add_argument(
        "--min-players",
        type=int,
        default=2,
        help="Minimum player count (default: 2)"
    )
    parser.add_argument(
        "--max-players",
        type=int,
        default=6,
        help="Maximum player count (default: 6)"
    )

    args = parser.parse_args()

    player_counts = list(range(args.min_players, args.max_players + 1))

    print("=" * 60)
    print("COSMIC ENCOUNTER OFFICIAL ALIEN SIMULATION")
    print("=" * 60)

    # Run simulations
    stats = run_simulations(
        games_per_player_count=args.games_per_count,
        player_counts=player_counts,
    )

    if not stats:
        print("No results to report!")
        return 1

    # Generate markdown
    markdown = generate_markdown_table(stats, player_counts)

    # Save to file
    output_path = Path(args.output)
    with open(output_path, "w") as f:
        f.write("# Cosmic Encounter Alien Win Rates\n\n")
        f.write("*Generated by automated simulation*\n\n")
        f.write(markdown)

    print(f"\nResults saved to {output_path}")

    # Print top 10
    print("\n" + "=" * 60)
    print("TOP 10 ALIENS BY WIN RATE")
    print("=" * 60)

    sorted_stats = sorted(
        stats.values(),
        key=lambda a: a.overall_win_rate,
        reverse=True
    )[:10]

    for i, alien in enumerate(sorted_stats, 1):
        print(f"{i:2}. {alien.name:20} {alien.overall_win_rate*100:5.1f}% ({alien.total_games} games)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
