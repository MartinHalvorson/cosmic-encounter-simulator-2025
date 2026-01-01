"""
9000 B Powers for Cosmic Encounter.
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
class Nine_K_Alpha_B(AlienPower):
    """Nine_K_Alpha_B - Power of Alpha. +5 always"""
    name: str = field(default="Nine_K_Alpha_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Beta_B(AlienPower):
    """Nine_K_Beta_B - Power of Beta. +5 always"""
    name: str = field(default="Nine_K_Beta_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Gamma_B(AlienPower):
    """Nine_K_Gamma_B - Power of Gamma. +5 always"""
    name: str = field(default="Nine_K_Gamma_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Delta_B(AlienPower):
    """Nine_K_Delta_B - Power of Delta. +5 always"""
    name: str = field(default="Nine_K_Delta_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Epsilon_B(AlienPower):
    """Nine_K_Epsilon_B - Power of Epsilon. +5 always"""
    name: str = field(default="Nine_K_Epsilon_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Zeta_B(AlienPower):
    """Nine_K_Zeta_B - Power of Zeta. +5 always"""
    name: str = field(default="Nine_K_Zeta_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Eta_B(AlienPower):
    """Nine_K_Eta_B - Power of Eta. +5 always"""
    name: str = field(default="Nine_K_Eta_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Theta_B(AlienPower):
    """Nine_K_Theta_B - Power of Theta. +5 always"""
    name: str = field(default="Nine_K_Theta_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Iota_B(AlienPower):
    """Nine_K_Iota_B - Power of Iota. +5 always"""
    name: str = field(default="Nine_K_Iota_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Kappa_B(AlienPower):
    """Nine_K_Kappa_B - Power of Kappa. +5 always"""
    name: str = field(default="Nine_K_Kappa_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Lambda_B(AlienPower):
    """Nine_K_Lambda_B - Power of Lambda. +5 always"""
    name: str = field(default="Nine_K_Lambda_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Mu_B(AlienPower):
    """Nine_K_Mu_B - Power of Mu. +5 always"""
    name: str = field(default="Nine_K_Mu_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Nine_K_Nu_B(AlienPower):
    """Nine_K_Nu_B - Power of Nu. +4 always"""
    name: str = field(default="Nine_K_Nu_B", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Nine_Thousand_Milestone(AlienPower):
    """Nine_Thousand_Milestone - Power of Victory. +6 always"""
    name: str = field(default="Nine_Thousand_Milestone", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


NINE_THOUSAND_B_POWERS = [
    Nine_K_Alpha_B, Nine_K_Beta_B, Nine_K_Gamma_B, Nine_K_Delta_B, Nine_K_Epsilon_B, Nine_K_Zeta_B, Nine_K_Eta_B,
    Nine_K_Theta_B, Nine_K_Iota_B, Nine_K_Kappa_B, Nine_K_Lambda_B, Nine_K_Mu_B, Nine_K_Nu_B, Nine_Thousand_Milestone,
]

for power_class in NINE_THOUSAND_B_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
