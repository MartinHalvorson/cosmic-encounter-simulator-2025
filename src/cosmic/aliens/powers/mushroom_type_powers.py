"""
Mushroom Type Powers for Cosmic Encounter.
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
class Shiitake_Mushroom(AlienPower):
    """Shiitake_Mushroom - Power of Umami. +5 always."""
    name: str = field(default="Shiitake_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Portobello_Mushroom(AlienPower):
    """Portobello_Mushroom - Power of Meaty. +5 always."""
    name: str = field(default="Portobello_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Chanterelle_Mushroom(AlienPower):
    """Chanterelle_Mushroom - Power of Golden. +5 always."""
    name: str = field(default="Chanterelle_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Morel_Mushroom(AlienPower):
    """Morel_Mushroom - Power of Rare. +6 always."""
    name: str = field(default="Morel_Mushroom", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Oyster_Mushroom(AlienPower):
    """Oyster_Mushroom - Power of Tender. +5 always."""
    name: str = field(default="Oyster_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Truffle_Mushroom(AlienPower):
    """Truffle_Mushroom - Power of Luxury. +7 always."""
    name: str = field(default="Truffle_Mushroom", init=False)
    description: str = field(default="+7 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 7
        return total


@dataclass
class Porcini_Mushroom(AlienPower):
    """Porcini_Mushroom - Power of Nutty. +5 always."""
    name: str = field(default="Porcini_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Enoki_Mushroom(AlienPower):
    """Enoki_Mushroom - Power of Delicate. +4 always."""
    name: str = field(default="Enoki_Mushroom", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Maitake_Mushroom(AlienPower):
    """Maitake_Mushroom - Power of Dance. +5 always."""
    name: str = field(default="Maitake_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Cremini_Mushroom(AlienPower):
    """Cremini_Mushroom - Power of Common. +4 always."""
    name: str = field(default="Cremini_Mushroom", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class King_Trumpet_Mushroom(AlienPower):
    """King_Trumpet_Mushroom - Power of Royal. +5 always."""
    name: str = field(default="King_Trumpet_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Lion_Mane_Mushroom(AlienPower):
    """Lion_Mane_Mushroom - Power of Shaggy. +5 always."""
    name: str = field(default="Lion_Mane_Mushroom", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Reishi_Mushroom(AlienPower):
    """Reishi_Mushroom - Power of Immortal. +6 on defense."""
    name: str = field(default="Reishi_Mushroom", init=False)
    description: str = field(default="+6 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class Button_Mushroom(AlienPower):
    """Button_Mushroom - Power of Basic. +4 always."""
    name: str = field(default="Button_Mushroom", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


MUSHROOM_TYPE_POWERS = [
    Shiitake_Mushroom, Portobello_Mushroom, Chanterelle_Mushroom, Morel_Mushroom, Oyster_Mushroom, Truffle_Mushroom, Porcini_Mushroom,
    Enoki_Mushroom, Maitake_Mushroom, Cremini_Mushroom, King_Trumpet_Mushroom, Lion_Mane_Mushroom, Reishi_Mushroom, Button_Mushroom,
]

for power_class in MUSHROOM_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
