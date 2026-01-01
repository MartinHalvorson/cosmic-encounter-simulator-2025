"""
Candy and confectionery themed alien powers for Cosmic Encounter.
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
class Chocolate(AlienPower):
    """Chocolate - Power of Sweetness. Rich and decadent."""
    name: str = field(default="Chocolate", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Lollipop(AlienPower):
    """Lollipop - Power of the Stick. Long lasting flavor."""
    name: str = field(default="Lollipop", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Gummy(AlienPower):
    """Gummy - Power of Chewiness. Soft and stretchy."""
    name: str = field(default="Gummy", init=False)
    description: str = field(default="+2 per ship.", init=False)
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
        return base_total + (ships * 2)


@dataclass
class Caramel(AlienPower):
    """Caramel - Power of Sticky. Golden sweetness."""
    name: str = field(default="Caramel", init=False)
    description: str = field(default="+3 as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Licorice(AlienPower):
    """Licorice - Power of Black. Strong and divisive."""
    name: str = field(default="Licorice", init=False)
    description: str = field(default="Random +0-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(0, 6)
        return base_total


@dataclass
class Marshmallow(AlienPower):
    """Marshmallow - Power of Fluff. Soft and puffy."""
    name: str = field(default="Marshmallow", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                allies = sum(1 for p in game.offense_ships if p != player.name and game.offense_ships.get(p, 0) > 0)
            else:
                allies = sum(1 for p in game.defense_ships if p != player.name and game.defense_ships.get(p, 0) > 0)
            return base_total + (allies * 2)
        return base_total


@dataclass
class Toffee(AlienPower):
    """Toffee - Power of Crunch. Hard and buttery."""
    name: str = field(default="Toffee", init=False)
    description: str = field(default="+4 as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Nougat(AlienPower):
    """Nougat - Power of Filling. Sweet and chewy."""
    name: str = field(default="Nougat", init=False)
    description: str = field(default="+3 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                has_allies = any(p != player.name and game.offense_ships.get(p, 0) > 0 for p in game.offense_ships)
            else:
                has_allies = any(p != player.name and game.defense_ships.get(p, 0) > 0 for p in game.defense_ships)
            if has_allies:
                return base_total + 3
        return base_total


@dataclass
class Mint(AlienPower):
    """Mint - Power of Fresh. Cool and refreshing."""
    name: str = field(default="Mint_Candy", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class JellyBean(AlienPower):
    """JellyBean - Power of Variety. Many flavors."""
    name: str = field(default="Jelly_Bean", init=False)
    description: str = field(default="Random +1-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 5)
        return base_total


@dataclass
class Truffle(AlienPower):
    """Truffle - Power of Luxury. Premium chocolate."""
    name: str = field(default="Truffle", init=False)
    description: str = field(default="+5 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Fudge(AlienPower):
    """Fudge - Power of Rich. Dense and creamy."""
    name: str = field(default="Fudge", init=False)
    description: str = field(default="+3 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 3
        return base_total


@dataclass
class Taffy(AlienPower):
    """Taffy - Power of Pull. Stretched and twisted."""
    name: str = field(default="Taffy", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(player.hand)
        return base_total


@dataclass
class Praline(AlienPower):
    """Praline - Power of Nuts. Sugary and nutty."""
    name: str = field(default="Praline", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + (home_colonies * 2)
        return base_total


@dataclass
class Marzipan(AlienPower):
    """Marzipan - Power of Almonds. Sweet almond paste."""
    name: str = field(default="Marzipan", init=False)
    description: str = field(default="+3 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 3
        return base_total


# Register all candy powers
AlienRegistry.register(Chocolate())
AlienRegistry.register(Lollipop())
AlienRegistry.register(Gummy())
AlienRegistry.register(Caramel())
AlienRegistry.register(Licorice())
AlienRegistry.register(Marshmallow())
AlienRegistry.register(Toffee())
AlienRegistry.register(Nougat())
AlienRegistry.register(Mint())
AlienRegistry.register(JellyBean())
AlienRegistry.register(Truffle())
AlienRegistry.register(Fudge())
AlienRegistry.register(Taffy())
AlienRegistry.register(Praline())
AlienRegistry.register(Marzipan())
