"""
Analysis tools for Cosmic Encounter simulator.

Provides tools for:
- Balance analysis (power tiers, outliers)
- Meta game analysis
- Statistical comparisons
"""

from .balance import (
    BalanceAnalyzer,
    BalanceReport,
    PowerBalanceData,
    compare_power_matchups,
    identify_power_synergies,
    calculate_player_count_balance,
)

__all__ = [
    "BalanceAnalyzer",
    "BalanceReport",
    "PowerBalanceData",
    "compare_power_matchups",
    "identify_power_synergies",
    "calculate_player_count_balance",
]
