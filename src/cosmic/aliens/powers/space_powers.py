"""
Space Powers - Aliens with cosmic and space-themed abilities.
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
class Asteroid(AlienPower):
    """
    Asteroid - Space Rock.
    When defending, opponent's attack card is reduced by 5.
    """
    name: str = field(default="Asteroid", init=False)
    description: str = field(default="Reduce attacking card by 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class BlackHole(AlienPower):
    """
    BlackHole - Gravity Well.
    Ships lost in encounters with you are removed from the game.
    """
    name: str = field(default="BlackHole", init=False)
    description: str = field(default="Lost ships removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Comet(AlienPower):
    """
    Comet - Fast Traveler.
    You may have a second encounter after winning or losing.
    """
    name: str = field(default="Comet", init=False)
    description: str = field(default="Second encounter after any result.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Constellation(AlienPower):
    """
    Constellation - Star Pattern.
    Your home planets are worth 2 colonies each for winning.
    """
    name: str = field(default="Constellation", init=False)
    description: str = field(default="Home planets count as 2 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cosmos(AlienPower):
    """
    Cosmos - Universal Force.
    Once per game, you may cancel any encounter and restart.
    """
    name: str = field(default="Cosmos", init=False)
    description: str = field(default="Cancel and restart encounter once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Eclipse(AlienPower):
    """
    Eclipse - Shadow Pass.
    During your turn, other players cannot use their powers.
    """
    name: str = field(default="Eclipse", init=False)
    description: str = field(default="Block powers during your turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Galaxy(AlienPower):
    """
    Galaxy - Vast Space.
    You may establish colonies on any planet in any system.
    """
    name: str = field(default="Galaxy", init=False)
    description: str = field(default="Colonize any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nebula(AlienPower):
    """
    Nebula - Gas Cloud.
    Attacks against you have -3 to their total.
    """
    name: str = field(default="Nebula", init=False)
    description: str = field(default="Attackers get -3 total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nova(AlienPower):
    """
    Nova - Exploding Star.
    When you lose, all ships on the planet go to warp.
    """
    name: str = field(default="Nova", init=False)
    description: str = field(default="All ships warp when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Orbit(AlienPower):
    """
    Orbit - Circular Path.
    Ships you lose go to your colonies instead of warp.
    """
    name: str = field(default="Orbit", init=False)
    description: str = field(default="Lost ships return to colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pulsar(AlienPower):
    """
    Pulsar - Energy Pulse.
    Once per encounter, force opponent to discard their encounter card.
    """
    name: str = field(default="Pulsar", init=False)
    description: str = field(default="Force opponent card discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quasar(AlienPower):
    """
    Quasar - Bright Object.
    Your encounter cards are revealed face up before selection.
    """
    name: str = field(default="Quasar", init=False)
    description: str = field(default="Cards revealed during selection.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Satellite(AlienPower):
    """
    Satellite - Orbiter.
    You may ally in any encounter without being invited.
    """
    name: str = field(default="Satellite", init=False)
    description: str = field(default="Ally without invitation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Singularity(AlienPower):
    """
    Singularity - Unique Point.
    You can only have one ship per planet, but each counts as 4.
    """
    name: str = field(default="Singularity", init=False)
    description: str = field(default="1 ship per planet, counts as 4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Solar(AlienPower):
    """
    Solar - Sun Power.
    At the start of your turn, retrieve 2 ships from warp.
    """
    name: str = field(default="Solar", init=False)
    description: str = field(default="Retrieve 2 ships at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Star(AlienPower):
    """
    Star - Shining Light.
    Your attack cards get +3 value.
    """
    name: str = field(default="Star", init=False)
    description: str = field(default="Attack cards +3 value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 to total."""
        return total + 3


@dataclass
class Supernova(AlienPower):
    """
    Supernova - Massive Explosion.
    When winning by 20+, opponent loses all ships on that planet.
    """
    name: str = field(default="Supernova", init=False)
    description: str = field(default="Big wins destroy all opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Wormhole(AlienPower):
    """
    Wormhole - Space Tunnel.
    You may attack any planet, ignoring destiny.
    """
    name: str = field(default="Wormhole", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Asteroid())
AlienRegistry.register(BlackHole())
AlienRegistry.register(Comet())
AlienRegistry.register(Constellation())
AlienRegistry.register(Cosmos())
AlienRegistry.register(Eclipse())
AlienRegistry.register(Galaxy())
AlienRegistry.register(Nebula())
AlienRegistry.register(Nova())
AlienRegistry.register(Orbit())
AlienRegistry.register(Pulsar())
AlienRegistry.register(Quasar())
AlienRegistry.register(Satellite())
AlienRegistry.register(Singularity())
AlienRegistry.register(Solar())
AlienRegistry.register(Star())
AlienRegistry.register(Supernova())
AlienRegistry.register(Wormhole())
