"""
Game balance analysis tools for Cosmic Encounter simulator.

Provides tools for analyzing power balance, identifying outliers,
and generating balance reports.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, TYPE_CHECKING
from collections import defaultdict
import math
import json

if TYPE_CHECKING:
    from ..simulation.stats import Statistics


@dataclass
class PowerBalanceData:
    """Balance data for a single alien power."""
    name: str
    games_played: int
    win_rate: float
    elo_rating: float
    solo_wins: int
    shared_wins: int
    z_score: float = 0.0  # Standard deviations from mean
    balance_tier: str = "Normal"  # Overpowered, Strong, Normal, Weak, Underpowered


@dataclass
class BalanceReport:
    """Full balance analysis report."""
    total_powers: int
    mean_win_rate: float
    std_dev: float
    median_win_rate: float

    overpowered: List[PowerBalanceData] = field(default_factory=list)
    strong: List[PowerBalanceData] = field(default_factory=list)
    normal: List[PowerBalanceData] = field(default_factory=list)
    weak: List[PowerBalanceData] = field(default_factory=list)
    underpowered: List[PowerBalanceData] = field(default_factory=list)

    # Special categories
    alternate_win_aliens: List[PowerBalanceData] = field(default_factory=list)
    high_variance_aliens: List[PowerBalanceData] = field(default_factory=list)

    def summary(self) -> str:
        """Generate text summary of balance report."""
        lines = [
            "=" * 60,
            "COSMIC ENCOUNTER BALANCE REPORT",
            "=" * 60,
            "",
            f"Total Powers Analyzed: {self.total_powers}",
            f"Mean Win Rate: {self.mean_win_rate*100:.1f}%",
            f"Standard Deviation: {self.std_dev*100:.2f}%",
            f"Median Win Rate: {self.median_win_rate*100:.1f}%",
            "",
            "-" * 60,
            "BALANCE DISTRIBUTION",
            "-" * 60,
            f"Overpowered (>2σ):  {len(self.overpowered)}",
            f"Strong (1-2σ):      {len(self.strong)}",
            f"Normal (-1 to 1σ):  {len(self.normal)}",
            f"Weak (-2 to -1σ):   {len(self.weak)}",
            f"Underpowered (<-2σ): {len(self.underpowered)}",
            "",
        ]

        if self.overpowered:
            lines.extend([
                "-" * 60,
                "OVERPOWERED ALIENS (Need Nerfs)",
                "-" * 60,
            ])
            for p in self.overpowered[:10]:
                lines.append(f"  {p.name:20} {p.win_rate*100:.1f}% (z={p.z_score:+.2f})")

        if self.underpowered:
            lines.extend([
                "",
                "-" * 60,
                "UNDERPOWERED ALIENS (Need Buffs)",
                "-" * 60,
            ])
            for p in self.underpowered[:10]:
                lines.append(f"  {p.name:20} {p.win_rate*100:.1f}% (z={p.z_score:+.2f})")

        if self.alternate_win_aliens:
            lines.extend([
                "",
                "-" * 60,
                "ALTERNATE WIN CONDITION ALIENS",
                "-" * 60,
            ])
            for p in self.alternate_win_aliens[:10]:
                lines.append(f"  {p.name:20} {p.win_rate*100:.1f}%")

        return "\n".join(lines)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON export."""
        return {
            "summary": {
                "total_powers": self.total_powers,
                "mean_win_rate": self.mean_win_rate,
                "std_dev": self.std_dev,
                "median_win_rate": self.median_win_rate,
            },
            "distribution": {
                "overpowered": len(self.overpowered),
                "strong": len(self.strong),
                "normal": len(self.normal),
                "weak": len(self.weak),
                "underpowered": len(self.underpowered),
            },
            "overpowered": [{"name": p.name, "win_rate": p.win_rate, "z_score": p.z_score}
                          for p in self.overpowered],
            "underpowered": [{"name": p.name, "win_rate": p.win_rate, "z_score": p.z_score}
                           for p in self.underpowered],
        }


