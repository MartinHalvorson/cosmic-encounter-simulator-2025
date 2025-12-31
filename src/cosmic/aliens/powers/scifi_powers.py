"""
Sci-Fi Powers for Cosmic Encounter.

Aliens inspired by science fiction tropes and concepts.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Clone_Alt(AlienPower):
    """
    Clone_Alt - Power to Duplicate.
    Your ships count double in encounters.
    """
    name: str = field(default="Clone_Alt", init=False)
    description: str = field(
        default="Ships count double.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Teleporter(AlienPower):
    """
    Teleporter - Power to Beam.
    Move ships between any of your colonies before launch.
    """
    name: str = field(default="Teleporter", init=False)
    description: str = field(
        default="Move ships between colonies freely.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hologram(AlienPower):
    """
    Hologram - Power to Deceive.
    Your card appears as a different value until reveal.
    """
    name: str = field(default="Hologram", init=False)
    description: str = field(
        default="Disguise your card value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Laser(AlienPower):
    """
    Laser - Power to Pierce.
    +3 on offense.
    """
    name: str = field(default="Laser", init=False)
    description: str = field(
        default="+3 on offense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Forcefield(AlienPower):
    """
    Forcefield - Power to Block.
    +3 on defense.
    """
    name: str = field(default="Forcefield", init=False)
    description: str = field(
        default="+3 on defense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cyborg_Alt(AlienPower):
    """
    Cyborg_Alt - Power of Enhancement.
    +1 for each card in your hand.
    """
    name: str = field(default="Cyborg_Alt", init=False)
    description: str = field(
        default="+1 per card in hand (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Android_Alt(AlienPower):
    """
    Android_Alt - Power of Logic.
    Win ties automatically.
    """
    name: str = field(default="Android_Alt", init=False)
    description: str = field(
        default="Win all ties.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mothership(AlienPower):
    """
    Mothership - Power to Launch.
    Commit up to 6 ships on offense.
    """
    name: str = field(default="Mothership", init=False)
    description: str = field(
        default="Launch up to 6 ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spacedock(AlienPower):
    """
    Spacedock - Power to Repair.
    Return 2 ships from warp at start of turn.
    """
    name: str = field(default="Spacedock", init=False)
    description: str = field(
        default="Return 2 ships from warp each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stasis(AlienPower):
    """
    Stasis - Power to Freeze.
    One opponent cannot commit allies this encounter.
    """
    name: str = field(default="Stasis", init=False)
    description: str = field(
        default="Block one player's allies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hyperdrive(AlienPower):
    """
    Hyperdrive - Power to Speed.
    Get an extra encounter if you win on offense.
    """
    name: str = field(default="Hyperdrive", init=False)
    description: str = field(
        default="Extra encounter on offense win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Quantum_Alt(AlienPower):
    """
    Quantum_Alt - Power of Uncertainty.
    Flip a coin; heads = +5, tails = -5.
    """
    name: str = field(default="Quantum_Alt", init=False)
    description: str = field(
        default="50% chance +5 or -5.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Alien_Tech(AlienPower):
    """
    Alien_Tech - Power of Innovation.
    Draw 1 extra card at start of each turn.
    """
    name: str = field(default="Alien_Tech", init=False)
    description: str = field(
        default="Draw 1 extra card each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Terraformer(AlienPower):
    """
    Terraformer - Power to Change.
    Treat foreign planets as home planets.
    """
    name: str = field(default="Terraformer", init=False)
    description: str = field(
        default="Foreign planets count as home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Xenomorph(AlienPower):
    """
    Xenomorph - Power to Evolve.
    +1 for each encounter you've won this game.
    """
    name: str = field(default="Xenomorph", init=False)
    description: str = field(
        default="+1 per win (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all sci-fi powers
AlienRegistry.register(Clone_Alt())
AlienRegistry.register(Teleporter())
AlienRegistry.register(Hologram())
AlienRegistry.register(Laser())
AlienRegistry.register(Forcefield())
AlienRegistry.register(Cyborg_Alt())
AlienRegistry.register(Android_Alt())
AlienRegistry.register(Mothership())
AlienRegistry.register(Spacedock())
AlienRegistry.register(Stasis())
AlienRegistry.register(Hyperdrive())
AlienRegistry.register(Quantum_Alt())
AlienRegistry.register(Alien_Tech())
AlienRegistry.register(Terraformer())
AlienRegistry.register(Xenomorph())
