"""
Hand Tool Powers for Cosmic Encounter.
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
class Hammer_HT(AlienPower):
    """Hammer_HT - Power of Strike. +5 on offense"""
    name: str = field(default="Hammer_HT", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Screwdriver_HT(AlienPower):
    """Screwdriver_HT - Power of Turn. +5 always"""
    name: str = field(default="Screwdriver_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Wrench_HT(AlienPower):
    """Wrench_HT - Power of Grip. +5 always"""
    name: str = field(default="Wrench_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Pliers_HT(AlienPower):
    """Pliers_HT - Power of Pinch. +5 always"""
    name: str = field(default="Pliers_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Saw_HT(AlienPower):
    """Saw_HT - Power of Cut. +5 on offense"""
    name: str = field(default="Saw_HT", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Level_HT(AlienPower):
    """Level_HT - Power of Balance. +5 always"""
    name: str = field(default="Level_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Tape_Measure_HT(AlienPower):
    """Tape_Measure_HT - Power of Extend. +5 always"""
    name: str = field(default="Tape_Measure_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Drill_HT(AlienPower):
    """Drill_HT - Power of Bore. +5 on offense"""
    name: str = field(default="Drill_HT", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Chisel_HT(AlienPower):
    """Chisel_HT - Power of Carve. +5 always"""
    name: str = field(default="Chisel_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class File_HT(AlienPower):
    """File_HT - Power of Smooth. +5 always"""
    name: str = field(default="File_HT", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Clamp_HT(AlienPower):
    """Clamp_HT - Power of Hold. +5 on defense"""
    name: str = field(default="Clamp_HT", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Utility_Knife_HT(AlienPower):
    """Utility_Knife_HT - Power of Slice. +5 on offense"""
    name: str = field(default="Utility_Knife_HT", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Pry_Bar_HT(AlienPower):
    """Pry_Bar_HT - Power of Leverage. +4 always"""
    name: str = field(default="Pry_Bar_HT", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Impact_Driver_HT(AlienPower):
    """Impact_Driver_HT - Power of Force. +6 on offense"""
    name: str = field(default="Impact_Driver_HT", init=False)
    description: str = field(default="+6 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


HAND_TOOL_NEW_POWERS = [
    Hammer_HT, Screwdriver_HT, Wrench_HT, Pliers_HT, Saw_HT, Level_HT, Tape_Measure_HT,
    Drill_HT, Chisel_HT, File_HT, Clamp_HT, Utility_Knife_HT, Pry_Bar_HT, Impact_Driver_HT,
]

for power_class in HAND_TOOL_NEW_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
