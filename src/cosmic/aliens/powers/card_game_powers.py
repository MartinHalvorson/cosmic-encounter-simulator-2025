"""
Card Game Powers - Playing card themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Ace(AlienPower):
    """Ace - High Card. +6 always."""
    name: str = field(default="Ace", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class King_Card(AlienPower):
    """King_Card - Royal Card. +5 on defense."""
    name: str = field(default="King_Card", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Queen_Card(AlienPower):
    """Queen_Card - Royal Card. +5 on defense."""
    name: str = field(default="Queen_Card", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Jack_Card(AlienPower):
    """Jack_Card - Face Card. +4 on offense."""
    name: str = field(default="Jack_Card", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Joker_Card(AlienPower):
    """Joker_Card - Wild Card. Random +1 to +7."""
    name: str = field(default="Joker_Card", init=False)
    description: str = field(default="Random +1 to +7.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 7)
        return total


@dataclass
class Spade(AlienPower):
    """Spade - Black Suit. +4 on offense."""
    name: str = field(default="Spade", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Heart_Card(AlienPower):
    """Heart_Card - Red Suit. +2 per ally."""
    name: str = field(default="Heart_Card", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Club(AlienPower):
    """Club - Black Suit. +4 on defense."""
    name: str = field(default="Club", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Diamond_Card(AlienPower):
    """Diamond_Card - Red Suit. Extra card draw."""
    name: str = field(default="Diamond_Card", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dealer(AlienPower):
    """Dealer - Card Giver. Extra card draw."""
    name: str = field(default="Dealer", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shuffle(AlienPower):
    """Shuffle - Mix Cards. Random +1 to +5."""
    name: str = field(default="Shuffle", init=False)
    description: str = field(default="Random +1 to +5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 5)
        return total


@dataclass
class Poker_Face(AlienPower):
    """Poker_Face - Hidden Intent. See opponent card."""
    name: str = field(default="Poker_Face", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Full_House(AlienPower):
    """Full_House - Strong Hand. +5 always."""
    name: str = field(default="Full_House", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Royal_Flush(AlienPower):
    """Royal_Flush - Best Hand. +6 always."""
    name: str = field(default="Royal_Flush", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Bluff(AlienPower):
    """Bluff - Fake Out. Random +/- 4."""
    name: str = field(default="Bluff", init=False)
    description: str = field(default="Random -4 to +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return max(0, total + random.randint(-4, 4))
        return total


# Register all powers
CARD_GAME_POWERS = [
    Ace, King_Card, Queen_Card, Jack_Card, Joker_Card, Spade, Heart_Card,
    Club, Diamond_Card, Dealer, Shuffle, Poker_Face, Full_House, Royal_Flush, Bluff,
]

for power_class in CARD_GAME_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
