"""
Tool and Equipment themed alien powers for Cosmic Encounter.
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
class Hammer(AlienPower):
    """Hammer - Power of Force."""
    name: str = field(default="Hammer", init=False)
    description: str = field(
        default="+5 when you play attack 20 or higher.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wrench(AlienPower):
    """Wrench - Power of Fixing."""
    name: str = field(default="Wrench", init=False)
    description: str = field(
        default="Retrieve 1 ship from warp at start of each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saw(AlienPower):
    """Saw - Power of Cutting."""
    name: str = field(default="Saw", init=False)
    description: str = field(
        default="Cut opponent's card value in half.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Drill(AlienPower):
    """Drill - Power of Penetration."""
    name: str = field(default="Drill", init=False)
    description: str = field(
        default="Ignore defender's reinforcement cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Screwdriver(AlienPower):
    """Screwdriver - Power of Adjustment."""
    name: str = field(default="Screwdriver", init=False)
    description: str = field(
        default="Modify your card value by +/- 3.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pliers(AlienPower):
    """Pliers - Power of Grip."""
    name: str = field(default="Pliers", init=False)
    description: str = field(
        default="Hold onto cards; can't be forced to discard.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Knife(AlienPower):
    """Knife - Power of Precision."""
    name: str = field(default="Knife", init=False)
    description: str = field(
        default="Remove 1 specific ship from encounter before combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lever(AlienPower):
    """Lever - Power of Advantage."""
    name: str = field(default="Lever", init=False)
    description: str = field(
        default="Your ships count as 1.5x (rounded down).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chisel(AlienPower):
    """Chisel - Power of Shaping."""
    name: str = field(default="Chisel", init=False)
    description: str = field(
        default="Change any negotiate to attack 10.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shovel(AlienPower):
    """Shovel - Power of Digging."""
    name: str = field(default="Shovel", init=False)
    description: str = field(
        default="Draw bottom card of cosmic deck instead of top.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Axe(AlienPower):
    """Axe - Power of Chopping."""
    name: str = field(default="Axe", init=False)
    description: str = field(
        default="Destroy 2 ships when you win as offense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Clamp(AlienPower):
    """Clamp - Power of Holding."""
    name: str = field(default="Clamp", init=False)
    description: str = field(
        default="Opponent can't retrieve ships from warp next turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Brush(AlienPower):
    """Brush - Power of Cleaning."""
    name: str = field(default="Brush", init=False)
    description: str = field(
        default="Remove 1 card from any discard pile.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Compass(AlienPower):
    """Compass - Power of Direction."""
    name: str = field(default="Compass", init=False)
    description: str = field(
        default="See top 3 destiny cards before drawing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wrench_Alt(AlienPower):
    """Wrench Alt - Power of Repair."""
    name: str = field(default="Wrench_Alt", init=False)
    description: str = field(
        default="Restore lost power once per game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Hammer())
AlienRegistry.register(Wrench())
AlienRegistry.register(Saw())
AlienRegistry.register(Drill())
AlienRegistry.register(Screwdriver())
AlienRegistry.register(Pliers())
AlienRegistry.register(Knife())
AlienRegistry.register(Lever())
AlienRegistry.register(Chisel())
AlienRegistry.register(Shovel())
AlienRegistry.register(Axe())
AlienRegistry.register(Clamp())
AlienRegistry.register(Brush())
AlienRegistry.register(Compass())
AlienRegistry.register(Wrench_Alt())
