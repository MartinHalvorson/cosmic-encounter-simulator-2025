"""
Achievement themed alien powers - 6000 milestone!
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
class Celebrant(AlienPower):
    """Celebrant - Power of Celebration. Mark the milestone."""
    name: str = field(default="Celebrant", init=False)
    description: str = field(default="+6 constant for 6000!", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Milestone_Master(AlienPower):
    """Milestone_Master - Power of Achievement. Reach new heights."""
    name: str = field(default="Milestone_Master", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Apex(AlienPower):
    """Apex - Power of Peak. At the top."""
    name: str = field(default="Apex", init=False)
    description: str = field(default="+5 with 4+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return total + 5
        return total


@dataclass
class Summit_Achievement(AlienPower):
    """Summit_Achievement - Power of Heights. Highest point."""
    name: str = field(default="Summit_Achievement", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Pinnacle(AlienPower):
    """Pinnacle - Power of Excellence. Best of the best."""
    name: str = field(default="Pinnacle", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Zenith_Achievement(AlienPower):
    """Zenith_Achievement - Power of Climax. Highest achievement."""
    name: str = field(default="Zenith_Achievement", init=False)
    description: str = field(default="+6 with 6+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 6:
            return total + 6
        return total


@dataclass
class Crowning(AlienPower):
    """Crowning - Power of Victory. Final triumph."""
    name: str = field(default="Crowning", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Triumph_Achievement(AlienPower):
    """Triumph_Achievement - Power of Success. Total victory."""
    name: str = field(default="Triumph_Achievement", init=False)
    description: str = field(default="+4 with allies.", init=False)
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
            return total + 4
        return total


@dataclass
class Glory_Achievement(AlienPower):
    """Glory_Achievement - Power of Fame. Legendary status."""
    name: str = field(default="Glory_Achievement", init=False)
    description: str = field(default="+2 per ally (max +8).", init=False)
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
        return total + min(8, ally_count * 2)


@dataclass
class Accolade(AlienPower):
    """Accolade - Power of Honor. Recognized achievement."""
    name: str = field(default="Accolade", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Laureate(AlienPower):
    """Laureate - Power of Award. Crowned winner."""
    name: str = field(default="Laureate", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Elite_Achievement(AlienPower):
    """Elite_Achievement - Power of Excellence. Top tier."""
    name: str = field(default="Elite_Achievement", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, game.current_turn)
        return total


@dataclass
class Paragon(AlienPower):
    """Paragon - Power of Model. Perfect example."""
    name: str = field(default="Paragon", init=False)
    description: str = field(default="+4 with 4+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 4:
            return total + 4
        return total


@dataclass
class Virtuoso_Achievement(AlienPower):
    """Virtuoso_Achievement - Power of Mastery. Expert skill."""
    name: str = field(default="Virtuoso_Achievement", init=False)
    description: str = field(default="+3 plus random +0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3 + random.randint(0, 3)
        return total


@dataclass
class Exemplar(AlienPower):
    """Exemplar - Power of Example. Model of excellence."""
    name: str = field(default="Exemplar", init=False)
    description: str = field(default="+4 when alone.", init=False)
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
            return total + 4
        return total


@dataclass
class Sage_6K(AlienPower):
    """Sage_6K - Power of Wisdom. Ancient knowledge."""
    name: str = field(default="Sage_6K", init=False)
    description: str = field(default="+2 per colony (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + min(8, colonies * 2)
        return total


@dataclass
class Luminary(AlienPower):
    """Luminary - Power of Light. Guiding star."""
    name: str = field(default="Luminary", init=False)
    description: str = field(default="+5 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return total + 5
        return total


@dataclass
class Magistrate(AlienPower):
    """Magistrate - Power of Authority. Rule wisely."""
    name: str = field(default="Magistrate", init=False)
    description: str = field(default="+2 per ship (max +10).", init=False)
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
        return total + min(10, ships * 2)


ACHIEVEMENT_POWERS = [
    Celebrant, Milestone_Master, Apex, Summit_Achievement, Pinnacle,
    Zenith_Achievement, Crowning, Triumph_Achievement, Glory_Achievement,
    Accolade, Laureate, Elite_Achievement, Paragon, Virtuoso_Achievement,
    Exemplar, Sage_6K, Luminary, Magistrate
]

for power_class in ACHIEVEMENT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
