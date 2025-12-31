"""
Analysis tools for Cosmic Encounter simulator.

Provides tools for:
- Balance analysis (power tiers, outliers)
- Synergy analysis (ally combinations, counters)
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

from .synergy import (
    SynergyAnalyzer,
    SynergyReport,
    SynergyData,
    CounterData,
    suggest_synergies,
    POWER_CATEGORIES,
)

__all__ = [
    # Balance
    "BalanceAnalyzer",
    "BalanceReport",
    "PowerBalanceData",
    "compare_power_matchups",
    "identify_power_synergies",
    "calculate_player_count_balance",
    # Synergy
    "SynergyAnalyzer",
    "SynergyReport",
    "SynergyData",
    "CounterData",
    "suggest_synergies",
    "POWER_CATEGORIES",
]
