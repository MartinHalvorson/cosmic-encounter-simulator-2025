"""
Bird Type Powers for Cosmic Encounter.
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
class Eagle_Bird(AlienPower):
    """Eagle_Bird - Power of Soar. +6 on offense."""
    name: str = field(default="Eagle_Bird", init=False)
    description: str = field(default="+6 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Hawk_Bird(AlienPower):
    """Hawk_Bird - Power of Hunt. +5 on offense."""
    name: str = field(default="Hawk_Bird", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Owl_Bird(AlienPower):
    """Owl_Bird - Power of Night. +5 on defense."""
    name: str = field(default="Owl_Bird", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Falcon_Bird(AlienPower):
    """Falcon_Bird - Power of Speed. +6 on offense."""
    name: str = field(default="Falcon_Bird", init=False)
    description: str = field(default="+6 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Sparrow_Bird(AlienPower):
    """Sparrow_Bird - Power of Quick. +4 always."""
    name: str = field(default="Sparrow_Bird", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Crow_Bird(AlienPower):
    """Crow_Bird - Power of Smart. +5 always."""
    name: str = field(default="Crow_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Raven_Bird(AlienPower):
    """Raven_Bird - Power of Omen. +5 always."""
    name: str = field(default="Raven_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hummingbird_Bird(AlienPower):
    """Hummingbird_Bird - Power of Hover. +5 always."""
    name: str = field(default="Hummingbird_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Peacock_Bird(AlienPower):
    """Peacock_Bird - Power of Display. +5 always."""
    name: str = field(default="Peacock_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Penguin_Bird(AlienPower):
    """Penguin_Bird - Power of Waddle. +5 on defense."""
    name: str = field(default="Penguin_Bird", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Flamingo_Bird(AlienPower):
    """Flamingo_Bird - Power of Stand. +5 always."""
    name: str = field(default="Flamingo_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Pelican_Bird(AlienPower):
    """Pelican_Bird - Power of Scoop. +5 always."""
    name: str = field(default="Pelican_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Parrot_Bird(AlienPower):
    """Parrot_Bird - Power of Mimic. +5 always."""
    name: str = field(default="Parrot_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Swan_Bird(AlienPower):
    """Swan_Bird - Power of Grace. +5 always."""
    name: str = field(default="Swan_Bird", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


BIRD_TYPE_POWERS = [
    Eagle_Bird, Hawk_Bird, Owl_Bird, Falcon_Bird, Sparrow_Bird, Crow_Bird, Raven_Bird,
    Hummingbird_Bird, Peacock_Bird, Penguin_Bird, Flamingo_Bird, Pelican_Bird, Parrot_Bird, Swan_Bird,
]

for power_class in BIRD_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
