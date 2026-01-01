"""
Apocalypse themed alien powers for Cosmic Encounter.

Powers based on end times, survival, and post-apocalyptic themes.
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
# END TIMES
# ============================================================================

@dataclass
class Doomsday(AlienPower):
    """Doomsday - Power of Finality. End-game bonus."""
    name: str = field(default="Doomsday", init=False)
    description: str = field(default="+8 after turn 20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 20:
            return base_total + 8
        return base_total


@dataclass
class Plague(AlienPower):
    """Plague - Power of Contagion. Spread weakness."""
    name: str = field(default="Plague_Power", init=False)
    description: str = field(default="Opponent loses 1 ship before combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Famine(AlienPower):
    """Famine - Power of Starvation. Resource denial."""
    name: str = field(default="Famine", init=False)
    description: str = field(default="Opponent discards 1 card per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cataclysm(AlienPower):
    """Cataclysm - Power of Disaster. Once per game devastation."""
    name: str = field(default="Cataclysm", init=False)
    description: str = field(default="Once per game: +12 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    used: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and not self.used:
            if random.random() < 0.25:
                self.used = True
                return base_total + 12
        return base_total


@dataclass
class Extinction(AlienPower):
    """Extinction - Power of Endings. Final strike."""
    name: str = field(default="Extinction", init=False)
    description: str = field(default="+5 when opponent has 4+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# SURVIVAL
# ============================================================================

@dataclass
class Survivor(AlienPower):
    """Survivor - Power of Endurance. Never give up."""
    name: str = field(default="Survivor", init=False)
    description: str = field(default="+4 when you have 0-1 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies <= 1:
                return base_total + 4
        return base_total


@dataclass
class Scavenger(AlienPower):
    """Scavenger - Power of Recovery. Find resources."""
    name: str = field(default="Scavenger", init=False)
    description: str = field(default="Draw 1 card after any encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bunker(AlienPower):
    """Bunker - Power of Shelter. Strong defense."""
    name: str = field(default="Bunker", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Prepper(AlienPower):
    """Prepper - Power of Preparation. Ready for anything."""
    name: str = field(default="Prepper", init=False)
    description: str = field(default="+2 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, len(player.hand) * 2)
        return base_total


@dataclass
class Wasteland(AlienPower):
    """Wasteland - Power of Desolation. Harsh environment."""
    name: str = field(default="Wasteland", init=False)
    description: str = field(default="All players lose 1 ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ============================================================================
# POST-APOCALYPTIC
# ============================================================================

@dataclass
class Raider(AlienPower):
    """Raider - Power of Pillaging. Take resources."""
    name: str = field(default="Raider", init=False)
    description: str = field(default="Draw 1 card from opponent on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mutant(AlienPower):
    """Mutant - Power of Adaptation. Random bonuses."""
    name: str = field(default="Mutant", init=False)
    description: str = field(default="Random +0 to +6 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(0, 6)
        return base_total


@dataclass
class Wanderer_Apoc(AlienPower):
    """Wanderer_Apoc - Power of Nomads. Move freely."""
    name: str = field(default="Wanderer_Apoc", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vault_Dweller(AlienPower):
    """Vault_Dweller - Power of Isolation. Protected bonus."""
    name: str = field(default="Vault_Dweller", init=False)
    description: str = field(default="+3 when defending home system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Wastelander(AlienPower):
    """Wastelander - Power of Harsh Living. Tough survivor."""
    name: str = field(default="Wastelander", init=False)
    description: str = field(default="+2 per encounter this game (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    encounters: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            self.encounters += 1
            return base_total + min(8, self.encounters * 2)
        return base_total


# ============================================================================
# DESTRUCTION
# ============================================================================

@dataclass
class Devastator(AlienPower):
    """Devastator - Power of Ruin. Destroy everything."""
    name: str = field(default="Devastator", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Fallout(AlienPower):
    """Fallout - Power of Radiation. Lingering effects."""
    name: str = field(default="Fallout", init=False)
    description: str = field(default="+1 per turn (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class Nuclear(AlienPower):
    """Nuclear - Power of the Atom. Devastating attack."""
    name: str = field(default="Nuclear", init=False)
    description: str = field(default="Once per game: destroy all defending ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    used: bool = False


@dataclass
class Collapse(AlienPower):
    """Collapse - Power of Entropy. Systems fail."""
    name: str = field(default="Collapse", init=False)
    description: str = field(default="+4 after turn 15.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 15:
            return base_total + 4
        return base_total


# Register all apocalypse powers
APOCALYPSE_POWERS = [
    Doomsday, Plague, Famine, Cataclysm, Extinction,
    Survivor, Scavenger, Bunker, Prepper, Wasteland,
    Raider, Mutant, Wanderer_Apoc, Vault_Dweller, Wastelander,
    Devastator, Fallout, Nuclear, Collapse,
]


# Auto-register all powers
for power_class in APOCALYPSE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
