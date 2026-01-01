"""
Flower Type Powers for Cosmic Encounter.
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
class Rose_Flower(AlienPower):
    """Rose_Flower - Power of Love. +5 always."""
    name: str = field(default="Rose_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Tulip_Flower(AlienPower):
    """Tulip_Flower - Power of Spring. +5 always."""
    name: str = field(default="Tulip_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Sunflower_Flower(AlienPower):
    """Sunflower_Flower - Power of Sun. +5 on offense."""
    name: str = field(default="Sunflower_Flower", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Daisy_Flower(AlienPower):
    """Daisy_Flower - Power of Simple. +4 always."""
    name: str = field(default="Daisy_Flower", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Lily_Flower(AlienPower):
    """Lily_Flower - Power of Pure. +5 always."""
    name: str = field(default="Lily_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Orchid_Flower(AlienPower):
    """Orchid_Flower - Power of Exotic. +6 always."""
    name: str = field(default="Orchid_Flower", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Jasmine_Flower(AlienPower):
    """Jasmine_Flower - Power of Fragrance. +5 always."""
    name: str = field(default="Jasmine_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Lotus_Flower(AlienPower):
    """Lotus_Flower - Power of Enlighten. +6 always."""
    name: str = field(default="Lotus_Flower", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Carnation_Flower(AlienPower):
    """Carnation_Flower - Power of Mother. +5 always."""
    name: str = field(default="Carnation_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Violet_Flower(AlienPower):
    """Violet_Flower - Power of Modest. +4 always."""
    name: str = field(default="Violet_Flower", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Daffodil_Flower(AlienPower):
    """Daffodil_Flower - Power of Cheer. +5 always."""
    name: str = field(default="Daffodil_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Peony_Flower(AlienPower):
    """Peony_Flower - Power of Honor. +5 always."""
    name: str = field(default="Peony_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Magnolia_Flower(AlienPower):
    """Magnolia_Flower - Power of Noble. +5 always."""
    name: str = field(default="Magnolia_Flower", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Lavender_Flower(AlienPower):
    """Lavender_Flower - Power of Calm. +5 on defense."""
    name: str = field(default="Lavender_Flower", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


FLOWER_TYPE_POWERS = [
    Rose_Flower, Tulip_Flower, Sunflower_Flower, Daisy_Flower, Lily_Flower, Orchid_Flower, Jasmine_Flower,
    Lotus_Flower, Carnation_Flower, Violet_Flower, Daffodil_Flower, Peony_Flower, Magnolia_Flower, Lavender_Flower,
]

for power_class in FLOWER_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
