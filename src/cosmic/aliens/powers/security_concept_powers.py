"""
Security Concept Powers for Cosmic Encounter.
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
class Firewall_Security(AlienPower):
    """Firewall_Security - Power of Block. +5 on defense"""
    name: str = field(default="Firewall_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class IDS_Security(AlienPower):
    """IDS_Security - Power of Detect. +5 on defense"""
    name: str = field(default="IDS_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class IPS_Security(AlienPower):
    """IPS_Security - Power of Prevent. +5 on defense"""
    name: str = field(default="IPS_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class WAF_Security(AlienPower):
    """WAF_Security - Power of Filter. +5 on defense"""
    name: str = field(default="WAF_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class DDoS_Protection_Security(AlienPower):
    """DDoS_Protection_Security - Power of Absorb. +5 on defense"""
    name: str = field(default="DDoS_Protection_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Penetration_Test_Security(AlienPower):
    """Penetration_Test_Security - Power of Probe. +5 on offense"""
    name: str = field(default="Penetration_Test_Security", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Vulnerability_Scan_Security(AlienPower):
    """Vulnerability_Scan_Security - Power of Find. +5 always"""
    name: str = field(default="Vulnerability_Scan_Security", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Patch_Management_Security(AlienPower):
    """Patch_Management_Security - Power of Update. +5 always"""
    name: str = field(default="Patch_Management_Security", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Access_Control_Security(AlienPower):
    """Access_Control_Security - Power of Restrict. +5 on defense"""
    name: str = field(default="Access_Control_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class MFA_Security(AlienPower):
    """MFA_Security - Power of Verify. +5 on defense"""
    name: str = field(default="MFA_Security", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Zero_Trust_Security(AlienPower):
    """Zero_Trust_Security - Power of Assume. +5 always"""
    name: str = field(default="Zero_Trust_Security", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class SIEM_Security(AlienPower):
    """SIEM_Security - Power of Correlate. +5 always"""
    name: str = field(default="SIEM_Security", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Honeypot_Security(AlienPower):
    """Honeypot_Security - Power of Trap. +4 on defense"""
    name: str = field(default="Honeypot_Security", init=False)
    description: str = field(default="+4 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class SOC_Security(AlienPower):
    """SOC_Security - Power of Center. +6 always"""
    name: str = field(default="SOC_Security", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


SECURITY_CONCEPT_POWERS = [
    Firewall_Security, IDS_Security, IPS_Security, WAF_Security, DDoS_Protection_Security, Penetration_Test_Security, Vulnerability_Scan_Security,
    Patch_Management_Security, Access_Control_Security, MFA_Security, Zero_Trust_Security, SIEM_Security, Honeypot_Security, SOC_Security,
]

for power_class in SECURITY_CONCEPT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
