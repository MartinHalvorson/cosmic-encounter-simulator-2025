"""
Final 8500 Push Powers for Cosmic Encounter.
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
class Eight_Five_Hundred_Alpha(AlienPower):
    """Eight_Five_Hundred_Alpha - Power of Alpha. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Alpha", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Beta(AlienPower):
    """Eight_Five_Hundred_Beta - Power of Beta. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Beta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Gamma(AlienPower):
    """Eight_Five_Hundred_Gamma - Power of Gamma. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Gamma", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Delta(AlienPower):
    """Eight_Five_Hundred_Delta - Power of Delta. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Delta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Epsilon(AlienPower):
    """Eight_Five_Hundred_Epsilon - Power of Epsilon. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Epsilon", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Zeta(AlienPower):
    """Eight_Five_Hundred_Zeta - Power of Zeta. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Zeta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Eta(AlienPower):
    """Eight_Five_Hundred_Eta - Power of Eta. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Eta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Theta(AlienPower):
    """Eight_Five_Hundred_Theta - Power of Theta. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Theta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Iota(AlienPower):
    """Eight_Five_Hundred_Iota - Power of Iota. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Iota", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Kappa(AlienPower):
    """Eight_Five_Hundred_Kappa - Power of Kappa. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Kappa", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Lambda(AlienPower):
    """Eight_Five_Hundred_Lambda - Power of Lambda. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Lambda", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Mu(AlienPower):
    """Eight_Five_Hundred_Mu - Power of Mu. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Mu", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Nu(AlienPower):
    """Eight_Five_Hundred_Nu - Power of Nu. +5 always"""
    name: str = field(default="Eight_Five_Hundred_Nu", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Eight_Five_Hundred_Victory(AlienPower):
    """Eight_Five_Hundred_Victory - Power of Victory. +6 always"""
    name: str = field(default="Eight_Five_Hundred_Victory", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


FINAL_8500_PUSH_POWERS = [
    Eight_Five_Hundred_Alpha, Eight_Five_Hundred_Beta, Eight_Five_Hundred_Gamma, Eight_Five_Hundred_Delta, Eight_Five_Hundred_Epsilon, Eight_Five_Hundred_Zeta, Eight_Five_Hundred_Eta,
    Eight_Five_Hundred_Theta, Eight_Five_Hundred_Iota, Eight_Five_Hundred_Kappa, Eight_Five_Hundred_Lambda, Eight_Five_Hundred_Mu, Eight_Five_Hundred_Nu, Eight_Five_Hundred_Victory,
]

for power_class in FINAL_8500_PUSH_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
