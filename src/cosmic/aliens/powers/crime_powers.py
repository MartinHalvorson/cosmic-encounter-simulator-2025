"""
Crime Powers for Cosmic Encounter.

Aliens inspired by criminal activities and law enforcement.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Thief(AlienPower):
    """
    Thief - Power to Steal.
    After winning, take 1 random card from the loser's hand.
    """
    name: str = field(default="Thief", init=False)
    description: str = field(
        default="Take 1 card from loser after winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pirate(AlienPower):
    """
    Pirate - Power to Plunder.
    +3 when attacking foreign planets.
    """
    name: str = field(default="Pirate", init=False)
    description: str = field(
        default="+3 attacking foreign planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Burglar(AlienPower):
    """
    Burglar - Power to Break In.
    You may establish a colony with only 1 ship.
    """
    name: str = field(default="Burglar", init=False)
    description: str = field(
        default="Colony with just 1 ship.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smuggler(AlienPower):
    """
    Smuggler - Power to Move.
    Move 2 ships between colonies after each encounter.
    """
    name: str = field(default="Smuggler", init=False)
    description: str = field(
        default="Move 2 ships after encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Assassin(AlienPower):
    """
    Assassin - Power to Eliminate.
    Remove 1 ship from play when you win by 10+.
    """
    name: str = field(default="Assassin", init=False)
    description: str = field(
        default="Remove 1 ship when winning by 10+.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Detective(AlienPower):
    """
    Detective - Power to Investigate.
    Look at any player's hand at start of each encounter.
    """
    name: str = field(default="Detective", init=False)
    description: str = field(
        default="View one hand each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sheriff(AlienPower):
    """
    Sheriff - Power of Law.
    +4 when defending your home planets.
    """
    name: str = field(default="Sheriff", init=False)
    description: str = field(
        default="+4 defending home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bounty(AlienPower):
    """
    Bounty - Power to Hunt.
    +3 against the player with most colonies.
    """
    name: str = field(default="Bounty", init=False)
    description: str = field(
        default="+3 vs player with most colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hacker(AlienPower):
    """
    Hacker - Power to Breach.
    Once per encounter, reveal an opponent's face-down card.
    """
    name: str = field(default="Hacker", init=False)
    description: str = field(
        default="Reveal opponent's card once.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mastermind(AlienPower):
    """
    Mastermind - Power to Plan.
    Look at top 3 cards of destiny deck.
    """
    name: str = field(default="Mastermind", init=False)
    description: str = field(
        default="See top 3 destiny cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Getaway(AlienPower):
    """
    Getaway - Power to Escape.
    Your losing ships return to colonies instead of warp.
    """
    name: str = field(default="Getaway", init=False)
    description: str = field(
        default="Losing ships return to colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fence(AlienPower):
    """
    Fence - Power to Trade.
    You may trade cards with opponent after a deal.
    """
    name: str = field(default="Fence", init=False)
    description: str = field(
        default="Trade cards after deals.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Witness(AlienPower):
    """
    Witness - Power to See.
    You may look at cards played before they're revealed.
    """
    name: str = field(default="Witness", init=False)
    description: str = field(
        default="See cards before reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Warden(AlienPower):
    """
    Warden - Power to Imprison.
    Ships you defeat stay in warp one extra turn.
    """
    name: str = field(default="Warden", init=False)
    description: str = field(
        default="Defeated ships stay in warp longer.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Informant(AlienPower):
    """
    Informant - Power to Reveal.
    When you lose, reveal opponent's entire hand.
    """
    name: str = field(default="Informant", init=False)
    description: str = field(
        default="Reveal opponent's hand when losing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all crime powers
AlienRegistry.register(Thief())
AlienRegistry.register(Pirate())
AlienRegistry.register(Burglar())
AlienRegistry.register(Smuggler())
AlienRegistry.register(Assassin())
AlienRegistry.register(Detective())
AlienRegistry.register(Sheriff())
AlienRegistry.register(Bounty())
AlienRegistry.register(Hacker())
AlienRegistry.register(Mastermind())
AlienRegistry.register(Getaway())
AlienRegistry.register(Fence())
AlienRegistry.register(Witness())
AlienRegistry.register(Warden())
AlienRegistry.register(Informant())
