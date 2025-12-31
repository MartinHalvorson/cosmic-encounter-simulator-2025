"""
Power synergy analysis for Cosmic Encounter simulator.

Analyzes how alien powers perform together as allies or against each other.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Set, TYPE_CHECKING
from collections import defaultdict
import math
import json

if TYPE_CHECKING:
    from ..simulation.stats import Statistics


@dataclass
class SynergyData:
    """Synergy data for a power pair."""
    power1: str
    power2: str
    games_together: int = 0
    combined_wins: int = 0
    power1_solo_wins: int = 0
    power2_solo_wins: int = 0

    @property
    def synergy_win_rate(self) -> float:
        if self.games_together == 0:
            return 0.0
        return self.combined_wins / self.games_together

    @property
    def synergy_score(self) -> float:
        """Calculate synergy score (positive = good synergy, negative = anti-synergy)."""
        if self.games_together < 10:
            return 0.0
        # Compare combined performance to individual performance
        expected = 0.4  # Expected win rate for 2 of 5 players
        actual = self.synergy_win_rate
        return (actual - expected) * 100  # Percentage points above/below expected


@dataclass
class CounterData:
    """Counter matchup data for a power pair."""
    power1: str
    power2: str
    games_against: int = 0
    power1_wins: int = 0
    power2_wins: int = 0

    @property
    def power1_win_rate(self) -> float:
        if self.games_against == 0:
            return 0.5
        return self.power1_wins / self.games_against

    @property
    def counter_score(self) -> float:
        """How much power1 counters power2 (positive = good counter)."""
        if self.games_against < 10:
            return 0.0
        # Compare to 50/50 baseline
        return (self.power1_win_rate - 0.5) * 100


@dataclass
class SynergyReport:
    """Full synergy analysis report."""
    powers_analyzed: int
    total_matchups: int

    best_synergies: List[SynergyData] = field(default_factory=list)
    worst_synergies: List[SynergyData] = field(default_factory=list)
    best_counters: List[CounterData] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            "=" * 60,
            "COSMIC ENCOUNTER SYNERGY REPORT",
            "=" * 60,
            "",
            f"Powers Analyzed: {self.powers_analyzed}",
            f"Total Matchups: {self.total_matchups}",
            "",
        ]

        if self.best_synergies:
            lines.extend([
                "-" * 60,
                "BEST ALLY SYNERGIES",
                "-" * 60,
            ])
            for s in self.best_synergies[:15]:
                lines.append(
                    f"  {s.power1:15} + {s.power2:15} = {s.synergy_win_rate*100:.1f}% "
                    f"(+{s.synergy_score:.1f}pp)"
                )

        if self.worst_synergies:
            lines.extend([
                "",
                "-" * 60,
                "WORST ALLY COMBINATIONS (Anti-synergy)",
                "-" * 60,
            ])
            for s in self.worst_synergies[:15]:
                lines.append(
                    f"  {s.power1:15} + {s.power2:15} = {s.synergy_win_rate*100:.1f}% "
                    f"({s.synergy_score:.1f}pp)"
                )

        if self.best_counters:
            lines.extend([
                "",
                "-" * 60,
                "BEST COUNTERS (Power1 counters Power2)",
                "-" * 60,
            ])
            for c in self.best_counters[:15]:
                lines.append(
                    f"  {c.power1:15} vs {c.power2:15} = {c.power1_win_rate*100:.1f}% "
                    f"(+{c.counter_score:.1f}pp)"
                )

        return "\n".join(lines)


class SynergyAnalyzer:
    """Analyzes power synergies from simulation data."""

    def __init__(self, min_games: int = 20):
        """
        Initialize analyzer.

        Args:
            min_games: Minimum games required for valid synergy data
        """
        self.min_games = min_games
        self.synergy_matrix: Dict[Tuple[str, str], SynergyData] = {}
        self.counter_matrix: Dict[Tuple[str, str], CounterData] = {}

    def record_game(
        self,
        powers: List[str],
        winner_indices: List[int],
        ally_pairs: List[Tuple[int, int]] = None
    ) -> None:
        """
        Record a game for synergy analysis.

        Args:
            powers: List of alien power names for each player
            winner_indices: Indices of winning players
            ally_pairs: Optional list of (player1_idx, player2_idx) ally pairs
        """
        n = len(powers)

        # Record counter matchups (who beat whom)
        for i in range(n):
            for j in range(i + 1, n):
                key = tuple(sorted([powers[i], powers[j]]))
                if key not in self.counter_matrix:
                    self.counter_matrix[key] = CounterData(
                        power1=key[0], power2=key[1]
                    )

                data = self.counter_matrix[key]
                data.games_against += 1

                # Check who won
                i_won = i in winner_indices
                j_won = j in winner_indices

                if i_won and not j_won:
                    if powers[i] == key[0]:
                        data.power1_wins += 1
                    else:
                        data.power2_wins += 1
                elif j_won and not i_won:
                    if powers[j] == key[0]:
                        data.power1_wins += 1
                    else:
                        data.power2_wins += 1

        # Record synergy (shared wins)
        if ally_pairs:
            for i, j in ally_pairs:
                key = tuple(sorted([powers[i], powers[j]]))
                if key not in self.synergy_matrix:
                    self.synergy_matrix[key] = SynergyData(
                        power1=key[0], power2=key[1]
                    )

                data = self.synergy_matrix[key]
                data.games_together += 1

                # Check if both won (shared victory)
                if i in winner_indices and j in winner_indices:
                    data.combined_wins += 1

    def analyze(self) -> SynergyReport:
        """Generate synergy report from recorded data."""
        # Filter synergies with enough games
        valid_synergies = [
            s for s in self.synergy_matrix.values()
            if s.games_together >= self.min_games
        ]
        valid_counters = [
            c for c in self.counter_matrix.values()
            if c.games_against >= self.min_games
        ]

        # Sort by synergy/counter score
        valid_synergies.sort(key=lambda s: -s.synergy_score)
        valid_counters.sort(key=lambda c: -c.counter_score)

        # Build report
        report = SynergyReport(
            powers_analyzed=len(set(
                [s.power1 for s in valid_synergies] +
                [s.power2 for s in valid_synergies]
            )),
            total_matchups=len(valid_synergies) + len(valid_counters),
        )

        # Best and worst synergies
        report.best_synergies = valid_synergies[:20]
        report.worst_synergies = list(reversed(valid_synergies[-20:]))

        # Best counters
        report.best_counters = valid_counters[:20]

        return report


# Power categories for thematic synergy suggestions
POWER_CATEGORIES = {
    "combat_boost": {
        "Warrior", "Human", "Virus", "Macron", "Titan", "Giant",
        "Veteran", "Champion", "Aggressor", "Cavalry", "Infantry"
    },
    "card_manipulation": {
        "Oracle", "Mind", "Seer", "Visionary", "CardShark", "Hoarder",
        "Inspector", "Revealer", "Exchanger", "Doubler"
    },
    "defense": {
        "Defender", "Guardian", "Shield", "Wall", "Fortress", "Rampart",
        "Guerrilla", "Bunker", "Citadel"
    },
    "alliance": {
        "Extrovert", "Charmer", "Diplomat", "General", "Marshal",
        "Ally", "Recruiter", "Coalition"
    },
    "disruption": {
        "Virus", "Fungus", "Parasite", "Saboteur", "Anarchist",
        "Chaos", "Scrambler", "Disruptor"
    },
}


def suggest_synergies(power_name: str) -> List[str]:
    """
    Suggest powers that might synergize with the given power.

    Based on thematic categories and power types.
    """
    suggestions = []

    # Find what category this power belongs to
    power_categories = []
    for category, powers in POWER_CATEGORIES.items():
        if power_name in powers:
            power_categories.append(category)

    # Suggest powers from complementary categories
    complementary = {
        "combat_boost": ["defense", "alliance"],
        "card_manipulation": ["combat_boost", "disruption"],
        "defense": ["combat_boost", "alliance"],
        "alliance": ["combat_boost", "defense"],
        "disruption": ["card_manipulation", "combat_boost"],
    }

    for cat in power_categories:
        for comp_cat in complementary.get(cat, []):
            suggestions.extend(list(POWER_CATEGORIES.get(comp_cat, set())))

    # Remove duplicates and the original power
    suggestions = list(set(suggestions) - {power_name})

    return suggestions[:10]  # Return top 10 suggestions
