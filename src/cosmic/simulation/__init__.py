"""
Simulation runner and statistics for Cosmic Encounter.
"""

from .runner import Simulator, SimulationResult
from .stats import Statistics
from .cumulative_stats import CumulativeStats, AlienEloStats, EloCalculator
from .power_analysis import PowerBalanceAnalyzer, BalanceReport, PowerTier, run_analysis
from .matchup_analysis import (
    MatchupAnalyzer,
    MatchupMatrix,
    MatchupResult,
    run_quick_matchup,
    find_counters,
)
from .tournament import (
    Tournament,
    RoundRobinTournament,
    SwissTournament,
    MonteCarloEstimator,
    SynergyMatrix,
    TournamentResults,
    run_quick_tournament,
    run_monte_carlo_analysis,
)

__all__ = [
    "Simulator",
    "SimulationResult",
    "Statistics",
    "CumulativeStats",
    "AlienEloStats",
    "EloCalculator",
    "PowerBalanceAnalyzer",
    "BalanceReport",
    "PowerTier",
    "run_analysis",
    "MatchupAnalyzer",
    "MatchupMatrix",
    "MatchupResult",
    "run_quick_matchup",
    "find_counters",
    "Tournament",
    "RoundRobinTournament",
    "SwissTournament",
    "MonteCarloEstimator",
    "SynergyMatrix",
    "TournamentResults",
    "run_quick_tournament",
    "run_monte_carlo_analysis",
]
