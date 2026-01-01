"""
Desert Creature Powers for Cosmic Encounter.

Aliens inspired by desert animals and environments.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Scorpion_Alt(AlienPower):
    """Scorpion_Alt - Power of Stinging. Attacker loses 1 ship after."""
    name: str = field(default="Scorpion_Alt", init=False)
    description: str = field(default="Attacker loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Camel(AlienPower):
    """Camel - Power of Endurance. Lose max 2 ships per encounter."""
    name: str = field(default="Camel", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rattlesnake(AlienPower):
    """Rattlesnake - Power of Warning. +3 on defense."""
    name: str = field(default="Rattlesnake", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Vulture_Alt(AlienPower):
    """Vulture_Alt - Power of Scavenging. Draw 1 card from discard on win."""
    name: str = field(default="Vulture_Alt", init=False)
    description: str = field(default="Take discarded card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Coyote(AlienPower):
    """Coyote - Power of Cunning. See opponent's card before choosing."""
    name: str = field(default="Coyote", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Roadrunner(AlienPower):
    """Roadrunner - Power of Speed. +4 on first encounter."""
    name: str = field(default="Roadrunner", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Gila_Monster(AlienPower):
    """Gila_Monster - Power of Venom. Winner loses 1 ship after."""
    name: str = field(default="Gila_Monster", init=False)
    description: str = field(default="Winner loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fennec(AlienPower):
    """Fennec - Power of Hearing. Know opponent's hand size."""
    name: str = field(default="Fennec", init=False)
    description: str = field(default="Know opponent hand size.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sidewinder(AlienPower):
    """Sidewinder - Power of Evasion. Win ties automatically."""
    name: str = field(default="Sidewinder", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sandstorm(AlienPower):
    """Sandstorm - Power of Blinding. -2 to opponent's total."""
    name: str = field(default="Sandstorm", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oasis(AlienPower):
    """Oasis - Power of Refuge. Ships return from warp each turn."""
    name: str = field(default="Oasis", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tumbleweed_Alt(AlienPower):
    """Tumbleweed_Alt - Power of Wandering. Attack any planet."""
    name: str = field(default="Tumbleweed_Alt", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dust_Devil(AlienPower):
    """Dust_Devil - Power of Spinning. Scatter opponent ships."""
    name: str = field(default="Dust_Devil", init=False)
    description: str = field(default="Scatter opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mirage(AlienPower):
    """Mirage - Power of Illusion. Copy opponent's card value."""
    name: str = field(default="Mirage", init=False)
    description: str = field(default="Copy opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Armadillo(AlienPower):
    """Armadillo - Power of Armor. +2 on defense."""
    name: str = field(default="Armadillo", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


# Register all desert creature powers
AlienRegistry.register(Scorpion_Alt())
AlienRegistry.register(Camel())
AlienRegistry.register(Rattlesnake())
AlienRegistry.register(Vulture_Alt())
AlienRegistry.register(Coyote())
AlienRegistry.register(Roadrunner())
AlienRegistry.register(Gila_Monster())
AlienRegistry.register(Fennec())
AlienRegistry.register(Sidewinder())
AlienRegistry.register(Sandstorm())
AlienRegistry.register(Oasis())
AlienRegistry.register(Tumbleweed_Alt())
AlienRegistry.register(Dust_Devil())
AlienRegistry.register(Mirage())
AlienRegistry.register(Armadillo())
