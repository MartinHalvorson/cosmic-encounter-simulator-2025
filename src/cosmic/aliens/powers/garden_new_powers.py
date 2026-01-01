"""
Garden Powers for Cosmic Encounter.
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
class Shovel_Grd(AlienPower):
    """Shovel_Grd - Power of Dig. +5 always"""
    name: str = field(default="Shovel_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Rake_Grd(AlienPower):
    """Rake_Grd - Power of Gather. +5 always"""
    name: str = field(default="Rake_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hoe_Grd(AlienPower):
    """Hoe_Grd - Power of Cultivate. +5 always"""
    name: str = field(default="Hoe_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Pruner_Grd(AlienPower):
    """Pruner_Grd - Power of Trim. +5 always"""
    name: str = field(default="Pruner_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Trowel_Grd(AlienPower):
    """Trowel_Grd - Power of Plant. +5 always"""
    name: str = field(default="Trowel_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Watering_Can_Grd(AlienPower):
    """Watering_Can_Grd - Power of Hydrate. +5 always"""
    name: str = field(default="Watering_Can_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hose_Grd(AlienPower):
    """Hose_Grd - Power of Spray. +5 always"""
    name: str = field(default="Hose_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Wheelbarrow_Grd(AlienPower):
    """Wheelbarrow_Grd - Power of Haul. +5 always"""
    name: str = field(default="Wheelbarrow_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Lawn_Mower_Grd(AlienPower):
    """Lawn_Mower_Grd - Power of Cut. +5 on offense"""
    name: str = field(default="Lawn_Mower_Grd", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Hedge_Trimmer_Grd(AlienPower):
    """Hedge_Trimmer_Grd - Power of Shape. +5 always"""
    name: str = field(default="Hedge_Trimmer_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Leaf_Blower_Grd(AlienPower):
    """Leaf_Blower_Grd - Power of Clear. +5 always"""
    name: str = field(default="Leaf_Blower_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Seed_Spreader_Grd(AlienPower):
    """Seed_Spreader_Grd - Power of Distribute. +5 always"""
    name: str = field(default="Seed_Spreader_Grd", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Garden_Fork_Grd(AlienPower):
    """Garden_Fork_Grd - Power of Turn. +4 always"""
    name: str = field(default="Garden_Fork_Grd", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Chainsaw_Grd(AlienPower):
    """Chainsaw_Grd - Power of Power. +6 on offense"""
    name: str = field(default="Chainsaw_Grd", init=False)
    description: str = field(default="+6 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


GARDEN_NEW_POWERS = [
    Shovel_Grd, Rake_Grd, Hoe_Grd, Pruner_Grd, Trowel_Grd, Watering_Can_Grd, Hose_Grd,
    Wheelbarrow_Grd, Lawn_Mower_Grd, Hedge_Trimmer_Grd, Leaf_Blower_Grd, Seed_Spreader_Grd, Garden_Fork_Grd, Chainsaw_Grd,
]

for power_class in GARDEN_NEW_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
