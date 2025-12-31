"""
Vehicle-themed alien powers.

These aliens are inspired by various modes of transportation.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Racecar(AlienPower):
    """Racecar - Power of Speed. Always have 2 encounters per turn."""
    name: str = field(default="Racecar", init=False)
    description: str = field(default="Always have 2 encounters per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tank_Vehicle(AlienPower):
    """Tank - Power of Armor. +5 when on defense."""
    name: str = field(default="Tank_Vehicle", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Helicopter(AlienPower):
    """Helicopter - Power of Hover. May attack any planet, ignoring destiny."""
    name: str = field(default="Helicopter", init=False)
    description: str = field(default="Choose any planet to attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Submarine_Vehicle(AlienPower):
    """Submarine - Power of Stealth. Opponent doesn't know your card value."""
    name: str = field(default="Submarine_Vehicle", init=False)
    description: str = field(default="Your card is hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rocket_Vehicle(AlienPower):
    """Rocket - Power of Launch. +3 on first encounter of game."""
    name: str = field(default="Rocket_Vehicle", init=False)
    description: str = field(default="+3 on first encounter of game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn == 1:
            return total + 3
        return total


@dataclass
class Train_Vehicle(AlienPower):
    """Train - Power of Momentum. +1 for each consecutive win (max +5)."""
    name: str = field(default="Train_Vehicle", init=False)
    description: str = field(default="+1 for each consecutive win (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    consecutive_wins: int = field(default=0, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(self.consecutive_wins, 5)
        return total


@dataclass
class Bicycle_Vehicle(AlienPower):
    """Bicycle - Power of Simplicity. +2 when you have exactly 1 ship."""
    name: str = field(default="Bicycle_Vehicle", init=False)
    description: str = field(default="+2 when you have exactly 1 ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Airplane_Vehicle(AlienPower):
    """Airplane - Power of Flight. Ships can come from any colony."""
    name: str = field(default="Airplane_Vehicle", init=False)
    description: str = field(default="Commit ships from any of your colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boat_Vehicle(AlienPower):
    """Boat - Power of Sailing. +2 when attacking."""
    name: str = field(default="Boat_Vehicle", init=False)
    description: str = field(default="+2 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 2
        return total


@dataclass
class Spaceship_Vehicle(AlienPower):
    """Spaceship - Power of Exploration. Draw 1 card when winning as offense."""
    name: str = field(default="Spaceship_Vehicle", init=False)
    description: str = field(default="Draw 1 card when winning as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Motorcycle_Vehicle(AlienPower):
    """Motorcycle - Power of Agility. May withdraw half ships before resolution."""
    name: str = field(default="Motorcycle_Vehicle", init=False)
    description: str = field(default="May withdraw half ships before resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Truck_Vehicle(AlienPower):
    """Truck - Power of Cargo. May commit up to 6 ships."""
    name: str = field(default="Truck_Vehicle", init=False)
    description: str = field(default="May commit up to 6 ships to encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bus_Vehicle(AlienPower):
    """Bus - Power of Transport. Allies add +2 each."""
    name: str = field(default="Bus_Vehicle", init=False)
    description: str = field(default="Allied ships on your side add +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ambulance_Vehicle(AlienPower):
    """Ambulance - Power of Rescue. Return 2 ships from warp at turn start."""
    name: str = field(default="Ambulance_Vehicle", init=False)
    description: str = field(default="Return 2 ships from warp at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Firetruck_Vehicle(AlienPower):
    """Firetruck - Power of Emergency. +4 when defending home planet."""
    name: str = field(default="Firetruck_Vehicle", init=False)
    description: str = field(default="+4 when defending a home planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


# Register all vehicle powers
AlienRegistry.register(Racecar())
AlienRegistry.register(Tank_Vehicle())
AlienRegistry.register(Helicopter())
AlienRegistry.register(Submarine_Vehicle())
AlienRegistry.register(Rocket_Vehicle())
AlienRegistry.register(Train_Vehicle())
AlienRegistry.register(Bicycle_Vehicle())
AlienRegistry.register(Airplane_Vehicle())
AlienRegistry.register(Boat_Vehicle())
AlienRegistry.register(Spaceship_Vehicle())
AlienRegistry.register(Motorcycle_Vehicle())
AlienRegistry.register(Truck_Vehicle())
AlienRegistry.register(Bus_Vehicle())
AlienRegistry.register(Ambulance_Vehicle())
AlienRegistry.register(Firetruck_Vehicle())
