"""
Milestone 5K Batch 5 Powers - Final batch for 5000+ milestone.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

# Generate powers programmatically for batch 5
power_specs_batch5 = [
    ("Peacemaker_5K", "+3 always", 3, None),
    ("Arbiter_5K", "+3 always", 3, None),
    ("Judge_5K", "+4 always", 4, None),
    ("Juror_5K", "+3 always", 3, None),
    ("Witness_5K", "+2 always", 2, None),
    ("Attorney_5K", "+4 always", 4, None),
    ("Prosecutor_5K", "+4 offense", 4, Side.OFFENSE),
    ("Defender_Alt_5K", "+4 defense", 4, Side.DEFENSE),
    ("Bailiff_5K", "+3 defense", 3, Side.DEFENSE),
    ("Clerk_5K", "+2 always", 2, None),
    ("Magistrate_5K", "+4 always", 4, None),
    ("Chancellor_5K", "+5 always", 5, None),
    ("Senator_5K", "+4 always", 4, None),
    ("Governor_5K", "+4 always", 4, None),
    ("Mayor_5K", "+3 always", 3, None),
    ("Councilor_5K", "+3 always", 3, None),
    ("Elder_5K", "+4 always", 4, None),
    ("Sage_5K", "+4 always", 4, None),
    ("Advisor_5K", "+3 always", 3, None),
    ("Mentor_5K", "+4 always", 4, None),
    ("Teacher_5K", "+3 always", 3, None),
    ("Student_5K", "+2 always", 2, None),
    ("Scholar_5K", "+4 always", 4, None),
    ("Professor_5K", "+4 always", 4, None),
    ("Dean_5K", "+4 always", 4, None),
    ("Principal_5K", "+4 always", 4, None),
    ("Headmaster_5K", "+5 always", 5, None),
    ("Director_5K", "+4 always", 4, None),
    ("Manager_5K", "+3 always", 3, None),
    ("Supervisor_5K", "+3 always", 3, None),
]

MILESTONE_5K_BATCH5_POWERS = []

for name, desc, bonus, side in power_specs_batch5:
    @dataclass
    class Power(AlienPower):
        name: str = field(default=name, init=False)
        description: str = field(default=desc, init=False)
        timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
        power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
        category: PowerCategory = field(default=PowerCategory.GREEN if bonus <= 4 else PowerCategory.YELLOW, init=False)
        _bonus: int = field(default=bonus, init=False)
        _side: Side = field(default=side, init=False)

        def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
            if not player.power_active:
                return total
            if self._side is None or side == self._side:
                return total + self._bonus
            return total

    Power.__name__ = name
    Power.__qualname__ = name
    MILESTONE_5K_BATCH5_POWERS.append(Power)

for power_class in MILESTONE_5K_BATCH5_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
