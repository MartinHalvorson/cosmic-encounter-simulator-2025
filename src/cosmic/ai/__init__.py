"""
AI strategies for Cosmic Encounter.
"""

from .base import AIStrategy
from .basic_ai import BasicAI
from .strategic_ai import StrategicAI
from .random_ai import RandomAI
from .adaptive_ai import LearningAI
from .tactical_ai import TacticalAI
from .personality_ai import (
    AggressiveAI,
    CautiousAI,
    OpportunisticAI,
    SocialAI,
    AdaptiveAI,
    VengefulAI,
    KingmakerAI,
    BlufferAI,
    MinimalistAI,
    ChaosAI,
)
from .alliance_utils import (
    AllianceHistory,
    estimate_win_probability,
    evaluate_ally_power_synergy,
    calculate_offense_ally_value,
    calculate_defense_ally_value,
    select_optimal_ally_ships,
    should_block_leader,
    get_alliance_recommendation,
    COMBAT_BONUS_POWERS,
    DANGEROUS_ALLY_POWERS,
    ALLIANCE_SYNERGY_POWERS,
)

__all__ = [
    "AIStrategy",
    "BasicAI",
    "StrategicAI",
    "RandomAI",
    "LearningAI",
    "TacticalAI",
    "AggressiveAI",
    "CautiousAI",
    "OpportunisticAI",
    "SocialAI",
    "AdaptiveAI",
    "VengefulAI",
    "KingmakerAI",
    "BlufferAI",
    "MinimalistAI",
    "ChaosAI",
    "AllianceHistory",
    "estimate_win_probability",
    "evaluate_ally_power_synergy",
    "calculate_offense_ally_value",
    "calculate_defense_ally_value",
    "select_optimal_ally_ships",
    "should_block_leader",
    "get_alliance_recommendation",
    "COMBAT_BONUS_POWERS",
    "DANGEROUS_ALLY_POWERS",
    "ALLIANCE_SYNERGY_POWERS",
]
