"""
School sport themed alien powers.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Dodgeball(AlienPower):
    """Dodgeball - Power of Evasion. Avoid the hit."""
    name: str = field(default="Dodgeball", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Kickball(AlienPower):
    """Kickball - Power of Impact. Strong kick."""
    name: str = field(default="Kickball", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Tug_Of_War(AlienPower):
    """Tug_Of_War - Power of Pulling. Team strength."""
    name: str = field(default="Tug_Of_War", init=False)
    description: str = field(default="+2 per ship (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return total + min(8, ships * 2)


@dataclass
class Relay_Race(AlienPower):
    """Relay_Race - Power of Passing. Teamwork."""
    name: str = field(default="Relay_Race", init=False)
    description: str = field(default="+2 per ally (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        return total + min(6, ally_count * 2)


@dataclass
class Long_Jump(AlienPower):
    """Long_Jump - Power of Leaping. Great distance."""
    name: str = field(default="Long_Jump", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class High_Jump(AlienPower):
    """High_Jump - Power of Height. Rise above."""
    name: str = field(default="High_Jump", init=False)
    description: str = field(default="+4 with 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 4
        return total


@dataclass
class Sprint(AlienPower):
    """Sprint - Power of Speed. Fast burst."""
    name: str = field(default="Sprint", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Shot_Put(AlienPower):
    """Shot_Put - Power of Throwing. Heavy launch."""
    name: str = field(default="Shot_Put", init=False)
    description: str = field(default="+5 with 3 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return total + 5
        return total


@dataclass
class Hurdles(AlienPower):
    """Hurdles - Power of Jumping. Overcome obstacles."""
    name: str = field(default="Hurdles", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Cross_Country(AlienPower):
    """Cross_Country - Power of Endurance. Long distance."""
    name: str = field(default="Cross_Country", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, game.current_turn)
        return total


@dataclass
class Softball(AlienPower):
    """Softball - Power of Batting. Hit the ball."""
    name: str = field(default="Softball", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Wrestling(AlienPower):
    """Wrestling - Power of Grappling. Direct combat."""
    name: str = field(default="Wrestling", init=False)
    description: str = field(default="+5 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 5
        return total


@dataclass
class Gymnastics(AlienPower):
    """Gymnastics - Power of Flexibility. Acrobatic moves."""
    name: str = field(default="Gymnastics", init=False)
    description: str = field(default="+2 plus random +0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + random.randint(0, 3)
        return total


@dataclass
class Field_Hockey(AlienPower):
    """Field_Hockey - Power of Sticks. Ground game."""
    name: str = field(default="Field_Hockey", init=False)
    description: str = field(default="+3 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count > 0:
            return total + 3
        return total


@dataclass
class Track(AlienPower):
    """Track - Power of Running. Speed on track."""
    name: str = field(default="Track", init=False)
    description: str = field(default="+4 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return total + 4
        return total


SCHOOL_SPORT_POWERS = [
    Dodgeball, Kickball, Tug_Of_War, Relay_Race, Long_Jump, High_Jump,
    Sprint, Shot_Put, Hurdles, Cross_Country, Softball, Wrestling,
    Gymnastics, Field_Hockey, Track
]

for power_class in SCHOOL_SPORT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
