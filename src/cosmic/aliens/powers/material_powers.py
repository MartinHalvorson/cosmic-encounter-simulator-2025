"""
Material Powers - Substance and material-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Steel(AlienPower):
    """Steel - Power of Strength. +4 always."""
    name: str = field(default="Steel", init=False)
    description: str = field(default="+4 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Glass(AlienPower):
    """Glass - Power of Transparency. See all cards."""
    name: str = field(default="Glass", init=False)
    description: str = field(default="See all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stone(AlienPower):
    """Stone - Power of Endurance. +3 on defense."""
    name: str = field(default="Stone", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Wood(AlienPower):
    """Wood - Power of Growth. Extra ship each turn."""
    name: str = field(default="Wood", init=False)
    description: str = field(default="Add 1 ship to colony each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gold(AlienPower):
    """Gold - Power of Value. Extra cards."""
    name: str = field(default="Gold", init=False)
    description: str = field(default="Draw 2 extra cards each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Silver(AlienPower):
    """Silver - Power of Second. +2 on second encounter."""
    name: str = field(default="Silver", init=False)
    description: str = field(default="+2 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bronze(AlienPower):
    """Bronze - Power of Third. +3 always."""
    name: str = field(default="Bronze", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Iron(AlienPower):
    """Iron - Power of Durability. Lose fewer ships."""
    name: str = field(default="Iron", init=False)
    description: str = field(default="Lose 1 fewer ship in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Copper(AlienPower):
    """Copper - Power of Conductivity. Transfer bonuses."""
    name: str = field(default="Copper", init=False)
    description: str = field(default="Give +2 to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Titanium(AlienPower):
    """Titanium - Power of Lightness. +5 with few ships."""
    name: str = field(default="Titanium", init=False)
    description: str = field(default="+5 when committing 1-2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diamond(AlienPower):
    """Diamond - Power of Hardness. +6 on defense."""
    name: str = field(default="Diamond", init=False)
    description: str = field(default="+6 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class Ruby(AlienPower):
    """Ruby - Power of Fire. +3 on offense."""
    name: str = field(default="Ruby", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Emerald(AlienPower):
    """Emerald - Power of Nature. +2 per home colony."""
    name: str = field(default="Emerald", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sapphire(AlienPower):
    """Sapphire - Power of Wisdom. See opponent card."""
    name: str = field(default="Sapphire", init=False)
    description: str = field(default="View opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clay(AlienPower):
    """Clay - Power of Shaping. Change card type."""
    name: str = field(default="Clay", init=False)
    description: str = field(default="Treat attack as negotiate or vice versa.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Brick(AlienPower):
    """Brick - Power of Building. Extra colonies."""
    name: str = field(default="Brick", init=False)
    description: str = field(default="Win grants extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sand(AlienPower):
    """Sand - Power of Numbers. +1 per ship."""
    name: str = field(default="Sand", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Plastic(AlienPower):
    """Plastic - Power of Flexibility. Change ally allegiance."""
    name: str = field(default="Plastic", init=False)
    description: str = field(default="Switch 1 ally to your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Paper(AlienPower):
    """Paper - Power of Record. Draw on win."""
    name: str = field(default="Paper", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Leather(AlienPower):
    """Leather - Power of Protection. Reduce damage."""
    name: str = field(default="Leather", init=False)
    description: str = field(default="Lose 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
MATERIAL_POWERS = [
    Steel, Glass, Stone, Wood, Gold, Silver, Bronze, Iron, Copper, Titanium,
    Diamond, Ruby, Emerald, Sapphire, Clay, Brick, Sand, Plastic, Paper, Leather,
]

for power_class in MATERIAL_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
