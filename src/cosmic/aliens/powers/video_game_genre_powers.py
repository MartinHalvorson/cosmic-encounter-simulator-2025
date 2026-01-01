"""
Video Game Genre Powers - Gaming genre themed aliens.
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
class RPG_Game(AlienPower):
    """RPG_Game - Role playing growth."""
    name: str = field(default="RPG_Game", init=False)
    description: str = field(default="+1 per turn (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(7, game.current_turn)
        return total


@dataclass
class FPS_Game(AlienPower):
    """FPS_Game - First person action."""
    name: str = field(default="FPS_Game", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Strategy_Game(AlienPower):
    """Strategy_Game - Tactical planning."""
    name: str = field(default="Strategy_Game", init=False)
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
class Platformer_Game(AlienPower):
    """Platformer_Game - Jump and run."""
    name: str = field(default="Platformer_Game", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Puzzle_Game(AlienPower):
    """Puzzle_Game - Mind bending."""
    name: str = field(default="Puzzle_Game", init=False)
    description: str = field(default="+1 per card (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(7, len(player.hand))
        return total


@dataclass
class Racing_Game(AlienPower):
    """Racing_Game - Speed thrill."""
    name: str = field(default="Racing_Game", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Survival_Game(AlienPower):
    """Survival_Game - Resource management."""
    name: str = field(default="Survival_Game", init=False)
    description: str = field(default="+5 with 3 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return total + 5
        return total


@dataclass
class Simulation_Game(AlienPower):
    """Simulation_Game - Life builder."""
    name: str = field(default="Simulation_Game", init=False)
    description: str = field(default="+5 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 5
        return total


@dataclass
class Fighting_Game(AlienPower):
    """Fighting_Game - Combo master."""
    name: str = field(default="Fighting_Game", init=False)
    description: str = field(default="+2 plus random +0-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + random.randint(0, 5)
        return total


@dataclass
class Horror_Game(AlienPower):
    """Horror_Game - Terrifying defense."""
    name: str = field(default="Horror_Game", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Sandbox_Game(AlienPower):
    """Sandbox_Game - Open world."""
    name: str = field(default="Sandbox_Game", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Roguelike_Game(AlienPower):
    """Roguelike_Game - Random challenge."""
    name: str = field(default="Roguelike_Game", init=False)
    description: str = field(default="+3 plus random +0-4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3 + random.randint(0, 4)
        return total


@dataclass
class MMORPG_Game(AlienPower):
    """MMORPG_Game - Massive multiplayer."""
    name: str = field(default="MMORPG_Game", init=False)
    description: str = field(default="+5 with allies.", init=False)
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
            return total + 5
        return total


@dataclass
class Stealth_Game(AlienPower):
    """Stealth_Game - Silent assassin."""
    name: str = field(default="Stealth_Game", init=False)
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
class Rhythm_Game(AlienPower):
    """Rhythm_Game - Beat master."""
    name: str = field(default="Rhythm_Game", init=False)
    description: str = field(default="+4 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 4
        return total


VIDEO_GAME_GENRE_POWERS = [
    RPG_Game, FPS_Game, Strategy_Game, Platformer_Game, Puzzle_Game,
    Racing_Game, Survival_Game, Simulation_Game, Fighting_Game, Horror_Game,
    Sandbox_Game, Roguelike_Game, MMORPG_Game, Stealth_Game, Rhythm_Game
]

for power_class in VIDEO_GAME_GENRE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
