"""
DevOps Powers for Cosmic Encounter.
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
class CI_Dv(AlienPower):
    """CI_Dv - Power of Integrate. +5 always"""
    name: str = field(default="CI_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class CD_Dv(AlienPower):
    """CD_Dv - Power of Deploy. +5 always"""
    name: str = field(default="CD_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Docker_Dv(AlienPower):
    """Docker_Dv - Power of Container. +5 always"""
    name: str = field(default="Docker_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Kubernetes_Dv(AlienPower):
    """Kubernetes_Dv - Power of Orchestrate. +5 always"""
    name: str = field(default="Kubernetes_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Terraform_Dv(AlienPower):
    """Terraform_Dv - Power of Infra. +5 always"""
    name: str = field(default="Terraform_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ansible_Dv(AlienPower):
    """Ansible_Dv - Power of Config. +5 always"""
    name: str = field(default="Ansible_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Jenkins_Dv(AlienPower):
    """Jenkins_Dv - Power of Pipeline. +5 always"""
    name: str = field(default="Jenkins_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Git_Dv(AlienPower):
    """Git_Dv - Power of Version. +5 always"""
    name: str = field(default="Git_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Monitoring_Dv(AlienPower):
    """Monitoring_Dv - Power of Observe. +5 on defense"""
    name: str = field(default="Monitoring_Dv", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Logging_Dv(AlienPower):
    """Logging_Dv - Power of Record. +5 always"""
    name: str = field(default="Logging_Dv", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Alerting_Dv(AlienPower):
    """Alerting_Dv - Power of Warn. +5 on defense"""
    name: str = field(default="Alerting_Dv", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Rollback_Dv(AlienPower):
    """Rollback_Dv - Power of Revert. +5 on defense"""
    name: str = field(default="Rollback_Dv", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Canary_Dv(AlienPower):
    """Canary_Dv - Power of Test. +4 always"""
    name: str = field(default="Canary_Dv", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Blue_Green_Dv(AlienPower):
    """Blue_Green_Dv - Power of Switch. +6 always"""
    name: str = field(default="Blue_Green_Dv", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


DEVOPS_NEW_POWERS = [
    CI_Dv, CD_Dv, Docker_Dv, Kubernetes_Dv, Terraform_Dv, Ansible_Dv, Jenkins_Dv,
    Git_Dv, Monitoring_Dv, Logging_Dv, Alerting_Dv, Rollback_Dv, Canary_Dv, Blue_Green_Dv,
]

for power_class in DEVOPS_NEW_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
