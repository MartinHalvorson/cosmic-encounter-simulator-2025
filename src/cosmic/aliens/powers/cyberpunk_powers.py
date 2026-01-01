"""
Cyberpunk themed alien powers for Cosmic Encounter.

Powers based on cyberpunk aesthetics, technology, and dystopian futures.
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
# HACKER TYPES
# ============================================================================

@dataclass
class Hacker_Cyber(AlienPower):
    """Hacker_Cyber - Power of Intrusion. Access systems."""
    name: str = field(default="Hacker_Cyber", init=False)
    description: str = field(default="See opponent's hand before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Netrunner(AlienPower):
    """Netrunner - Power of the Net. Digital superiority."""
    name: str = field(default="Netrunner", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Console_Cowboy(AlienPower):
    """Console_Cowboy - Power of the Console. Fast hacking."""
    name: str = field(default="Console_Cowboy", init=False)
    description: str = field(default="+2 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, len(player.hand) * 2)
        return base_total


@dataclass
class Decker(AlienPower):
    """Decker - Power of the Deck. Interface bonus."""
    name: str = field(default="Decker", init=False)
    description: str = field(default="+4 with exactly 4 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and len(player.hand) == 4:
            return base_total + 4
        return base_total


# ============================================================================
# AUGMENTATIONS
# ============================================================================

@dataclass
class Chromed(AlienPower):
    """Chromed - Power of Chrome. Enhanced body."""
    name: str = field(default="Chromed", init=False)
    description: str = field(default="+3 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Cyborg(AlienPower):
    """Cyborg - Power of Integration. Human-machine hybrid."""
    name: str = field(default="Cyborg", init=False)
    description: str = field(default="+2 plus random +0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2 + random.randint(0, 3)
        return base_total


@dataclass
class Neural_Link(AlienPower):
    """Neural_Link - Power of Connection. Brain-machine interface."""
    name: str = field(default="Neural_Link", init=False)
    description: str = field(default="+1 per encounter this game (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    encounters: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            self.encounters += 1
            return base_total + min(8, self.encounters)
        return base_total


@dataclass
class Synthetic(AlienPower):
    """Synthetic - Power of Artifice. Fully artificial."""
    name: str = field(default="Synthetic", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Reflex_Booster(AlienPower):
    """Reflex_Booster - Power of Speed. Enhanced reflexes."""
    name: str = field(default="Reflex_Booster", init=False)
    description: str = field(default="Act first in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# CORPORATIONS
# ============================================================================

@dataclass
class Megacorp(AlienPower):
    """Megacorp - Power of Capital. Corporate might."""
    name: str = field(default="Megacorp", init=False)
    description: str = field(default="+3 per foreign colony (max +9).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(9, colonies * 3)
        return base_total


@dataclass
class Fixer(AlienPower):
    """Fixer - Power of Connections. Make deals happen."""
    name: str = field(default="Fixer", init=False)
    description: str = field(default="Negotiate cards always succeed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Street_Samurai(AlienPower):
    """Street_Samurai - Power of the Street. Combat specialist."""
    name: str = field(default="Street_Samurai", init=False)
    description: str = field(default="+5 when you have 4+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships >= 4:
            return base_total + 5
        return base_total


@dataclass
class Corpo(AlienPower):
    """Corpo - Power of the Corporation. Wealth bonus."""
    name: str = field(default="Corpo", init=False)
    description: str = field(default="Draw extra card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# TECHNOLOGY
# ============================================================================

@dataclass
class Neon(AlienPower):
    """Neon - Power of Light. Bright and bold."""
    name: str = field(default="Neon", init=False)
    description: str = field(default="+3 on odd-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 3
        return base_total


@dataclass
class Hologram(AlienPower):
    """Hologram - Power of Illusion. Not what you see."""
    name: str = field(default="Hologram_Cyber", init=False)
    description: str = field(default="Opponent can't see your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Drone_Pilot(AlienPower):
    """Drone_Pilot - Power of Drones. Remote combat."""
    name: str = field(default="Drone_Pilot", init=False)
    description: str = field(default="+2 per ship (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + min(8, ships * 2)


@dataclass
class Black_Ice(AlienPower):
    """Black_Ice - Power of Defense. Dangerous firewall."""
    name: str = field(default="Black_Ice", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Virus(AlienPower):
    """Virus - Power of Infection. Spread and corrupt."""
    name: str = field(default="Virus_Cyber", init=False)
    description: str = field(default="Opponent's card -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all cyberpunk powers
CYBERPUNK_POWERS = [
    Hacker_Cyber, Netrunner, Console_Cowboy, Decker,
    Chromed, Cyborg, Neural_Link, Synthetic, Reflex_Booster,
    Megacorp, Fixer, Street_Samurai, Corpo,
    Neon, Hologram, Drone_Pilot, Black_Ice, Virus,
]


# Auto-register all powers
for power_class in CYBERPUNK_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
