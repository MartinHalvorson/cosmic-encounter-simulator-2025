"""
Brazilian/South American Powers - Brazilian folklore themed aliens.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Iara(AlienPower):
    """Iara - River mermaid. +4 on offense."""
    name: str = field(default="Iara", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Curupira(AlienPower):
    """Curupira - Forest guardian. +4 on defense."""
    name: str = field(default="Curupira", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Boitata(AlienPower):
    """Boitata - Fire serpent. +5 offense, -2 defense."""
    name: str = field(default="Boitata", init=False)
    description: str = field(default="+5 offense, -2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                return total + 5
            return total - 2
        return total


@dataclass
class Saci(AlienPower):
    """Saci - One-legged trickster. +2 always."""
    name: str = field(default="Saci", init=False)
    description: str = field(default="+2 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Anhanga(AlienPower):
    """Anhanga - Ghost spirit. Retrieve 3 ships."""
    name: str = field(default="Anhanga", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jaci(AlienPower):
    """Jaci - Moon goddess. Win ties."""
    name: str = field(default="Jaci", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class MulaSemCabeca(AlienPower):
    """MulaSemCabeca - Headless mule. See opponent card."""
    name: str = field(default="MulaSemCabeca", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Iemanja(AlienPower):
    """Iemanja - Sea mother. +2 per home colony."""
    name: str = field(default="Iemanja", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + (home_count * 2)
        return total


@dataclass
class Caipora(AlienPower):
    """Caipora - Forest spirit. +3 first encounter."""
    name: str = field(default="Caipora", init=False)
    description: str = field(default="+3 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Mapinguari(AlienPower):
    """Mapinguari - Beast man. Random +0 to +6."""
    name: str = field(default="Mapinguari", init=False)
    description: str = field(default="Random +0 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 6)
        return total


@dataclass
class BotoPink(AlienPower):
    """BotoPink - River dolphin. +3 defending home."""
    name: str = field(default="BotoPink", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 3
        return total


@dataclass
class Lobisomem(AlienPower):
    """Lobisomem - Werewolf. -2 to opponent."""
    name: str = field(default="Lobisomem", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class NegroDAgua(AlienPower):
    """NegroDAgua - Water spirit. +1 per ally."""
    name: str = field(default="NegroDAgua", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tupinamba(AlienPower):
    """Tupinamba - Spirit. +1 per card."""
    name: str = field(default="Tupinamba", init=False)
    description: str = field(default="+1 per card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Oxum(AlienPower):
    """Oxum - River goddess. Ships go home."""
    name: str = field(default="Oxum", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
BRAZILIAN_POWERS = [
    Iara, Curupira, Boitata, Saci, Anhanga, Jaci, MulaSemCabeca, Iemanja,
    Caipora, Mapinguari, BotoPink, Lobisomem, NegroDAgua, Tupinamba, Oxum,
]

for power_class in BRAZILIAN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
