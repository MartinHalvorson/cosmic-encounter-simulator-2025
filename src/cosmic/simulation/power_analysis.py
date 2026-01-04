"""
Power Balance Analysis Tools for Cosmic Encounter.

Provides comprehensive analysis of alien power performance including:
- Tier classification based on win rates and ELO
- Performance comparison across player counts
- Power balance metrics
- Statistical significance testing
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any
from enum import Enum, auto
import math

from .cumulative_stats import CumulativeStats, AlienEloStats


class PowerTier(Enum):
    """Power tier classification."""
    S = "S"  # Top tier (>30% win rate in 5-player)
    A = "A"  # Strong (25-30%)
    B = "B"  # Above average (22-25%)
    C = "C"  # Average (18-22%)
    D = "D"  # Below average (15-18%)
    F = "F"  # Weak (<15%)


@dataclass
class PowerAnalysis:
    """Analysis results for a single alien power."""
    name: str
    games_played: int
    win_rate: float
    solo_win_rate: float
    normalized_win_rate: float  # Compared to expected (1/num_players)
    tier: PowerTier
    elo_rating: float
    performance_score: float  # Combined metric
    confidence_interval: Tuple[float, float]  # 95% CI for win rate


@dataclass
class BalanceReport:
    """Complete balance analysis report."""
    analyses: Dict[str, PowerAnalysis] = field(default_factory=dict)
    total_games: int = 0
    expected_win_rate: float = 0.2  # For 5 players

    # Tier distributions
    tier_counts: Dict[PowerTier, int] = field(default_factory=dict)
    tier_members: Dict[PowerTier, List[str]] = field(default_factory=dict)

    # Balance metrics
    balance_score: float = 0.0  # 0-100, higher = more balanced
    gini_coefficient: float = 0.0  # Inequality measure
    win_rate_std: float = 0.0
    overpowered: List[str] = field(default_factory=list)
    underpowered: List[str] = field(default_factory=list)


class PowerBalanceAnalyzer:
    """
    Analyzes power balance across alien powers.
    """

    def __init__(self, min_games: int = 100):
        """
        Args:
            min_games: Minimum games required for statistical significance
        """
        self.min_games = min_games

    def analyze(self, stats: CumulativeStats) -> BalanceReport:
        """
        Perform comprehensive balance analysis.

        Args:
            stats: Cumulative statistics to analyze

        Returns:
            BalanceReport with analysis results
        """
        report = BalanceReport()
        report.total_games = stats.total_games

        # Determine expected win rate based on average player count
        total_player_games = sum(
            count * players
            for players, count in stats.games_by_player_count.items()
        )
        avg_players = total_player_games / max(1, stats.total_games)
        report.expected_win_rate = 1.0 / avg_players if avg_players > 0 else 0.2

        # Analyze each alien
        win_rates = []
        for name, alien_stats in stats.alien_stats.items():
            if alien_stats.games_played < self.min_games:
                continue

            analysis = self._analyze_alien(
                alien_stats, report.expected_win_rate
            )
            report.analyses[name] = analysis
            win_rates.append(analysis.win_rate)

        # Calculate balance metrics
        if win_rates:
            report.win_rate_std = self._std(win_rates)
            report.gini_coefficient = self._gini(win_rates)
            report.balance_score = self._calculate_balance_score(
                win_rates, report.expected_win_rate
            )

        # Classify into tiers
        self._classify_tiers(report)

        # Identify outliers
        self._identify_outliers(report)

        return report

    def _analyze_alien(
        self,
        stats: AlienEloStats,
        expected_wr: float
    ) -> PowerAnalysis:
        """Analyze a single alien power."""
        # Calculate confidence interval for win rate
        ci_low, ci_high = self._wilson_ci(
            stats.games_won, stats.games_played
        )

        # Normalized win rate (how much better/worse than expected)
        normalized_wr = stats.win_rate / expected_wr if expected_wr > 0 else 1.0

        # Performance score (combines multiple factors)
        perf_score = self._calculate_performance_score(
            stats.win_rate,
            stats.solo_win_rate,
            normalized_wr,
            stats.elo_rating
        )

        # Determine tier
        tier = self._get_tier(stats.win_rate, expected_wr)

        return PowerAnalysis(
            name=stats.name,
            games_played=stats.games_played,
            win_rate=stats.win_rate,
            solo_win_rate=stats.solo_win_rate,
            normalized_win_rate=normalized_wr,
            tier=tier,
            elo_rating=stats.elo_rating,
            performance_score=perf_score,
            confidence_interval=(ci_low, ci_high)
        )

    def _get_tier(self, win_rate: float, expected: float) -> PowerTier:
        """Classify power into a tier based on win rate."""
        ratio = win_rate / expected if expected > 0 else 1.0

        if ratio >= 1.5:  # 50% better than expected
            return PowerTier.S
        elif ratio >= 1.25:  # 25% better
            return PowerTier.A
        elif ratio >= 1.1:  # 10% better
            return PowerTier.B
        elif ratio >= 0.9:  # Within 10%
            return PowerTier.C
        elif ratio >= 0.75:  # 25% worse
            return PowerTier.D
        else:
            return PowerTier.F

    def _wilson_ci(
        self,
        successes: int,
        total: int,
        z: float = 1.96
    ) -> Tuple[float, float]:
        """
        Calculate Wilson score confidence interval.
        More accurate than normal approximation for proportions.
        """
        if total == 0:
            return (0.0, 0.0)

        p = successes / total
        n = total

        # Wilson score interval
        denominator = 1 + z * z / n
        center = (p + z * z / (2 * n)) / denominator
        margin = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denominator

        return (max(0, center - margin), min(1, center + margin))

    def _calculate_performance_score(
        self,
        win_rate: float,
        solo_rate: float,
        normalized: float,
        elo: float
    ) -> float:
        """Calculate combined performance score (0-100)."""
        # Weight different factors
        wr_component = win_rate * 100 * 2  # 0-40 for typical range
        solo_component = solo_rate * 100  # 0-20 for typical range

        # Normalize ELO (typical range 1000-2000, centered at 1500)
        # Scale so that 1500 = 0, and each 100 ELO = 2 points
        elo_normalized = (elo - 1500) / 50  # -10 to +10 for typical range

        # Combine
        score = (
            wr_component * 0.5 +
            solo_component * 0.3 +
            elo_normalized * 0.2 + 10  # Add 10 to center at baseline
        )

        return max(0, min(100, score))

    def _std(self, values: List[float]) -> float:
        """Calculate standard deviation."""
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)

    def _gini(self, values: List[float]) -> float:
        """
        Calculate Gini coefficient for inequality measurement.
        0 = perfect equality, 1 = perfect inequality
        """
        if not values or len(values) < 2:
            return 0.0

        sorted_vals = sorted(values)
        n = len(sorted_vals)
        total = sum(sorted_vals)

        if total == 0:
            return 0.0

        cumulative = 0
        gini_sum = 0
        for i, val in enumerate(sorted_vals):
            cumulative += val
            gini_sum += (i + 1) * val

        gini = (2 * gini_sum) / (n * total) - (n + 1) / n
        return max(0, min(1, gini))

    def _calculate_balance_score(
        self,
        win_rates: List[float],
        expected: float
    ) -> float:
        """
        Calculate overall balance score (0-100).
        Higher = more balanced.
        """
        if not win_rates:
            return 50.0

        # Calculate how close win rates are to expected
        deviations = [abs(wr - expected) / expected for wr in win_rates]
        avg_deviation = sum(deviations) / len(deviations)

        # Convert to 0-100 score (0 deviation = 100, 100% deviation = 0)
        score = max(0, 100 - avg_deviation * 100)

        # Penalize for high variance
        std = self._std(win_rates)
        std_penalty = std * 100  # Reduce score based on spread

        return max(0, score - std_penalty)

    def _classify_tiers(self, report: BalanceReport) -> None:
        """Classify all powers into tiers."""
        report.tier_counts = {tier: 0 for tier in PowerTier}
        report.tier_members = {tier: [] for tier in PowerTier}

        for name, analysis in report.analyses.items():
            tier = analysis.tier
            report.tier_counts[tier] = report.tier_counts.get(tier, 0) + 1
            report.tier_members[tier].append(name)

    def _identify_outliers(self, report: BalanceReport) -> None:
        """Identify significantly over/underpowered aliens."""
        expected = report.expected_win_rate

        for name, analysis in report.analyses.items():
            ci_low, ci_high = analysis.confidence_interval

            # Overpowered: entire CI above expected + 25%
            if ci_low > expected * 1.25:
                report.overpowered.append(name)

            # Underpowered: entire CI below expected - 25%
            elif ci_high < expected * 0.75:
                report.underpowered.append(name)

    def generate_report(self, report: BalanceReport) -> str:
        """Generate a text report of the analysis."""
        lines = [
            "=" * 70,
            "COSMIC ENCOUNTER POWER BALANCE ANALYSIS",
            "=" * 70,
            "",
            f"Games Analyzed: {report.total_games:,}",
            f"Powers Analyzed: {len(report.analyses)}",
            f"Expected Win Rate: {report.expected_win_rate*100:.1f}%",
            "",
            "BALANCE METRICS",
            "-" * 40,
            f"Balance Score: {report.balance_score:.1f}/100",
            f"Win Rate Std Dev: {report.win_rate_std*100:.2f}%",
            f"Gini Coefficient: {report.gini_coefficient:.3f}",
            "",
            "TIER DISTRIBUTION",
            "-" * 40,
        ]

        for tier in PowerTier:
            count = report.tier_counts.get(tier, 0)
            pct = count / max(1, len(report.analyses)) * 100
            lines.append(f"  Tier {tier.value}: {count:3} powers ({pct:5.1f}%)")

        lines.extend([
            "",
            "TOP 15 POWERS (by Win Rate)",
            "-" * 40,
        ])

        sorted_analyses = sorted(
            report.analyses.values(),
            key=lambda a: a.win_rate,
            reverse=True
        )

        for i, a in enumerate(sorted_analyses[:15], 1):
            lines.append(
                f"{i:2}. {a.name:15} | {a.tier.value} | "
                f"WR: {a.win_rate*100:5.1f}% | "
                f"Solo: {a.solo_win_rate*100:4.1f}% | "
                f"Games: {a.games_played:,}"
            )

        lines.extend([
            "",
            "BOTTOM 10 POWERS",
            "-" * 40,
        ])

        for a in sorted_analyses[-10:]:
            lines.append(
                f"    {a.name:15} | {a.tier.value} | "
                f"WR: {a.win_rate*100:5.1f}%"
            )

        if report.overpowered:
            lines.extend([
                "",
                "STATISTICALLY OVERPOWERED (95% CI > 125% expected)",
                "-" * 40,
            ])
            for name in report.overpowered:
                a = report.analyses[name]
                lines.append(
                    f"  {name}: {a.win_rate*100:.1f}% "
                    f"(CI: {a.confidence_interval[0]*100:.1f}%-{a.confidence_interval[1]*100:.1f}%)"
                )

        if report.underpowered:
            lines.extend([
                "",
                "STATISTICALLY UNDERPOWERED (95% CI < 75% expected)",
                "-" * 40,
            ])
            for name in report.underpowered:
                a = report.analyses[name]
                lines.append(
                    f"  {name}: {a.win_rate*100:.1f}% "
                    f"(CI: {a.confidence_interval[0]*100:.1f}%-{a.confidence_interval[1]*100:.1f}%)"
                )

        lines.extend(["", "=" * 70])

        return "\n".join(lines)


def run_analysis(stats_file: str = "cumulative_stats.json") -> str:
    """
    Run power balance analysis on cumulative stats.

    Args:
        stats_file: Path to cumulative stats JSON file

    Returns:
        Text report of the analysis
    """
    stats = CumulativeStats.load(stats_file)
    analyzer = PowerBalanceAnalyzer(min_games=100)
    report = analyzer.analyze(stats)
    return analyzer.generate_report(report)


if __name__ == "__main__":
    print(run_analysis())
