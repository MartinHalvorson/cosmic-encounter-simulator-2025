"""
Geography Powers - Location and terrain themed aliens.
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
class Mountain(AlienPower):
    """Mountain - Power of Height. +4 on defense."""
    name: str = field(default="Mountain", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Ocean(AlienPower):
    """Ocean - Power of Depth. Retrieve ships from warp."""
    name: str = field(default="Ocean", init=False)
    description: str = field(default="Return 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Valley(AlienPower):
    """Valley - Power of Shelter. Ships protected."""
    name: str = field(default="Valley", init=False)
    description: str = field(default="Ships on home planets immune to hazards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class River(AlienPower):
    """River - Power of Flow. Move ships freely."""
    name: str = field(default="River", init=False)
    description: str = field(default="Move ships between your colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Island(AlienPower):
    """Island - Power of Isolation. Blocks alliances."""
    name: str = field(default="Island", init=False)
    description: str = field(default="Opponent cannot invite allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cave(AlienPower):
    """Cave - Power of Hiding. Ships return instead of warp."""
    name: str = field(default="Cave", init=False)
    description: str = field(default="Lost ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cliff(AlienPower):
    """Cliff - Power of the Edge. High risk high reward."""
    name: str = field(default="Cliff", init=False)
    description: str = field(default="+8 or -4 (random).", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (8 if random.random() > 0.5 else -4)
        return total


@dataclass
class Plain(AlienPower):
    """Plain - Power of Openness. All cards visible."""
    name: str = field(default="Plain", init=False)
    description: str = field(default="See all players' hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jungle(AlienPower):
    """Jungle - Power of Growth. Extra cards."""
    name: str = field(default="Jungle", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swamp(AlienPower):
    """Swamp - Power of Trapping. Slow enemies."""
    name: str = field(default="Swamp", init=False)
    description: str = field(default="Attacking ships commit -1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glacier(AlienPower):
    """Glacier - Power of Cold. Freeze opponent's actions."""
    name: str = field(default="Glacier", init=False)
    description: str = field(default="Opponent skips alliance phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oasis(AlienPower):
    """Oasis - Power of Refuge. Safe haven."""
    name: str = field(default="Oasis", init=False)
    description: str = field(default="Return 1 ship from warp to home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Volcano_Alt(AlienPower):
    """Volcano_Alt - Power of Eruption. Destroy ships."""
    name: str = field(default="Volcano_Alt", init=False)
    description: str = field(default="Send 2 opponent ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Canyon(AlienPower):
    """Canyon - Power of Division. Split encounters."""
    name: str = field(default="Canyon", init=False)
    description: str = field(default="Allies count separately.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Plateau(AlienPower):
    """Plateau - Power of Stability. +3 always."""
    name: str = field(default="Plateau", init=False)
    description: str = field(default="+3 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Peninsula(AlienPower):
    """Peninsula - Power of Position. Strategic advantage."""
    name: str = field(default="Peninsula", init=False)
    description: str = field(default="+2 when only defender.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reef(AlienPower):
    """Reef - Power of Hidden Danger. Trap attackers."""
    name: str = field(default="Reef", init=False)
    description: str = field(default="Attacker loses 1 ship before combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hill(AlienPower):
    """Hill - Power of Advantage. +2 on defense."""
    name: str = field(default="Hill", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Lake(AlienPower):
    """Lake - Power of Calm. Cards revealed simultaneously."""
    name: str = field(default="Lake", init=False)
    description: str = field(default="Both cards reveal at same time.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coast(AlienPower):
    """Coast - Power of Trade. Draw when negotiating."""
    name: str = field(default="Coast", init=False)
    description: str = field(default="Draw 2 cards when dealing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
GEOGRAPHY_POWERS = [
    Mountain, Ocean, Valley, River, Island, Cave, Cliff, Plain, Jungle, Swamp,
    Glacier, Oasis, Volcano_Alt, Canyon, Plateau, Peninsula, Reef, Hill, Lake, Coast,
]

for power_class in GEOGRAPHY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
