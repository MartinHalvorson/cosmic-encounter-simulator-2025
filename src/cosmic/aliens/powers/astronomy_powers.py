"""
Astronomy and Celestial themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Star(AlienPower):
    """Star - Power of Brilliance."""
    name: str = field(default="Star", init=False)
    description: str = field(
        default="+1 for each planet you have ships on.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Comet(AlienPower):
    """Comet - Power of Speed."""
    name: str = field(default="Comet", init=False)
    description: str = field(
        default="Take a second encounter if you win the first.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nebula(AlienPower):
    """Nebula - Power of Concealment."""
    name: str = field(default="Nebula", init=False)
    description: str = field(
        default="Your ships can't be targeted by artifact powers.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pulsar(AlienPower):
    """Pulsar - Power of Rhythm."""
    name: str = field(default="Pulsar", init=False)
    description: str = field(
        default="+4 on even-numbered turns, -2 on odd turns.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Asteroid(AlienPower):
    """Asteroid - Power of Fragments."""
    name: str = field(default="Asteroid", init=False)
    description: str = field(
        default="When losing, send 1 opponent ship to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Constellation(AlienPower):
    """Constellation - Power of Patterns."""
    name: str = field(default="Constellation", init=False)
    description: str = field(
        default="+3 when your ships form a specific pattern.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eclipse(AlienPower):
    """Eclipse - Power of Darkness."""
    name: str = field(default="Eclipse", init=False)
    description: str = field(
        default="All encounter cards are hidden until reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Supernova(AlienPower):
    """Supernova - Power of Explosion."""
    name: str = field(default="Supernova", init=False)
    description: str = field(
        default="When you lose, all ships in encounter go to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Galaxy(AlienPower):
    """Galaxy - Power of Vastness."""
    name: str = field(default="Galaxy", init=False)
    description: str = field(
        default="+1 for each foreign colony you have.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Moonlet(AlienPower):
    """Moonlet - Power of Orbit."""
    name: str = field(default="Moonlet", init=False)
    description: str = field(
        default="Your ships return from warp at the start of each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quasar(AlienPower):
    """Quasar - Power of Energy."""
    name: str = field(default="Quasar", init=False)
    description: str = field(
        default="Draw 2 cards whenever you use a power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Meteor(AlienPower):
    """Meteor - Power of Impact."""
    name: str = field(default="Meteor", init=False)
    description: str = field(
        default="+5 when attacking, -2 when defending.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Star())
AlienRegistry.register(Comet())
AlienRegistry.register(Nebula())
AlienRegistry.register(Pulsar())
AlienRegistry.register(Asteroid())
AlienRegistry.register(Constellation())
AlienRegistry.register(Eclipse())
AlienRegistry.register(Supernova())
AlienRegistry.register(Galaxy())
AlienRegistry.register(Moonlet())
AlienRegistry.register(Quasar())
AlienRegistry.register(Meteor())
