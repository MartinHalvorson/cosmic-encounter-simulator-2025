"""
Soda and soft drink themed alien powers for Cosmic Encounter.
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
class Cola(AlienPower):
    """Cola - Power of Refreshment. Classic taste."""
    name: str = field(default="Cola", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class RootBeer(AlienPower):
    """RootBeer - Power of Foam. Creamy and sweet."""
    name: str = field(default="Root_Beer", init=False)
    description: str = field(default="+4 as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class GingerAle(AlienPower):
    """GingerAle - Power of Spice. Mild and gingery."""
    name: str = field(default="Ginger_Ale", init=False)
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
class LemonLime(AlienPower):
    """LemonLime - Power of Citrus. Tangy and bright."""
    name: str = field(default="Lemon_Lime", init=False)
    description: str = field(default="+3 as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class OrangeSoda(AlienPower):
    """OrangeSoda - Power of Citrus Burst. Sweet and fruity."""
    name: str = field(default="Orange_Soda", init=False)
    description: str = field(default="+2 per ship (max +8).", init=False)
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
        return base_total + min(8, ships * 2)


@dataclass
class GrapeSoda(AlienPower):
    """GrapeSoda - Power of Purple. Sweet grape flavor."""
    name: str = field(default="Grape_Soda", init=False)
    description: str = field(default="Random +1-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 5)
        return base_total


@dataclass
class CreamSoda(AlienPower):
    """CreamSoda - Power of Sweetness. Vanilla cream."""
    name: str = field(default="Cream_Soda", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Ginger_Beer(AlienPower):
    """Ginger_Beer - Power of Kick. Strong ginger taste."""
    name: str = field(default="Ginger_Beer", init=False)
    description: str = field(default="+3 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 3
        return base_total


@dataclass
class Tonic(AlienPower):
    """Tonic - Power of Quinine. Bitter and bubbly."""
    name: str = field(default="Tonic", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, game.current_turn)
        return base_total


@dataclass
class Seltzer(AlienPower):
    """Seltzer - Power of Bubbles. Pure carbonation."""
    name: str = field(default="Seltzer", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Energy_Drink(AlienPower):
    """Energy_Drink - Power of Caffeine. Extreme energy."""
    name: str = field(default="Energy_Drink", init=False)
    description: str = field(default="+5 as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Sparkling_Water(AlienPower):
    """Sparkling_Water - Power of Fizz. Light and refreshing."""
    name: str = field(default="Sparkling_Water", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(player.hand)
        return base_total


@dataclass
class Dr_Pepper(AlienPower):
    """Dr_Pepper - Power of 23 Flavors. Unique taste."""
    name: str = field(default="Dr_Pepper", init=False)
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
class Mountain_Dew(AlienPower):
    """Mountain_Dew - Power of Extreme. Citrus caffeine."""
    name: str = field(default="Mountain_Dew", init=False)
    description: str = field(default="+4 with 4+ ships.", init=False)
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
        if ships >= 4:
            return base_total + 4
        return base_total


@dataclass
class Sprite(AlienPower):
    """Sprite - Power of Lemon. Clear and crisp."""
    name: str = field(default="Sprite", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


# Register all soda powers
AlienRegistry.register(Cola())
AlienRegistry.register(RootBeer())
AlienRegistry.register(GingerAle())
AlienRegistry.register(LemonLime())
AlienRegistry.register(OrangeSoda())
AlienRegistry.register(GrapeSoda())
AlienRegistry.register(CreamSoda())
AlienRegistry.register(Ginger_Beer())
AlienRegistry.register(Tonic())
AlienRegistry.register(Seltzer())
AlienRegistry.register(Energy_Drink())
AlienRegistry.register(Sparkling_Water())
AlienRegistry.register(Dr_Pepper())
AlienRegistry.register(Mountain_Dew())
AlienRegistry.register(Sprite())
