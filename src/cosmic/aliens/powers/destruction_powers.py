"""
Destruction Powers - Aliens with devastating offensive abilities.
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
class Annihilator(AlienPower):
    """
    Annihilator - Total Destruction.
    Remove opponent ships from game.
    """
    name: str = field(default="Annihilator", init=False)
    description: str = field(default="Remove ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Blaster(AlienPower):
    """
    Blaster - Energy Attack.
    +8 when attacking.
    """
    name: str = field(default="Blaster", init=False)
    description: str = field(default="+8 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +8 when attacking."""
        if side == Side.OFFENSE:
            return total + 8
        return total


@dataclass
class Bomber(AlienPower):
    """
    Bomber - Area Damage.
    Hit multiple targets.
    """
    name: str = field(default="Bomber", init=False)
    description: str = field(default="Hit multiple.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Breaker(AlienPower):
    """
    Breaker - Shatter Defense.
    Ignore defensive bonuses.
    """
    name: str = field(default="Breaker", init=False)
    description: str = field(default="Ignore defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crusher(AlienPower):
    """
    Crusher - Overwhelming Force.
    +3 per ship committed.
    """
    name: str = field(default="Crusher", init=False)
    description: str = field(default="+3 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Decimator(AlienPower):
    """
    Decimator - Mass Casualties.
    Kill 10% of opponent ships.
    """
    name: str = field(default="Decimator", init=False)
    description: str = field(default="10% casualties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Demolisher(AlienPower):
    """
    Demolisher - Break Down.
    Destroy opponent cards.
    """
    name: str = field(default="Demolisher", init=False)
    description: str = field(default="Destroy cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Desolator(AlienPower):
    """
    Desolator - Leave Nothing.
    Clear planet of all ships.
    """
    name: str = field(default="Desolator", init=False)
    description: str = field(default="Clear planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Destroyer(AlienPower):
    """
    Destroyer - Pure Destruction.
    Win by 15+ removes all ships.
    """
    name: str = field(default="Destroyer", init=False)
    description: str = field(default="Big win kills all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Eradicator(AlienPower):
    """
    Eradicator - Complete Removal.
    Remove colony on win.
    """
    name: str = field(default="Eradicator", init=False)
    description: str = field(default="Remove colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Executioner(AlienPower):
    """
    Executioner - Kill Strike.
    Eliminate weakest ships.
    """
    name: str = field(default="Executioner", init=False)
    description: str = field(default="Kill weak ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Obliterator(AlienPower):
    """
    Obliterator - Wipe Out.
    Destroy all on critical win.
    """
    name: str = field(default="Obliterator", init=False)
    description: str = field(default="Wipe on crit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Piercer(AlienPower):
    """
    Piercer - Penetrating Attack.
    Ignore first 5 defense.
    """
    name: str = field(default="Piercer", init=False)
    description: str = field(default="Pierce 5 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ravager_Alt(AlienPower):
    """
    Ravager_Alt - Devastating Strike.
    Extra damage on win.
    """
    name: str = field(default="Ravager_Alt", init=False)
    description: str = field(default="Extra damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shatterer(AlienPower):
    """
    Shatterer - Break Apart.
    Split opponent forces.
    """
    name: str = field(default="Shatterer", init=False)
    description: str = field(default="Split forces.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Slayer(AlienPower):
    """
    Slayer - Kill Shot.
    Remove 1 ship before combat.
    """
    name: str = field(default="Slayer", init=False)
    description: str = field(default="Kill 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Smasher(AlienPower):
    """
    Smasher - Heavy Hit.
    +6 to total.
    """
    name: str = field(default="Smasher", init=False)
    description: str = field(default="+6 total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +6 to total."""
        return total + 6


@dataclass
class Wrecker(AlienPower):
    """
    Wrecker - Cause Havoc.
    Destroy random cards.
    """
    name: str = field(default="Wrecker", init=False)
    description: str = field(default="Random destruction.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Annihilator())
AlienRegistry.register(Blaster())
AlienRegistry.register(Bomber())
AlienRegistry.register(Breaker())
AlienRegistry.register(Crusher())
AlienRegistry.register(Decimator())
AlienRegistry.register(Demolisher())
AlienRegistry.register(Desolator())
AlienRegistry.register(Destroyer())
AlienRegistry.register(Eradicator())
AlienRegistry.register(Executioner())
AlienRegistry.register(Obliterator())
AlienRegistry.register(Piercer())
AlienRegistry.register(Ravager_Alt())
AlienRegistry.register(Shatterer())
AlienRegistry.register(Slayer())
AlienRegistry.register(Smasher())
AlienRegistry.register(Wrecker())
