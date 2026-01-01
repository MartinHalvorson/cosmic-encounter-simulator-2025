"""
Elemental Powers - Aliens with primal elemental control.
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
class Blaze(AlienPower):
    """
    Blaze - Fire Starter.
    When you win, opponent's highest attack card is discarded.
    """
    name: str = field(default="Blaze", init=False)
    description: str = field(default="Discard opponent's best card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Breeze(AlienPower):
    """
    Breeze - Wind Spirit.
    Ships from warp can go to any colony, not just home.
    """
    name: str = field(default="Breeze", init=False)
    description: str = field(default="Warp ships to any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cinder(AlienPower):
    """
    Cinder - Ember Spirit.
    When attacking, add +1 for each ship in warp.
    """
    name: str = field(default="Cinder", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Current(AlienPower):
    """
    Current - Water Flow.
    Move ships to adjacent planets after encounters.
    """
    name: str = field(default="Current", init=False)
    description: str = field(default="Move ships after encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dust(AlienPower):
    """
    Dust - Particle Cloud.
    When defending, opponent must reveal encounter card first.
    """
    name: str = field(default="Dust", init=False)
    description: str = field(default="Attacker reveals first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ember(AlienPower):
    """
    Ember - Hot Coal.
    When you lose, 1 opponent ship is also lost.
    """
    name: str = field(default="Ember", init=False)
    description: str = field(default="Take 1 ship with you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frost(AlienPower):
    """
    Frost - Cold Touch.
    Freeze opponent's power for one encounter.
    """
    name: str = field(default="Frost", init=False)
    description: str = field(default="Freeze opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gale(AlienPower):
    """
    Gale - Strong Wind.
    Blow 2 opposing ally ships back to colonies.
    """
    name: str = field(default="Gale", init=False)
    description: str = field(default="Return 2 ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Glacier(AlienPower):
    """
    Glacier - Slow Power.
    Add +5 when defending.
    """
    name: str = field(default="Glacier", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when defending."""
        if side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Inferno(AlienPower):
    """
    Inferno - Raging Fire.
    When you win by 10+, remove all opponent ships from game.
    """
    name: str = field(default="Inferno", init=False)
    description: str = field(default="Big win removes ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Magma(AlienPower):
    """
    Magma - Molten Rock.
    Ships lost by opponent are removed from game.
    """
    name: str = field(default="Magma", init=False)
    description: str = field(default="Lost ships removed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mist(AlienPower):
    """
    Mist - Obscuring Fog.
    Allies cannot be invited against you.
    """
    name: str = field(default="Mist", init=False)
    description: str = field(default="Block ally invitations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quartz(AlienPower):
    """
    Quartz - Crystal Power.
    Your attack cards have +2 value.
    """
    name: str = field(default="Quartz", init=False)
    description: str = field(default="Attack cards +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 to total."""
        return total + 2


@dataclass
class Ripple(AlienPower):
    """
    Ripple - Water Wave.
    When you win, move 1 ship from colony to any planet.
    """
    name: str = field(default="Ripple", init=False)
    description: str = field(default="Move ship on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smoke(AlienPower):
    """
    Smoke - Concealment.
    Your ships committed are hidden until reveal.
    """
    name: str = field(default="Smoke", init=False)
    description: str = field(default="Hidden ship count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spark(AlienPower):
    """
    Spark - Quick Strike.
    Win ties when attacking.
    """
    name: str = field(default="Spark", init=False)
    description: str = field(default="Win ties as attacker.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Steam(AlienPower):
    """
    Steam - Hot Vapor.
    Escape attacks - ships return to colonies on loss.
    """
    name: str = field(default="Steam", init=False)
    description: str = field(default="Ships return on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stone(AlienPower):
    """
    Stone - Rock Solid.
    Cannot be zapped. Power always active.
    """
    name: str = field(default="Stone", init=False)
    description: str = field(default="Cannot be zapped.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thunder(AlienPower):
    """
    Thunder - Loud Boom.
    When you win, draw 2 cards.
    """
    name: str = field(default="Thunder", init=False)
    description: str = field(default="Draw 2 on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wave(AlienPower):
    """
    Wave - Ocean Power.
    Retrieve 2 ships from warp when you win.
    """
    name: str = field(default="Wave", init=False)
    description: str = field(default="Retrieve 2 ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Whirlwind(AlienPower):
    """
    Whirlwind - Spinning Wind.
    Randomize opponent's encounter card from their hand.
    """
    name: str = field(default="Whirlwind", init=False)
    description: str = field(default="Randomize opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Blaze())
AlienRegistry.register(Breeze())
AlienRegistry.register(Cinder())
AlienRegistry.register(Current())
AlienRegistry.register(Dust())
AlienRegistry.register(Ember())
AlienRegistry.register(Frost())
AlienRegistry.register(Gale())
AlienRegistry.register(Glacier())
AlienRegistry.register(Inferno())
AlienRegistry.register(Magma())
AlienRegistry.register(Mist())
AlienRegistry.register(Quartz())
AlienRegistry.register(Ripple())
AlienRegistry.register(Smoke())
AlienRegistry.register(Spark())
AlienRegistry.register(Steam())
AlienRegistry.register(Stone())
AlienRegistry.register(Thunder())
AlienRegistry.register(Wave())
AlienRegistry.register(Whirlwind())
