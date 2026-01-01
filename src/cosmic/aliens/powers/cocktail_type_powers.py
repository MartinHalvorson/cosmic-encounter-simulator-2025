"""
Cocktail Type Powers for Cosmic Encounter.
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
class Martini_Cocktail(AlienPower):
    """Martini_Cocktail - Power of Classic. +5 always."""
    name: str = field(default="Martini_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Margarita_Cocktail(AlienPower):
    """Margarita_Cocktail - Power of Salt. +5 always."""
    name: str = field(default="Margarita_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Mojito_Cocktail(AlienPower):
    """Mojito_Cocktail - Power of Mint. +5 always."""
    name: str = field(default="Mojito_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Old_Fashioned_Cocktail(AlienPower):
    """Old_Fashioned_Cocktail - Power of Whiskey. +5 always."""
    name: str = field(default="Old_Fashioned_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Cosmopolitan_Cocktail(AlienPower):
    """Cosmopolitan_Cocktail - Power of Pink. +5 always."""
    name: str = field(default="Cosmopolitan_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Daiquiri_Cocktail(AlienPower):
    """Daiquiri_Cocktail - Power of Rum. +5 always."""
    name: str = field(default="Daiquiri_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Manhattan_Cocktail(AlienPower):
    """Manhattan_Cocktail - Power of City. +5 always."""
    name: str = field(default="Manhattan_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Negroni_Cocktail(AlienPower):
    """Negroni_Cocktail - Power of Bitter. +5 on offense."""
    name: str = field(default="Negroni_Cocktail", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Mai_Tai_Cocktail(AlienPower):
    """Mai_Tai_Cocktail - Power of Tiki. +5 always."""
    name: str = field(default="Mai_Tai_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Pina_Colada_Cocktail(AlienPower):
    """Pina_Colada_Cocktail - Power of Coconut. +5 always."""
    name: str = field(default="Pina_Colada_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Bloody_Mary_Cocktail(AlienPower):
    """Bloody_Mary_Cocktail - Power of Tomato. +5 always."""
    name: str = field(default="Bloody_Mary_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Whiskey_Sour_Cocktail(AlienPower):
    """Whiskey_Sour_Cocktail - Power of Citrus. +5 always."""
    name: str = field(default="Whiskey_Sour_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Sazerac_Cocktail(AlienPower):
    """Sazerac_Cocktail - Power of Anise. +5 always."""
    name: str = field(default="Sazerac_Cocktail", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Singapore_Sling_Cocktail(AlienPower):
    """Singapore_Sling_Cocktail - Power of Complex. +6 always."""
    name: str = field(default="Singapore_Sling_Cocktail", init=False)
    description: str = field(default="+6 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


COCKTAIL_TYPE_POWERS = [
    Martini_Cocktail, Margarita_Cocktail, Mojito_Cocktail, Old_Fashioned_Cocktail, Cosmopolitan_Cocktail, Daiquiri_Cocktail, Manhattan_Cocktail,
    Negroni_Cocktail, Mai_Tai_Cocktail, Pina_Colada_Cocktail, Bloody_Mary_Cocktail, Whiskey_Sour_Cocktail, Sazerac_Cocktail, Singapore_Sling_Cocktail,
]

for power_class in COCKTAIL_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
