"""
Ancient Powers - Aliens with old and wise abilities.
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
class Ancestor(AlienPower):
    """
    Ancestor - Elder Power.
    Use dead player's power.
    """
    name: str = field(default="Ancestor", init=False)
    description: str = field(default="Use dead power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Archaeologist(AlienPower):
    """
    Archaeologist - Find Relics.
    Draw from discard.
    """
    name: str = field(default="Archaeologist", init=False)
    description: str = field(default="Draw discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chronicler(AlienPower):
    """
    Chronicler - Record History.
    Know all played cards.
    """
    name: str = field(default="Chronicler", init=False)
    description: str = field(default="Know played cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Elder(AlienPower):
    """
    Elder - Wisdom.
    See opponent's plan.
    """
    name: str = field(default="Elder", init=False)
    description: str = field(default="See opponent plan.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eternal(AlienPower):
    """
    Eternal - Never Die.
    Ships return immediately.
    """
    name: str = field(default="Eternal", init=False)
    description: str = field(default="Instant return.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fossil(AlienPower):
    """
    Fossil - Preserved Power.
    +3 constant bonus.
    """
    name: str = field(default="Fossil", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 constant bonus."""
        return total + 3


@dataclass
class Keeper(AlienPower):
    """
    Keeper - Guard Secrets.
    Hide power from others.
    """
    name: str = field(default="Keeper", init=False)
    description: str = field(default="Hide power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Legacy(AlienPower):
    """
    Legacy - Pass Power.
    Give ability to ally.
    """
    name: str = field(default="Legacy", init=False)
    description: str = field(default="Give ally ability.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lore(AlienPower):
    """
    Lore - Ancient Knowledge.
    See destiny deck.
    """
    name: str = field(default="Lore", init=False)
    description: str = field(default="See destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Memory(AlienPower):
    """
    Memory - Perfect Recall.
    Reuse played card.
    """
    name: str = field(default="Memory", init=False)
    description: str = field(default="Reuse card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Patriarch(AlienPower):
    """
    Patriarch - Lead Family.
    Ships worth +1 each.
    """
    name: str = field(default="Patriarch", init=False)
    description: str = field(default="Ships +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Primordial(AlienPower):
    """
    Primordial - First Being.
    Act first always.
    """
    name: str = field(default="Primordial", init=False)
    description: str = field(default="Act first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Relic(AlienPower):
    """
    Relic - Powerful Artifact.
    Extra artifact effect.
    """
    name: str = field(default="Relic", init=False)
    description: str = field(default="Extra artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sage(AlienPower):
    """
    Sage - Give Advice.
    Ally gets +2.
    """
    name: str = field(default="Sage", init=False)
    description: str = field(default="Ally +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Venerable(AlienPower):
    """
    Venerable - Respected.
    Players hesitate to attack.
    """
    name: str = field(default="Venerable", init=False)
    description: str = field(default="Hesitate attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ancestor())
AlienRegistry.register(Archaeologist())
AlienRegistry.register(Chronicler())
AlienRegistry.register(Elder())
AlienRegistry.register(Eternal())
AlienRegistry.register(Fossil())
AlienRegistry.register(Keeper())
AlienRegistry.register(Legacy())
AlienRegistry.register(Lore())
AlienRegistry.register(Memory())
AlienRegistry.register(Patriarch())
AlienRegistry.register(Primordial())
AlienRegistry.register(Relic())
AlienRegistry.register(Sage())
AlienRegistry.register(Venerable())
