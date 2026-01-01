"""
Milestone 4000 alien powers - celebrating 4000 aliens!
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
class FourThousand(AlienPower):
    """FourThousand - Power of Scale. +4 in encounters."""
    name: str = field(default="FourThousand", init=False)
    description: str = field(default="+4 (celebrating 4000 aliens!).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Grand_Milestone(AlienPower):
    """Grand_Milestone - Power of Achievement. +8 bonus."""
    name: str = field(default="Grand_Milestone", init=False)
    description: str = field(default="+8 bonus (4000 milestone!).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 8
        return total


@dataclass
class Ultimate_Scale(AlienPower):
    """Ultimate_Scale - Power of Magnitude. Ships count as 2 each."""
    name: str = field(default="Ultimate_Scale", init=False)
    description: str = field(default="Ships count as 2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cosmic_Heritage(AlienPower):
    """Cosmic_Heritage - Power of History. +2 per turn game has lasted."""
    name: str = field(default="Cosmic_Heritage", init=False)
    description: str = field(default="+2 per game turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (game.current_turn * 2)
        return total


@dataclass
class Supreme_Champion(AlienPower):
    """Supreme_Champion - Power of Victory. +6 at 4 colonies."""
    name: str = field(default="Supreme_Champion", init=False)
    description: str = field(default="+6 at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return total + 6
        return total


@dataclass
class Infinite_Cosmos(AlienPower):
    """Infinite_Cosmos - Power of Universe. +4 always."""
    name: str = field(default="Infinite_Cosmos", init=False)
    description: str = field(default="+4 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Cosmic_Colossus(AlienPower):
    """Cosmic_Colossus - Power of Giants. May commit up to 8 ships."""
    name: str = field(default="Cosmic_Colossus", init=False)
    description: str = field(default="Commit up to 8 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Galaxy_Collector(AlienPower):
    """Galaxy_Collector - Power of Gathering. Draw 3 cards when winning."""
    name: str = field(default="Galaxy_Collector", init=False)
    description: str = field(default="Draw 3 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Perpetual_Champion(AlienPower):
    """Perpetual_Champion - Power of Persistence. Return 4 ships from warp."""
    name: str = field(default="Perpetual_Champion", init=False)
    description: str = field(default="Return 4 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mythic_One(AlienPower):
    """Mythic_One - Power of Legend. Win all ties and +2."""
    name: str = field(default="Mythic_One", init=False)
    description: str = field(default="Win ties, +2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


# Register all milestone 4000 powers
AlienRegistry.register(FourThousand())
AlienRegistry.register(Grand_Milestone())
AlienRegistry.register(Ultimate_Scale())
AlienRegistry.register(Cosmic_Heritage())
AlienRegistry.register(Supreme_Champion())
AlienRegistry.register(Infinite_Cosmos())
AlienRegistry.register(Cosmic_Colossus())
AlienRegistry.register(Galaxy_Collector())
AlienRegistry.register(Perpetual_Champion())
AlienRegistry.register(Mythic_One())
