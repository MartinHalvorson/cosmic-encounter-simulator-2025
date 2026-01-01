"""
Crystal Type Powers for Cosmic Encounter.
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
class Amethyst_Crystal(AlienPower):
    """Amethyst_Crystal - Power of Purple. +5 always."""
    name: str = field(default="Amethyst_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Citrine_Crystal(AlienPower):
    """Citrine_Crystal - Power of Yellow. +5 on offense."""
    name: str = field(default="Citrine_Crystal", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Rose_Quartz_Crystal(AlienPower):
    """Rose_Quartz_Crystal - Power of Love. +5 always."""
    name: str = field(default="Rose_Quartz_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Clear_Quartz_Crystal(AlienPower):
    """Clear_Quartz_Crystal - Power of Amplify. +6 always."""
    name: str = field(default="Clear_Quartz_Crystal", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Smoky_Quartz_Crystal(AlienPower):
    """Smoky_Quartz_Crystal - Power of Ground. +5 on defense."""
    name: str = field(default="Smoky_Quartz_Crystal", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Tiger_Eye_Crystal(AlienPower):
    """Tiger_Eye_Crystal - Power of Courage. +5 on offense."""
    name: str = field(default="Tiger_Eye_Crystal", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Moonstone_Crystal(AlienPower):
    """Moonstone_Crystal - Power of Intuition. +5 always."""
    name: str = field(default="Moonstone_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Labradorite_Crystal(AlienPower):
    """Labradorite_Crystal - Power of Transform. +5 always."""
    name: str = field(default="Labradorite_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Fluorite_Crystal(AlienPower):
    """Fluorite_Crystal - Power of Focus. +5 always."""
    name: str = field(default="Fluorite_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Selenite_Crystal(AlienPower):
    """Selenite_Crystal - Power of Cleanse. +5 on defense."""
    name: str = field(default="Selenite_Crystal", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Aventurine_Crystal(AlienPower):
    """Aventurine_Crystal - Power of Luck. +5 always."""
    name: str = field(default="Aventurine_Crystal", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Carnelian_Crystal(AlienPower):
    """Carnelian_Crystal - Power of Motivate. +5 on offense."""
    name: str = field(default="Carnelian_Crystal", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Lapis_Lazuli_Crystal(AlienPower):
    """Lapis_Lazuli_Crystal - Power of Wisdom. +6 always."""
    name: str = field(default="Lapis_Lazuli_Crystal", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Malachite_Crystal(AlienPower):
    """Malachite_Crystal - Power of Protect. +5 on defense."""
    name: str = field(default="Malachite_Crystal", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


CRYSTAL_TYPE_POWERS = [
    Amethyst_Crystal, Citrine_Crystal, Rose_Quartz_Crystal, Clear_Quartz_Crystal, Smoky_Quartz_Crystal, Tiger_Eye_Crystal, Moonstone_Crystal,
    Labradorite_Crystal, Fluorite_Crystal, Selenite_Crystal, Aventurine_Crystal, Carnelian_Crystal, Lapis_Lazuli_Crystal, Malachite_Crystal,
]

for power_class in CRYSTAL_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
