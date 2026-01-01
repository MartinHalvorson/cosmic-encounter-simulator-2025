"""
Mesopotamian mythology themed alien powers for Cosmic Encounter.
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
class Marduk(AlienPower):
    """Marduk - King of gods. +5 always."""
    name: str = field(default="Marduk", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ishtar(AlienPower):
    """Ishtar - War and love goddess. +5 offense, -2 defense."""
    name: str = field(default="Ishtar", init=False)
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
class Enlil(AlienPower):
    """Enlil - Storm god. Random +0-8."""
    name: str = field(default="Enlil", init=False)
    description: str = field(default="Random +0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 8)
        return total


@dataclass
class Enki(AlienPower):
    """Enki - Water god. +4 defending."""
    name: str = field(default="Enki", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Shamash(AlienPower):
    """Shamash - Sun god. +4 first encounter."""
    name: str = field(default="Shamash", init=False)
    description: str = field(default="+4 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Nergal(AlienPower):
    """Nergal - Death god. +6 attacking."""
    name: str = field(default="Nergal", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Ereshkigal(AlienPower):
    """Ereshkigal - Underworld queen. Ships go home."""
    name: str = field(default="Ereshkigal", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anu(AlienPower):
    """Anu - Sky father. +2 per home colony."""
    name: str = field(default="Anu", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sin_Moon(AlienPower):
    """Sin_Moon - Moon god. See opponent card."""
    name: str = field(default="Sin_Moon", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nabu(AlienPower):
    """Nabu - Wisdom god. +1 per card."""
    name: str = field(default="Nabu", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Tiamat(AlienPower):
    """Tiamat - Chaos dragon. +6 but lose ship."""
    name: str = field(default="Tiamat", init=False)
    description: str = field(default="+6 but lose a ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Gilgamesh(AlienPower):
    """Gilgamesh - Hero king. +4 always."""
    name: str = field(default="Gilgamesh", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Enkidu(AlienPower):
    """Enkidu - Wild man. +3 defending home."""
    name: str = field(default="Enkidu", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ninurta(AlienPower):
    """Ninurta - War god. Win ties."""
    name: str = field(default="Ninurta", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Utnapishtim(AlienPower):
    """Utnapishtim - Flood survivor. Retrieve 3 ships."""
    name: str = field(default="Utnapishtim", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
MESOPOTAMIAN_POWERS = [
    Marduk, Ishtar, Enlil, Enki, Shamash, Nergal, Ereshkigal,
    Anu, Sin_Moon, Nabu, Tiamat, Gilgamesh, Enkidu, Ninurta, Utnapishtim,
]

for power_class in MESOPOTAMIAN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
