"""
Combat Extended Powers - More combat-themed aliens.
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
class Warrior_Alt(AlienPower):
    """Warrior_Alt - Power of Combat. +4 on offense."""
    name: str = field(default="Warrior_Alt", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Defender_Alt(AlienPower):
    """Defender_Alt - Power of Protection. +5 on defense."""
    name: str = field(default="Defender_Alt", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Crusader(AlienPower):
    """Crusader - Power of Holy War. +3 always."""
    name: str = field(default="Crusader", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Duelist(AlienPower):
    """Duelist - Power of Single Combat. +6 alone."""
    name: str = field(default="Duelist", init=False)
    description: str = field(default="+6 when no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gladiator(AlienPower):
    """Gladiator - Power of Arena. Win ties."""
    name: str = field(default="Gladiator", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Samurai(AlienPower):
    """Samurai - Power of Honor. +4 with high cards."""
    name: str = field(default="Samurai", init=False)
    description: str = field(default="+4 when card is 15+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Viking(AlienPower):
    """Viking - Power of Raid. Take cards on win."""
    name: str = field(default="Viking", init=False)
    description: str = field(default="Take 1 card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spartan(AlienPower):
    """Spartan - Power of Discipline. +2 per ship."""
    name: str = field(default="Spartan", init=False)
    description: str = field(default="+2 per ship committed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Berserker_Alt(AlienPower):
    """Berserker_Alt - Power of Rage. +5 when losing."""
    name: str = field(default="Berserker_Alt", init=False)
    description: str = field(default="+5 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mercenary(AlienPower):
    """Mercenary - Power of Hire. +3 as ally."""
    name: str = field(default="Mercenary", init=False)
    description: str = field(default="+3 when allied.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warlord_Alt(AlienPower):
    """Warlord_Alt - Power of Conquest. +2 per colony."""
    name: str = field(default="Warlord_Alt", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class General(AlienPower):
    """General - Power of Strategy. +1 per ally ship."""
    name: str = field(default="General", init=False)
    description: str = field(default="+1 per allied ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Legionnaire(AlienPower):
    """Legionnaire - Power of Legion. +1 per home colony."""
    name: str = field(default="Legionnaire", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Centurion(AlienPower):
    """Centurion - Power of Rank. +4 constant."""
    name: str = field(default="Centurion", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Tactician(AlienPower):
    """Tactician - Power of Maneuver. See opponent card."""
    name: str = field(default="Tactician", init=False)
    description: str = field(default="View opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Commander(AlienPower):
    """Commander - Power of Leadership. +2 per ally."""
    name: str = field(default="Commander", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Marshal(AlienPower):
    """Marshal - Power of Order. Allies +1 each."""
    name: str = field(default="Marshal", init=False)
    description: str = field(default="Allies gain +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sergeant(AlienPower):
    """Sergeant - Power of Training. +3 with max ships."""
    name: str = field(default="Sergeant", init=False)
    description: str = field(default="+3 when committing 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Corporal(AlienPower):
    """Corporal - Power of Support. +2 constant."""
    name: str = field(default="Corporal", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


# Register all powers
COMBAT_EXTENDED_POWERS = [
    Warrior_Alt, Defender_Alt, Crusader, Duelist, Gladiator, Samurai, Viking, Spartan,
    Berserker_Alt, Mercenary, Warlord_Alt, General, Legionnaire, Centurion, Tactician,
    Commander, Marshal, Sergeant, Corporal,
]

for power_class in COMBAT_EXTENDED_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
