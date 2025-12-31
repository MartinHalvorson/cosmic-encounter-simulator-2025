"""
Season and Time-themed alien powers.
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
class Spring_Season(AlienPower):
    """Spring - Power of Renewal. +2 per ship returned from warp this turn."""
    name: str = field(default="Spring_Season", init=False)
    description: str = field(default="+2 per ship returned from warp this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Summer_Season(AlienPower):
    """Summer - Power of Heat. +4 on your turn."""
    name: str = field(default="Summer_Season", init=False)
    description: str = field(default="+4 when on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Autumn_Season(AlienPower):
    """Autumn - Power of Harvest. Draw 1 card when winning."""
    name: str = field(default="Autumn_Season", init=False)
    description: str = field(default="Draw 1 card when you win an encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Winter_Season(AlienPower):
    """Winter - Power of Cold. +4 when defending."""
    name: str = field(default="Winter_Season", init=False)
    description: str = field(default="+4 when on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Dawn_Season(AlienPower):
    """Dawn - Power of Beginning. +5 on first encounter of your turn."""
    name: str = field(default="Dawn_Season", init=False)
    description: str = field(default="+5 on first encounter of your turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dusk_Season(AlienPower):
    """Dusk - Power of Ending. +5 on second encounter of your turn."""
    name: str = field(default="Dusk_Season", init=False)
    description: str = field(default="+5 on second encounter of your turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Midnight_Season(AlienPower):
    """Midnight - Power of Darkness. Cards played against you are -2."""
    name: str = field(default="Midnight_Season", init=False)
    description: str = field(default="Opponent's attack cards are -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Noon_Season(AlienPower):
    """Noon - Power of Light. Your attack cards are +2."""
    name: str = field(default="Noon_Season", init=False)
    description: str = field(default="Your attack cards are +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Century_Season(AlienPower):
    """Century - Power of Ages. +1 for each turn the game has lasted."""
    name: str = field(default="Century_Season", init=False)
    description: str = field(default="+1 for each turn the game has lasted.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


@dataclass
class Decade_Season(AlienPower):
    """Decade - Power of Growth. +2 for each foreign colony you have."""
    name: str = field(default="Decade_Season", init=False)
    description: str = field(default="+2 for each foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + (colonies * 2)
        return total


@dataclass
class Era_Season(AlienPower):
    """Era - Power of Epochs. +3 per home planet you still control."""
    name: str = field(default="Era_Season", init=False)
    description: str = field(default="+3 per home planet you control.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return total + (home_count * 3)
        return total


@dataclass
class Moment_Season(AlienPower):
    """Moment - Power of Now. +6 if game is on turn 1-3."""
    name: str = field(default="Moment_Season", init=False)
    description: str = field(default="+6 during early game (turns 1-3).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 3:
            return total + 6
        return total


@dataclass
class Eternity_Season(AlienPower):
    """Eternity - Power of Forever. Ships never go to warp."""
    name: str = field(default="Eternity_Season", init=False)
    description: str = field(default="Your ships never go to the warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Yesterday_Season(AlienPower):
    """Yesterday - Power of Past. Draw from discard instead of deck."""
    name: str = field(default="Yesterday_Season", init=False)
    description: str = field(default="Draw from discard pile instead of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tomorrow_Season(AlienPower):
    """Tomorrow - Power of Future. See opponent's card before playing."""
    name: str = field(default="Tomorrow_Season", init=False)
    description: str = field(default="Opponent must reveal card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all season powers
AlienRegistry.register(Spring_Season())
AlienRegistry.register(Summer_Season())
AlienRegistry.register(Autumn_Season())
AlienRegistry.register(Winter_Season())
AlienRegistry.register(Dawn_Season())
AlienRegistry.register(Dusk_Season())
AlienRegistry.register(Midnight_Season())
AlienRegistry.register(Noon_Season())
AlienRegistry.register(Century_Season())
AlienRegistry.register(Decade_Season())
AlienRegistry.register(Era_Season())
AlienRegistry.register(Moment_Season())
AlienRegistry.register(Eternity_Season())
AlienRegistry.register(Yesterday_Season())
AlienRegistry.register(Tomorrow_Season())
