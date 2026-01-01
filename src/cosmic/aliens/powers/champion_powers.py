"""
Champion Powers - Aliens with combat and victory abilities.
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
class Ace(AlienPower):
    """
    Ace - Top Skill.
    +5 when alone.
    """
    name: str = field(default="Ace", init=False)
    description: str = field(default="+5 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Berserker(AlienPower):
    """
    Berserker - Rage Mode.
    +2 per ship lost.
    """
    name: str = field(default="Berserker", init=False)
    description: str = field(default="+2 per loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Champion_Alt(AlienPower):
    """
    Champion_Alt - Fight for Glory.
    Extra colony on victory.
    """
    name: str = field(default="Champion_Alt", init=False)
    description: str = field(default="Extra victory colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Duelist(AlienPower):
    """
    Duelist - One on One.
    Solo combat bonus.
    """
    name: str = field(default="Duelist", init=False)
    description: str = field(default="Solo bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fighter(AlienPower):
    """
    Fighter - Combat Expert.
    +3 in combat.
    """
    name: str = field(default="Fighter", init=False)
    description: str = field(default="+3 combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 in combat."""
        return total + 3


@dataclass
class Gladiator(AlienPower):
    """
    Gladiator - Arena Combat.
    Win ties always.
    """
    name: str = field(default="Gladiator", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hero(AlienPower):
    """
    Hero - Save the Day.
    Rescue ally ships.
    """
    name: str = field(default="Hero", init=False)
    description: str = field(default="Rescue ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Knight(AlienPower):
    """
    Knight - Noble Combat.
    +2 when defending ally.
    """
    name: str = field(default="Knight", init=False)
    description: str = field(default="+2 defend ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Legend(AlienPower):
    """
    Legend - Famous Fighter.
    +4 on reputation.
    """
    name: str = field(default="Legend", init=False)
    description: str = field(default="+4 fame.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Prodigy(AlienPower):
    """
    Prodigy - Natural Talent.
    Double first ship value.
    """
    name: str = field(default="Prodigy", init=False)
    description: str = field(default="Double first ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spartan(AlienPower):
    """
    Spartan - Disciplined.
    Never lose to larger force.
    """
    name: str = field(default="Spartan", init=False)
    description: str = field(default="Beat larger force.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Titan(AlienPower):
    """
    Titan - Giant Strength.
    Ships count as 2.
    """
    name: str = field(default="Titan", init=False)
    description: str = field(default="Ships count x2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Veteran(AlienPower):
    """
    Veteran - Battle Experience.
    +1 per encounter won.
    """
    name: str = field(default="Veteran", init=False)
    description: str = field(default="+1 per win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Victor(AlienPower):
    """
    Victor - Always Win.
    +2 per colony.
    """
    name: str = field(default="Victor", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warrior_Alt(AlienPower):
    """
    Warrior_Alt - Born Fighter.
    +4 attacking.
    """
    name: str = field(default="Warrior_Alt", init=False)
    description: str = field(default="+4 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking."""
        if side == Side.OFFENSE:
            return total + 4
        return total


# Register all powers
AlienRegistry.register(Ace())
AlienRegistry.register(Berserker())
AlienRegistry.register(Champion_Alt())
AlienRegistry.register(Duelist())
AlienRegistry.register(Fighter())
AlienRegistry.register(Gladiator())
AlienRegistry.register(Hero())
AlienRegistry.register(Knight())
AlienRegistry.register(Legend())
AlienRegistry.register(Prodigy())
AlienRegistry.register(Spartan())
AlienRegistry.register(Titan())
AlienRegistry.register(Veteran())
AlienRegistry.register(Victor())
AlienRegistry.register(Warrior_Alt())
