"""
Arthurian legend themed alien powers for Cosmic Encounter.
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
class King_Arthur(AlienPower):
    """King_Arthur - Once and future king. +5 always."""
    name: str = field(default="King_Arthur", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Merlin(AlienPower):
    """Merlin - Wizard prophet. See opponent card."""
    name: str = field(default="Merlin", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lancelot(AlienPower):
    """Lancelot - Greatest knight. +6 attacking."""
    name: str = field(default="Lancelot", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Guinevere(AlienPower):
    """Guinevere - Queen of Camelot. +3 and draw card."""
    name: str = field(default="Guinevere", init=False)
    description: str = field(default="+3 plus draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Galahad(AlienPower):
    """Galahad - Perfect knight. +4 defending."""
    name: str = field(default="Galahad", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Morgan_Le_Fay(AlienPower):
    """Morgan_Le_Fay - Dark sorceress. Random +0-8."""
    name: str = field(default="Morgan_Le_Fay", init=False)
    description: str = field(default="Random +0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 8)
        return total


@dataclass
class Gawain(AlienPower):
    """Gawain - Solar knight. +4 first encounter."""
    name: str = field(default="Gawain", init=False)
    description: str = field(default="+4 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Percival(AlienPower):
    """Percival - Grail knight. Retrieve 3 ships."""
    name: str = field(default="Percival", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mordred(AlienPower):
    """Mordred - Traitor knight. +5 offense, -2 defense."""
    name: str = field(default="Mordred", init=False)
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
class Nimue(AlienPower):
    """Nimue - Lady of Lake. Win ties."""
    name: str = field(default="Nimue", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kay(AlienPower):
    """Kay - Seneschal. +2 per home colony."""
    name: str = field(default="Kay", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tristan(AlienPower):
    """Tristan - Tragic knight. +1 per ally."""
    name: str = field(default="Tristan", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Green_Knight(AlienPower):
    """Green_Knight - Immortal challenger. Ships go home."""
    name: str = field(default="Green_Knight", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bedivere(AlienPower):
    """Bedivere - Last knight. +3 defending home."""
    name: str = field(default="Bedivere", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Excalibur(AlienPower):
    """Excalibur - Sacred sword. +1 per card."""
    name: str = field(default="Excalibur", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


# Register all powers
ARTHURIAN_POWERS = [
    King_Arthur, Merlin, Lancelot, Guinevere, Galahad, Morgan_Le_Fay,
    Gawain, Percival, Mordred, Nimue, Kay, Tristan, Green_Knight,
    Bedivere, Excalibur,
]

for power_class in ARTHURIAN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
