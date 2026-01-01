"""
6000 Alien Milestone themed powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Milestone(AlienPower):
    """Milestone - Power of Achievement. Celebrating 6000 aliens."""
    name: str = field(default="Milestone_6000", init=False)
    description: str = field(default="+6 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 6
        return base_total


@dataclass
class Celebrant(AlienPower):
    """Celebrant - Power of Celebration. Party time."""
    name: str = field(default="Celebrant", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Triumphant(AlienPower):
    """Triumphant - Power of Victory. Winner's mentality."""
    name: str = field(default="Triumphant", init=False)
    description: str = field(default="+5 as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Legendary_6K(AlienPower):
    """Legendary_6K - Power of Legend. Mythic status."""
    name: str = field(default="Legendary_6K", init=False)
    description: str = field(default="+3 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                allies = sum(1 for p in game.offense_ships if p != player.name and game.offense_ships.get(p, 0) > 0)
            else:
                allies = sum(1 for p in game.defense_ships if p != player.name and game.defense_ships.get(p, 0) > 0)
            return base_total + (allies * 3)
        return base_total


@dataclass
class Epochal(AlienPower):
    """Epochal - Power of the Age. Marking a new era."""
    name: str = field(default="Epochal", init=False)
    description: str = field(default="+2 per ship (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + min(10, ships * 2)


@dataclass
class Monumental(AlienPower):
    """Monumental - Power of Monument. Standing tall."""
    name: str = field(default="Monumental", init=False)
    description: str = field(default="+5 as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Historic(AlienPower):
    """Historic - Power of History. Making history."""
    name: str = field(default="Historic", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Climactic(AlienPower):
    """Climactic - Power of Peak. Reaching the summit."""
    name: str = field(default="Climactic", init=False)
    description: str = field(default="Random +2-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(2, 6)
        return base_total


@dataclass
class Ultimate_6K(AlienPower):
    """Ultimate_6K - Power of Finality. The ultimate form."""
    name: str = field(default="Ultimate_6K", init=False)
    description: str = field(default="+6 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                has_allies = any(p != player.name and game.offense_ships.get(p, 0) > 0 for p in game.offense_ships)
            else:
                has_allies = any(p != player.name and game.defense_ships.get(p, 0) > 0 for p in game.defense_ships)
            if has_allies:
                return base_total + 6
        return base_total


@dataclass
class Transcendent(AlienPower):
    """Transcendent - Power of Beyond. Surpassing limits."""
    name: str = field(default="Transcendent", init=False)
    description: str = field(default="+3 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 3)
        return base_total


@dataclass
class Pinnacle(AlienPower):
    """Pinnacle - Power of Peak. At the very top."""
    name: str = field(default="Pinnacle", init=False)
    description: str = field(default="+4 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 4
        return base_total


@dataclass
class Apex(AlienPower):
    """Apex - Power of Apex. Top predator."""
    name: str = field(default="Apex", init=False)
    description: str = field(default="+4 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 4
        return base_total


@dataclass
class Superlative(AlienPower):
    """Superlative - Power of the Best. The greatest."""
    name: str = field(default="Superlative", init=False)
    description: str = field(default="+2 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (len(player.hand) * 2)
        return base_total


@dataclass
class Consummate(AlienPower):
    """Consummate - Power of Perfection. Skill mastery."""
    name: str = field(default="Consummate", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Paragon(AlienPower):
    """Paragon - Power of Example. The model of excellence."""
    name: str = field(default="Paragon", init=False)
    description: str = field(default="+5 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Quintessential(AlienPower):
    """Quintessential - Power of the Essence. Pure form."""
    name: str = field(default="Quintessential", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + (home_colonies * 2)
        return base_total


# Register all milestone 6000 powers
AlienRegistry.register(Milestone())
AlienRegistry.register(Celebrant())
AlienRegistry.register(Triumphant())
AlienRegistry.register(Legendary_6K())
AlienRegistry.register(Epochal())
AlienRegistry.register(Monumental())
AlienRegistry.register(Historic())
AlienRegistry.register(Climactic())
AlienRegistry.register(Ultimate_6K())
AlienRegistry.register(Transcendent())
AlienRegistry.register(Pinnacle())
AlienRegistry.register(Apex())
AlienRegistry.register(Superlative())
AlienRegistry.register(Consummate())
AlienRegistry.register(Paragon())
AlienRegistry.register(Quintessential())
