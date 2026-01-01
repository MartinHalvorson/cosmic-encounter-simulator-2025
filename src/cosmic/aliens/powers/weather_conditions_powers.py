"""
Weather Conditions themed alien powers for Cosmic Encounter.

Powers based on various weather phenomena and atmospheric conditions.
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
# PRECIPITATION
# ============================================================================

@dataclass
class Drizzle(AlienPower):
    """Drizzle - Power of Light Rain. Gentle bonus."""
    name: str = field(default="Drizzle", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Downpour(AlienPower):
    """Downpour - Power of Heavy Rain. Strong effect."""
    name: str = field(default="Downpour", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Hailstorm(AlienPower):
    """Hailstorm - Power of Ice. Damaging precipitation."""
    name: str = field(default="Hailstorm", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Sleet(AlienPower):
    """Sleet - Power of Mixed. Ice and rain."""
    name: str = field(default="Sleet", init=False)
    description: str = field(default="Random +2 to +5 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(2, 5)
        return base_total


# ============================================================================
# WIND CONDITIONS
# ============================================================================

@dataclass
class Breeze(AlienPower):
    """Breeze - Power of Gentle Wind. Light movement."""
    name: str = field(default="Breeze", init=False)
    description: str = field(default="+2 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 2
        return base_total


@dataclass
class Gale(AlienPower):
    """Gale - Power of Strong Wind. Powerful force."""
    name: str = field(default="Gale", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Squall(AlienPower):
    """Squall - Power of Sudden Wind. Quick burst."""
    name: str = field(default="Squall", init=False)
    description: str = field(default="+5 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Doldrums(AlienPower):
    """Doldrums - Power of Calm. No wind."""
    name: str = field(default="Doldrums", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


# ============================================================================
# TEMPERATURE
# ============================================================================

@dataclass
class Heatwave(AlienPower):
    """Heatwave - Power of Extreme Heat. Burning intensity."""
    name: str = field(default="Heatwave_WC", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Cold_Snap(AlienPower):
    """Cold_Snap - Power of Sudden Cold. Freeze enemies."""
    name: str = field(default="Cold_Snap", init=False)
    description: str = field(default="Opponent's card -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frost_WC(AlienPower):
    """Frost_WC - Power of Light Ice. Chilling effect."""
    name: str = field(default="Frost_WC", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Thaw(AlienPower):
    """Thaw - Power of Warming. Ice melts."""
    name: str = field(default="Thaw", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# VISIBILITY
# ============================================================================

@dataclass
class Clear_Sky(AlienPower):
    """Clear_Sky - Power of Visibility. See all."""
    name: str = field(default="Clear_Sky", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Overcast(AlienPower):
    """Overcast - Power of Clouds. Obscured view."""
    name: str = field(default="Overcast", init=False)
    description: str = field(default="Opponent can't see your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Smog(AlienPower):
    """Smog - Power of Pollution. Visibility reduced."""
    name: str = field(default="Smog", init=False)
    description: str = field(default="All players' cards -1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mist_WC(AlienPower):
    """Mist_WC - Power of Light Fog. Partial obscurity."""
    name: str = field(default="Mist_WC", init=False)
    description: str = field(default="+3 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


# Register all weather conditions powers
WEATHER_CONDITIONS_POWERS = [
    Drizzle, Downpour, Hailstorm, Sleet,
    Breeze, Gale, Squall, Doldrums,
    Heatwave, Cold_Snap, Frost_WC, Thaw,
    Clear_Sky, Overcast, Smog, Mist_WC,
]


# Auto-register all powers
for power_class in WEATHER_CONDITIONS_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
