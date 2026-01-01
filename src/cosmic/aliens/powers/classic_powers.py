"""
Classic alien powers from Cosmic Encounter expansions.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Fodder(AlienPower):
    """
    Fodder - Sacrifice ships for power.
    As offense, before cards are revealed, you may send any number of
    your ships from the encounter to the warp to add 1 to your total
    for each ship sacrificed.
    """
    name: str = field(default="Fodder", init=False)
    description: str = field(
        default="Sacrifice encounter ships for +1 each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Grief(AlienPower):
    """
    Grief - Spread sorrow.
    Whenever you lose ships to the warp, each other player must
    also lose one ship to the warp.
    """
    name: str = field(default="Grief", init=False)
    description: str = field(
        default="When you lose ships, others lose one too.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pincushion(AlienPower):
    """
    Pincushion - Gain from pain.
    Whenever you lose an encounter, draw one card from the deck
    for each ship you lost to the warp.
    """
    name: str = field(default="Pincushion", init=False)
    description: str = field(
        default="Draw card per ship lost when defeated.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jester(AlienPower):
    """
    Jester - Play tricks.
    Once per encounter, force an opponent to play their encounter
    card face-up while yours remains hidden until both are revealed.
    """
    name: str = field(default="Jester", init=False)
    description: str = field(
        default="Force opponent to reveal card first.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Roach(AlienPower):
    """
    Roach - Impossible to eliminate.
    Whenever you would lose your last home colony, immediately
    return 3 ships from the warp to that colony.
    """
    name: str = field(default="Roach", init=False)
    description: str = field(
        default="Return ships when losing last home colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Feline(AlienPower):
    """
    Feline - Nine lives.
    Start with 9 extra ships on your alien sheet. When you would
    lose ships to the warp, lose from here first.
    """
    name: str = field(default="Feline", init=False)
    description: str = field(
        default="9 reserve ships absorb losses first.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Horde(AlienPower):
    """
    Horde - Overwhelming numbers.
    At the start of each encounter, return one of your ships
    from the warp to any of your colonies.
    """
    name: str = field(default="Horde", init=False)
    description: str = field(
        default="Return 1 ship from warp each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Phantom(AlienPower):
    """
    Phantom - Intangible.
    Your ships are not sent to the warp when you lose an encounter
    as the offense; instead return them to your colonies.
    """
    name: str = field(default="Phantom", init=False)
    description: str = field(
        default="Offense ships return home instead of warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Diplomat(AlienPower):
    """
    Diplomat - Negotiate from strength.
    When you play a negotiate card and your opponent plays an attack,
    you may choose to have a deal succeed anyway, giving both of
    you one colony.
    """
    name: str = field(default="Diplomat", init=False)
    description: str = field(
        default="Force deals even against attacks.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Vulture(AlienPower):
    """
    Vulture - Feed on defeat.
    Whenever another player loses ships to the warp, draw one card
    from the deck.
    """
    name: str = field(default="Vulture", init=False)
    description: str = field(
        default="Draw card when others lose ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Fodder())
AlienRegistry.register(Grief())
AlienRegistry.register(Pincushion())
AlienRegistry.register(Jester())
AlienRegistry.register(Roach())
AlienRegistry.register(Feline())
AlienRegistry.register(Horde())
AlienRegistry.register(Phantom())
AlienRegistry.register(Diplomat())
AlienRegistry.register(Vulture())
