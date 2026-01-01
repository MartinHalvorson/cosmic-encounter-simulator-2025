"""
Force Type Powers for Cosmic Encounter.
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
class Gravitational_Force(AlienPower):
    """Gravitational_Force - Power of Attract. +5 always."""
    name: str = field(default="Gravitational_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Electromagnetic_Force(AlienPower):
    """Electromagnetic_Force - Power of Charge. +5 always."""
    name: str = field(default="Electromagnetic_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Strong_Nuclear_Force(AlienPower):
    """Strong_Nuclear_Force - Power of Bind. +6 on defense."""
    name: str = field(default="Strong_Nuclear_Force", init=False)
    description: str = field(default="+6 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class Weak_Nuclear_Force(AlienPower):
    """Weak_Nuclear_Force - Power of Decay. +5 on offense."""
    name: str = field(default="Weak_Nuclear_Force", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Friction_Force(AlienPower):
    """Friction_Force - Power of Resist. +5 on defense."""
    name: str = field(default="Friction_Force", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Tension_Force(AlienPower):
    """Tension_Force - Power of Pull. +5 always."""
    name: str = field(default="Tension_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Normal_Force(AlienPower):
    """Normal_Force - Power of Support. +5 on defense."""
    name: str = field(default="Normal_Force", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Applied_Force(AlienPower):
    """Applied_Force - Power of Push. +5 on offense."""
    name: str = field(default="Applied_Force", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Spring_Force(AlienPower):
    """Spring_Force - Power of Restore. +5 always."""
    name: str = field(default="Spring_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Drag_Force(AlienPower):
    """Drag_Force - Power of Slow. +5 on defense."""
    name: str = field(default="Drag_Force", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Buoyant_Force(AlienPower):
    """Buoyant_Force - Power of Float. +5 always."""
    name: str = field(default="Buoyant_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Centripetal_Force(AlienPower):
    """Centripetal_Force - Power of Center. +5 always."""
    name: str = field(default="Centripetal_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Centrifugal_Force(AlienPower):
    """Centrifugal_Force - Power of Outward. +5 on offense."""
    name: str = field(default="Centrifugal_Force", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Magnetic_Force(AlienPower):
    """Magnetic_Force - Power of Pole. +5 always."""
    name: str = field(default="Magnetic_Force", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


FORCE_TYPE_POWERS = [
    Gravitational_Force, Electromagnetic_Force, Strong_Nuclear_Force, Weak_Nuclear_Force, Friction_Force, Tension_Force, Normal_Force,
    Applied_Force, Spring_Force, Drag_Force, Buoyant_Force, Centripetal_Force, Centrifugal_Force, Magnetic_Force,
]

for power_class in FORCE_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
