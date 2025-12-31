"""
Horror Powers for Cosmic Encounter.

Aliens inspired by horror movie and story tropes.
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
class Zombie_Alt_2(AlienPower):
    """
    Zombie_Alt_2 - Power of Undeath.
    Ships sent to warp return to any of your colonies.
    """
    name: str = field(default="Zombie_Alt_2", init=False)
    description: str = field(
        default="Ships return from warp immediately.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Vampire_Alt_2(AlienPower):
    """
    Vampire_Alt_2 - Power to Drain.
    When you win, take 1 card from loser.
    """
    name: str = field(default="Vampire_Alt_2", init=False)
    description: str = field(
        default="Take 1 card from loser when winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Werewolf_Alt(AlienPower):
    """
    Werewolf_Alt - Power of Transformation.
    +5 every other encounter.
    """
    name: str = field(default="Werewolf_Alt", init=False)
    description: str = field(
        default="+5 every other encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ghost_Alt_2(AlienPower):
    """
    Ghost_Alt_2 - Power of Haunting.
    Ships in warp count toward your combat total.
    """
    name: str = field(default="Ghost_Alt_2", init=False)
    description: str = field(
        default="Warp ships count in combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mummy(AlienPower):
    """
    Mummy - Power of the Curse.
    Players who attack you lose 1 ship at encounter end.
    """
    name: str = field(default="Mummy", init=False)
    description: str = field(
        default="Attackers lose 1 ship at end.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frankenstein(AlienPower):
    """
    Frankenstein - Power of Creation.
    Add discarded cards to your hand instead of discard pile.
    """
    name: str = field(default="Frankenstein", init=False)
    description: str = field(
        default="Collect discarded cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Slasher(AlienPower):
    """
    Slasher - Power of Fear.
    +4 against players with fewer colonies than you.
    """
    name: str = field(default="Slasher", init=False)
    description: str = field(
        default="+4 vs weaker players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Poltergeist_Alt(AlienPower):
    """
    Poltergeist_Alt - Power of Chaos.
    Force opponent to discard 1 random card before planning.
    """
    name: str = field(default="Poltergeist_Alt", init=False)
    description: str = field(
        default="Force opponent to discard 1 card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nightmare(AlienPower):
    """
    Nightmare - Power of Dreams.
    Look at opponent's hand before choosing your card.
    """
    name: str = field(default="Nightmare", init=False)
    description: str = field(
        default="See opponent's hand before planning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Creeper(AlienPower):
    """
    Creeper - Power of Stealth.
    Win ties automatically.
    """
    name: str = field(default="Creeper", init=False)
    description: str = field(
        default="Win all ties.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Possessor(AlienPower):
    """
    Possessor - Power to Control.
    Once per encounter, use opponent's power as your own.
    """
    name: str = field(default="Possessor", init=False)
    description: str = field(
        default="Use opponent's power once.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Reaper(AlienPower):
    """
    Reaper - Power of Death.
    Ships you defeat are removed from the game.
    """
    name: str = field(default="Reaper", init=False)
    description: str = field(
        default="Defeated ships removed from game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Horde(AlienPower):
    """
    Horde - Power of Numbers.
    +1 for each ship you have in the encounter.
    """
    name: str = field(default="Horde", init=False)
    description: str = field(
        default="+1 per ship in encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Doppelganger(AlienPower):
    """
    Doppelganger - Power to Copy.
    Your card becomes a copy of opponent's card.
    """
    name: str = field(default="Doppelganger", init=False)
    description: str = field(
        default="Copy opponent's card value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lurker_Horror(AlienPower):
    """
    Lurker_Horror - Power to Wait.
    +3 if you've been passed over for attack twice.
    """
    name: str = field(default="Lurker_Horror", init=False)
    description: str = field(
        default="+3 when passed over twice.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all horror powers
AlienRegistry.register(Zombie_Alt_2())
AlienRegistry.register(Vampire_Alt_2())
AlienRegistry.register(Werewolf_Alt())
AlienRegistry.register(Ghost_Alt_2())
AlienRegistry.register(Mummy())
AlienRegistry.register(Frankenstein())
AlienRegistry.register(Slasher())
AlienRegistry.register(Poltergeist_Alt())
AlienRegistry.register(Nightmare())
AlienRegistry.register(Creeper())
AlienRegistry.register(Possessor())
AlienRegistry.register(Reaper())
AlienRegistry.register(Horde())
AlienRegistry.register(Doppelganger())
AlienRegistry.register(Lurker_Horror())
