"""
Gem Powers - Crystal and precious stone-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Diamond(AlienPower):
    """Diamond - Unbreakable. Prevent first ship loss each encounter."""
    name: str = field(default="Diamond", init=False)
    description: str = field(default="Save first ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ruby(AlienPower):
    """Ruby - Fiery gem. +3 when attacking."""
    name: str = field(default="Ruby", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Sapphire(AlienPower):
    """Sapphire - Calm stone. +3 when defending."""
    name: str = field(default="Sapphire", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Emerald(AlienPower):
    """Emerald - Growth stone. Draw card when gaining colony."""
    name: str = field(default="Emerald", init=False)
    description: str = field(default="Draw card on colonization.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Amethyst(AlienPower):
    """Amethyst - Calming gem. Prevent Cosmic Zaps."""
    name: str = field(default="Amethyst", init=False)
    description: str = field(default="Immune to Cosmic Zaps.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Topaz(AlienPower):
    """Topaz - Clear vision. See opponent's hand before planning."""
    name: str = field(default="Topaz", init=False)
    description: str = field(default="View opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Opal(AlienPower):
    """Opal - Shifting colors. Change attack to negotiate or vice versa."""
    name: str = field(default="Opal", init=False)
    description: str = field(default="Switch card type after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pearl(AlienPower):
    """Pearl - Ocean treasure. +1 per card in hand."""
    name: str = field(default="Pearl", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Jade(AlienPower):
    """Jade - Luck stone. Redraw destiny once per turn."""
    name: str = field(default="Jade", init=False)
    description: str = field(default="Redraw destiny once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Onyx(AlienPower):
    """Onyx - Dark stone. Win ties."""
    name: str = field(default="Onyx", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quartz(AlienPower):
    """Quartz - Clear crystal. +2 always."""
    name: str = field(default="Quartz", init=False)
    description: str = field(default="+2 to all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Garnet(AlienPower):
    """Garnet - Blood stone. Steal ship from opponent when winning."""
    name: str = field(default="Garnet", init=False)
    description: str = field(default="Capture enemy ship on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Turquoise(AlienPower):
    """Turquoise - Protection stone. Allies immune to ship loss."""
    name: str = field(default="Turquoise", init=False)
    description: str = field(default="Protect allied ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crystal(AlienPower):
    """Crystal - Pure form. Double compensation received."""
    name: str = field(default="Crystal_Alt", init=False)
    description: str = field(default="Double compensation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Obsidian(AlienPower):
    """Obsidian - Volcanic glass. Destroy opponent's artifact."""
    name: str = field(default="Obsidian", init=False)
    description: str = field(default="Cancel one artifact per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Diamond())
AlienRegistry.register(Ruby())
AlienRegistry.register(Sapphire())
AlienRegistry.register(Emerald())
AlienRegistry.register(Amethyst())
AlienRegistry.register(Topaz())
AlienRegistry.register(Opal())
AlienRegistry.register(Pearl())
AlienRegistry.register(Jade())
AlienRegistry.register(Onyx())
AlienRegistry.register(Quartz())
AlienRegistry.register(Garnet())
AlienRegistry.register(Turquoise())
AlienRegistry.register(Crystal())
AlienRegistry.register(Obsidian())
