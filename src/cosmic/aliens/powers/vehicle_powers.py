"""
Vehicle and Transport themed alien powers for Cosmic Encounter.
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
class Rocket(AlienPower):
    """Rocket - Power of Launch."""
    name: str = field(default="Rocket", init=False)
    description: str = field(
        default="+4 when attacking from your home system.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Submarine(AlienPower):
    """Submarine - Power of Stealth."""
    name: str = field(default="Submarine", init=False)
    description: str = field(
        default="Your attack card is hidden until resolution.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tank(AlienPower):
    """Tank - Power of Armor."""
    name: str = field(default="Tank", init=False)
    description: str = field(
        default="First 2 ships lost each encounter go to colonies instead.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Helicopter(AlienPower):
    """Helicopter - Power of Hovering."""
    name: str = field(default="Helicopter", init=False)
    description: str = field(
        default="Choose to cancel encounter after cards are revealed.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Train(AlienPower):
    """Train - Power of Momentum."""
    name: str = field(default="Train", init=False)
    description: str = field(
        default="+1 for each consecutive encounter you've won.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spaceship(AlienPower):
    """Spaceship - Power of Travel."""
    name: str = field(default="Spaceship", init=False)
    description: str = field(
        default="Attack any planet regardless of destiny.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bicycle(AlienPower):
    """Bicycle - Power of Efficiency."""
    name: str = field(default="Bicycle", init=False)
    description: str = field(
        default="Your single ships count as 2 in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Airplane(AlienPower):
    """Airplane - Power of Altitude."""
    name: str = field(default="Airplane", init=False)
    description: str = field(
        default="Ships can't be targeted by trap cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Boat(AlienPower):
    """Boat - Power of Crossing."""
    name: str = field(default="Boat", init=False)
    description: str = field(
        default="Carry 1 ally ship with your ships for free.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bus(AlienPower):
    """Bus - Power of Capacity."""
    name: str = field(default="Bus", init=False)
    description: str = field(
        default="Commit up to 6 ships instead of 4.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Motorcycle(AlienPower):
    """Motorcycle - Power of Speed."""
    name: str = field(default="Motorcycle", init=False)
    description: str = field(
        default="+3 when you have fewer ships than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Truck(AlienPower):
    """Truck - Power of Hauling."""
    name: str = field(default="Truck", init=False)
    description: str = field(
        default="Draw 2 extra cards at start of turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Rocket())
AlienRegistry.register(Submarine())
AlienRegistry.register(Tank())
AlienRegistry.register(Helicopter())
AlienRegistry.register(Train())
AlienRegistry.register(Spaceship())
AlienRegistry.register(Bicycle())
AlienRegistry.register(Airplane())
AlienRegistry.register(Boat())
AlienRegistry.register(Bus())
AlienRegistry.register(Motorcycle())
AlienRegistry.register(Truck())
