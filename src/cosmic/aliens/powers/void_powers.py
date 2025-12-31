"""
Void Powers - Aliens with emptiness and darkness abilities.
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
class Abyss(AlienPower):
    """
    Abyss - Deep Darkness.
    Ships lost permanently.
    """
    name: str = field(default="Abyss", init=False)
    description: str = field(default="Permanent loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Blackhole(AlienPower):
    """
    Blackhole - Consume All.
    Take all cards from loser.
    """
    name: str = field(default="Blackhole", init=False)
    description: str = field(default="Take loser cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Darkness(AlienPower):
    """
    Darkness - Block Light.
    Hide all information.
    """
    name: str = field(default="Darkness", init=False)
    description: str = field(default="Hide all info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Empty(AlienPower):
    """
    Empty - Nothing There.
    Win with zero.
    """
    name: str = field(default="Empty", init=False)
    description: str = field(default="Win with zero.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Erasure(AlienPower):
    """
    Erasure - Delete Memory.
    Cancel opponent power.
    """
    name: str = field(default="Erasure", init=False)
    description: str = field(default="Cancel power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hollow(AlienPower):
    """
    Hollow - Empty Inside.
    No card played.
    """
    name: str = field(default="Hollow", init=False)
    description: str = field(default="No card play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Nihilist(AlienPower):
    """
    Nihilist - Nothing Matters.
    Nullify all bonuses.
    """
    name: str = field(default="Nihilist", init=False)
    description: str = field(default="Nullify bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Null(AlienPower):
    """
    Null - No Value.
    Cards worth zero.
    """
    name: str = field(default="Null", init=False)
    description: str = field(default="Zero cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Oblivion(AlienPower):
    """
    Oblivion - Complete Forget.
    Remove card from game.
    """
    name: str = field(default="Oblivion", init=False)
    description: str = field(default="Remove card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Shade_Alt(AlienPower):
    """
    Shade_Alt - Dark Form.
    +2 in darkness.
    """
    name: str = field(default="Shade_Alt", init=False)
    description: str = field(default="+2 in dark.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shadow_Alt(AlienPower):
    """
    Shadow_Alt - Follow Behind.
    Copy ally's attack.
    """
    name: str = field(default="Shadow_Alt", init=False)
    description: str = field(default="Copy ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vacuum(AlienPower):
    """
    Vacuum - Suck In.
    Pull ships to encounter.
    """
    name: str = field(default="Vacuum", init=False)
    description: str = field(default="Pull ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Void_Alt(AlienPower):
    """
    Void_Alt - Pure Nothing.
    Negate encounter entirely.
    """
    name: str = field(default="Void_Alt", init=False)
    description: str = field(default="Negate encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Zero(AlienPower):
    """
    Zero - Start Fresh.
    Reset totals to zero.
    """
    name: str = field(default="Zero", init=False)
    description: str = field(default="Reset totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Abyss())
AlienRegistry.register(Blackhole())
AlienRegistry.register(Darkness())
AlienRegistry.register(Empty())
AlienRegistry.register(Erasure())
AlienRegistry.register(Hollow())
AlienRegistry.register(Nihilist())
AlienRegistry.register(Null())
AlienRegistry.register(Oblivion())
AlienRegistry.register(Shade_Alt())
AlienRegistry.register(Shadow_Alt())
AlienRegistry.register(Vacuum())
AlienRegistry.register(Void_Alt())
AlienRegistry.register(Zero())
