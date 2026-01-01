"""
Gothic themed alien powers for Cosmic Encounter.

Powers based on gothic horror, Victorian darkness, and supernatural themes.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# GOTHIC CREATURES
# ============================================================================

@dataclass
class Vampire_Gothic(AlienPower):
    """Vampire_Gothic - Power of Blood. Drain enemies."""
    name: str = field(default="Vampire_Gothic", init=False)
    description: str = field(default="+3 and heal 1 ship on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Werewolf_Gothic(AlienPower):
    """Werewolf_Gothic - Power of the Beast. Savage combat."""
    name: str = field(default="Werewolf_Gothic", init=False)
    description: str = field(default="+5 on odd-numbered turns (full moon).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 5
        return base_total


@dataclass
class Ghost_Gothic(AlienPower):
    """Ghost_Gothic - Power of the Spirit. Ethereal presence."""
    name: str = field(default="Ghost_Gothic", init=False)
    description: str = field(default="Ships can't be destroyed, only sent to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ghoul(AlienPower):
    """Ghoul - Power of Consumption. Feed on the dead."""
    name: str = field(default="Ghoul", init=False)
    description: str = field(default="+1 per ship lost by opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wraith_Gothic(AlienPower):
    """Wraith_Gothic - Power of Shadows. Unseen movement."""
    name: str = field(default="Wraith_Gothic", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Banshee(AlienPower):
    """Banshee - Power of the Scream. Terrifying wail."""
    name: str = field(default="Banshee", init=False)
    description: str = field(default="Opponent's allies flee (don't count).", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# GOTHIC SETTINGS
# ============================================================================

@dataclass
class Crypt(AlienPower):
    """Crypt - Power of the Tomb. Defense of the dead."""
    name: str = field(default="Crypt", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Cathedral(AlienPower):
    """Cathedral - Power of Sanctuary. Protected ground."""
    name: str = field(default="Cathedral", init=False)
    description: str = field(default="+3 when defending home colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Graveyard(AlienPower):
    """Graveyard - Power of the Dead. Draw from the fallen."""
    name: str = field(default="Graveyard", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Manor(AlienPower):
    """Manor - Power of the Estate. Aristocratic privilege."""
    name: str = field(default="Manor", init=False)
    description: str = field(default="+2 per foreign colony (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(8, colonies * 2)
        return base_total


@dataclass
class Dungeon_Gothic(AlienPower):
    """Dungeon_Gothic - Power of Imprisonment. Trap enemies."""
    name: str = field(default="Dungeon_Gothic", init=False)
    description: str = field(default="Ships lost against you stay in warp extra turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# GOTHIC CONCEPTS
# ============================================================================

@dataclass
class Darkness_Gothic(AlienPower):
    """Darkness_Gothic - Power of Night. Thrives in shadow."""
    name: str = field(default="Darkness_Gothic", init=False)
    description: str = field(default="+4 on even-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 4
        return base_total


@dataclass
class Curse(AlienPower):
    """Curse - Power of Affliction. Weaken enemies."""
    name: str = field(default="Curse", init=False)
    description: str = field(default="Opponent's card -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dread(AlienPower):
    """Dread - Power of Fear. Intimidate enemies."""
    name: str = field(default="Dread", init=False)
    description: str = field(default="Opponent can't ally against you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Occult(AlienPower):
    """Occult - Power of Secrets. Hidden knowledge."""
    name: str = field(default="Occult", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ritual(AlienPower):
    """Ritual - Power of Ceremony. Building power."""
    name: str = field(default="Ritual", init=False)
    description: str = field(default="+1 per turn (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class Nightmare_Gothic(AlienPower):
    """Nightmare_Gothic - Power of Terror. Devastating effects."""
    name: str = field(default="Nightmare_Gothic", init=False)
    description: str = field(default="Random +3 to +8 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(3, 8)
        return base_total


# Register all gothic powers
GOTHIC_POWERS = [
    Vampire_Gothic, Werewolf_Gothic, Ghost_Gothic, Ghoul, Wraith_Gothic, Banshee,
    Crypt, Cathedral, Graveyard, Manor, Dungeon_Gothic,
    Darkness_Gothic, Curse, Dread, Occult, Ritual, Nightmare_Gothic,
]


# Auto-register all powers
for power_class in GOTHIC_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