class BalanceAnalyzer:
    """Analyzes game balance from simulation statistics."""

    # Known alternate win condition aliens
    ALTERNATE_WIN_ALIENS = {
        "Tick", "Masochist", "Anarchist", "Lizard", "The Meek",
        "Pacifist", "Mouth", "Glutton", "Loser", "Philanthropist"
    }

    def __init__(self, min_games: int = 100):
        """
        Initialize analyzer.

        Args:
            min_games: Minimum games required to include power in analysis
        """
        self.min_games = min_games

    def analyze(self, stats: "Statistics") -> BalanceReport:
        """
        Analyze power balance from statistics.

        Args:
            stats: Statistics object with alien performance data

        Returns:
            BalanceReport with analysis results
        """
        # Filter to powers with enough games
        valid_powers = []
        for name, alien_data in stats.alien_stats.items():
            if alien_data.games_played >= self.min_games:
                # win_rate is a property that returns 0-1, but old data might be 0-100
                wr = alien_data.win_rate
                if wr > 1:  # Assume it's a percentage
                    wr = wr / 100
                valid_powers.append(PowerBalanceData(
                    name=alien_data.name,
                    games_played=alien_data.games_played,
                    win_rate=wr,
                    elo_rating=getattr(alien_data, 'elo_rating', 1000),
                    solo_wins=alien_data.solo_wins,
                    shared_wins=alien_data.shared_wins,
                ))

        if not valid_powers:
            return BalanceReport(
                total_powers=0,
                mean_win_rate=0,
                std_dev=0,
                median_win_rate=0,
            )

        # Calculate statistics
        win_rates = [p.win_rate for p in valid_powers]
        mean_wr = sum(win_rates) / len(win_rates)
        variance = sum((wr - mean_wr) ** 2 for wr in win_rates) / len(win_rates)
        std_dev = math.sqrt(variance)

        sorted_rates = sorted(win_rates)
        mid = len(sorted_rates) // 2
        median = sorted_rates[mid] if len(sorted_rates) % 2 else (sorted_rates[mid-1] + sorted_rates[mid]) / 2

        # Calculate z-scores and categorize
        for power in valid_powers:
            if std_dev > 0:
                power.z_score = (power.win_rate - mean_wr) / std_dev
            else:
                power.z_score = 0

            # Assign balance tier
            if power.z_score > 2:
                power.balance_tier = "Overpowered"
            elif power.z_score > 1:
                power.balance_tier = "Strong"
            elif power.z_score > -1:
                power.balance_tier = "Normal"
            elif power.z_score > -2:
                power.balance_tier = "Weak"
            else:
                power.balance_tier = "Underpowered"

        # Sort by z-score
        valid_powers.sort(key=lambda p: -p.z_score)

        # Build report
        report = BalanceReport(
            total_powers=len(valid_powers),
            mean_win_rate=mean_wr,
            std_dev=std_dev,
            median_win_rate=median,
        )

        for power in valid_powers:
            if power.balance_tier == "Overpowered":
                report.overpowered.append(power)
            elif power.balance_tier == "Strong":
                report.strong.append(power)
            elif power.balance_tier == "Normal":
                report.normal.append(power)
            elif power.balance_tier == "Weak":
                report.weak.append(power)
            else:
                report.underpowered.append(power)

            # Check for alternate win aliens
            if power.name in self.ALTERNATE_WIN_ALIENS:
                report.alternate_win_aliens.append(power)

        return report

    def analyze_from_file(self, filepath: str) -> BalanceReport:
        """Analyze from a JSON stats file."""
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Create a mock statistics object
        from ..simulation.stats import Statistics, AlienStats
        stats = Statistics()

        if "alien_stats" in data:
            for name, alien_data in data["alien_stats"].items():
                stats.alien_stats[name] = AlienStats(
                    name=alien_data.get("name", name),
                    games_played=alien_data.get("games_played", 0),
                    games_won=alien_data.get("games_won", 0),
                    solo_wins=alien_data.get("solo_wins", 0),
                    shared_wins=alien_data.get("shared_wins", 0),
                )

        return self.analyze(stats)


def compare_power_matchups(stats: "Statistics", power1: str, power2: str) -> Dict:
    """
    Compare two powers head-to-head.

    Returns matchup statistics if available.
    """
    # This would require tracking head-to-head stats in the Statistics class
    # For now, return basic comparison
    p1 = stats.alien_stats.get(power1)
    p2 = stats.alien_stats.get(power2)

    if not p1 or not p2:
        return {"error": "One or both powers not found"}

    return {
        "power1": {
            "name": p1.name,
            "win_rate": p1.win_rate,
            "games": p1.games_played,
            "elo": p1.elo_rating,
        },
        "power2": {
            "name": p2.name,
            "win_rate": p2.win_rate,
            "games": p2.games_played,
            "elo": p2.elo_rating,
        },
        "comparison": {
            "win_rate_diff": p1.win_rate - p2.win_rate,
            "elo_diff": p1.elo_rating - p2.elo_rating,
            "predicted_winner": p1.name if p1.elo_rating > p2.elo_rating else p2.name,
        }
    }


def identify_power_synergies(stats: "Statistics", min_games: int = 50) -> List[Tuple[str, str, float]]:
    """
    Identify alien power pairs that work well together (as allies).

    This would require tracking ally combinations in statistics.
    For now, returns empty list as placeholder.
    """
    # TODO: Implement when Statistics tracks ally combinations
    return []


def calculate_player_count_balance(stats: "Statistics") -> Dict[int, float]:
    """
    Analyze how player count affects game balance.

    Returns win rate variance by player count.
    """
    # Get games by player count
    games_by_count = defaultdict(int)
    for count, games in stats.games_by_player_count.items():
        games_by_count[int(count)] = games

    # For now, return the distribution
    total = sum(games_by_count.values())
    return {
        count: games / total if total > 0 else 0
        for count, games in sorted(games_by_count.items())
    }
