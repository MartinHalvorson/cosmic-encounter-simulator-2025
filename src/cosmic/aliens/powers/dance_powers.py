"""
Dance and Movement themed alien powers for Cosmic Encounter.
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
class Dancer(AlienPower):
    """Dancer - Power of Movement."""
    name: str = field(default="Dancer", init=False)
    description: str = field(
        default="Move 2 ships between colonies after each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Waltz(AlienPower):
    """Waltz - Power of Three."""
    name: str = field(default="Waltz", init=False)
    description: str = field(
        default="+3 when you have exactly 3 ships in the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tango(AlienPower):
    """Tango - Power of Partnership."""
    name: str = field(default="Tango", init=False)
    description: str = field(
        default="Choose 1 ally; you both get +2.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ballet(AlienPower):
    """Ballet - Power of Grace."""
    name: str = field(default="Ballet", init=False)
    description: str = field(
        default="Avoid losing ships when negotiation fails.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Breakdance(AlienPower):
    """Breakdance - Power of Style."""
    name: str = field(default="Breakdance", init=False)
    description: str = field(
        default="+4 when playing attack 10 or lower.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Salsa(AlienPower):
    """Salsa - Power of Heat."""
    name: str = field(default="Salsa", init=False)
    description: str = field(
        default="+2 for each card in opponent's hand over 5.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swing(AlienPower):
    """Swing - Power of Momentum."""
    name: str = field(default="Swing", init=False)
    description: str = field(
        default="After winning, immediately attack same opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class HipHop(AlienPower):
    """HipHop - Power of Flow."""
    name: str = field(default="HipHop", init=False)
    description: str = field(
        default="Draw 1 card for each ally on your side.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flamenco(AlienPower):
    """Flamenco - Power of Passion."""
    name: str = field(default="Flamenco", init=False)
    description: str = field(
        default="+5 when you have fewer ships than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tap(AlienPower):
    """Tap - Power of Rhythm."""
    name: str = field(default="Tap", init=False)
    description: str = field(
        default="Once per turn, replay a card from discard.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Dancer())
AlienRegistry.register(Waltz())
AlienRegistry.register(Tango())
AlienRegistry.register(Ballet())
AlienRegistry.register(Breakdance())
AlienRegistry.register(Salsa())
AlienRegistry.register(Swing())
AlienRegistry.register(HipHop())
AlienRegistry.register(Flamenco())
AlienRegistry.register(Tap())
