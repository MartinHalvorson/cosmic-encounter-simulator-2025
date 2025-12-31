"""
Color Powers - Color-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Red(AlienPower):
    """Red - Aggressive color. +4 when attacking."""
    name: str = field(default="Red", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Blue(AlienPower):
    """Blue - Calm color. +4 when defending."""
    name: str = field(default="Blue", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class GreenColor(AlienPower):
    """Green Color - Growth color. +1 per home colony."""
    name: str = field(default="GreenColor", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + home_count
        return total


@dataclass
class Yellow(AlienPower):
    """Yellow - Bright color. See opponent's card."""
    name: str = field(default="Yellow", init=False)
    description: str = field(default="View opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Orange(AlienPower):
    """Orange - Warm color. +3 on first encounter."""
    name: str = field(default="Orange", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Purple(AlienPower):
    """Purple - Royal color. Win ties."""
    name: str = field(default="Purple", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class White(AlienPower):
    """White - Pure color. +2 always."""
    name: str = field(default="White", init=False)
    description: str = field(default="+2 to all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class BlackColor(AlienPower):
    """Black Color - Dark color. -2 to opponent's total."""
    name: str = field(default="BlackColor", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gray(AlienPower):
    """Gray - Neutral color. Ships escape to colonies."""
    name: str = field(default="Gray", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pink(AlienPower):
    """Pink - Soft color. Force one ally to join."""
    name: str = field(default="Pink", init=False)
    description: str = field(default="Compel one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Brown(AlienPower):
    """Brown - Earth color. +2 defending home."""
    name: str = field(default="Brown", init=False)
    description: str = field(default="+2 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 2
        return total


@dataclass
class Cyan(AlienPower):
    """Cyan - Cool color. Retrieve 2 ships from warp."""
    name: str = field(default="Cyan", init=False)
    description: str = field(default="Retrieve 2 ships each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magenta(AlienPower):
    """Magenta - Vibrant color. Swap encounter cards."""
    name: str = field(default="Magenta", init=False)
    description: str = field(default="Swap cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Indigo(AlienPower):
    """Indigo - Deep color. Draw card when winning."""
    name: str = field(default="Indigo", init=False)
    description: str = field(default="Draw card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Violet(AlienPower):
    """Violet - Soft purple. +1 per ally."""
    name: str = field(default="Violet", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Red())
AlienRegistry.register(Blue())
AlienRegistry.register(GreenColor())
AlienRegistry.register(Yellow())
AlienRegistry.register(Orange())
AlienRegistry.register(Purple())
AlienRegistry.register(White())
AlienRegistry.register(BlackColor())
AlienRegistry.register(Gray())
AlienRegistry.register(Pink())
AlienRegistry.register(Brown())
AlienRegistry.register(Cyan())
AlienRegistry.register(Magenta())
AlienRegistry.register(Indigo())
AlienRegistry.register(Violet())
