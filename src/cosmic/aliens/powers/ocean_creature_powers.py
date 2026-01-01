"""
Ocean Creature Powers - Sea life themed aliens.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Whale_Ocean(AlienPower):
    """Whale_Ocean - Massive and powerful."""
    name: str = field(default="Whale_Ocean", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Dolphin_Ocean(AlienPower):
    """Dolphin_Ocean - Intelligent and swift."""
    name: str = field(default="Dolphin_Ocean", init=False)
    description: str = field(default="+4 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count > 0:
            return total + 4
        return total


@dataclass
class Shark_Ocean(AlienPower):
    """Shark_Ocean - Apex predator."""
    name: str = field(default="Shark_Ocean", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Octopus_Ocean(AlienPower):
    """Octopus_Ocean - Eight-armed wonder."""
    name: str = field(default="Octopus_Ocean", init=False)
    description: str = field(default="+1 per card (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(8, len(player.hand))
        return total


@dataclass
class Jellyfish_Ocean(AlienPower):
    """Jellyfish_Ocean - Drifting stinger."""
    name: str = field(default="Jellyfish_Ocean", init=False)
    description: str = field(default="+3 plus random +0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3 + random.randint(0, 3)
        return total


@dataclass
class Seahorse_Ocean(AlienPower):
    """Seahorse_Ocean - Gentle swimmer."""
    name: str = field(default="Seahorse_Ocean", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Starfish_Ocean(AlienPower):
    """Starfish_Ocean - Regenerating creature."""
    name: str = field(default="Starfish_Ocean", init=False)
    description: str = field(default="+5 with 3 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return total + 5
        return total


@dataclass
class Crab_Ocean(AlienPower):
    """Crab_Ocean - Armored sidewalker."""
    name: str = field(default="Crab_Ocean", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Eel_Ocean(AlienPower):
    """Eel_Ocean - Electric shocker."""
    name: str = field(default="Eel_Ocean", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Lobster_Ocean(AlienPower):
    """Lobster_Ocean - Clawed crustacean."""
    name: str = field(default="Lobster_Ocean", init=False)
    description: str = field(default="+5 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 5
        return total


@dataclass
class Clam_Ocean(AlienPower):
    """Clam_Ocean - Pearl maker."""
    name: str = field(default="Clam_Ocean", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Manta_Ocean(AlienPower):
    """Manta_Ocean - Graceful glider."""
    name: str = field(default="Manta_Ocean", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Coral_Ocean(AlienPower):
    """Coral_Ocean - Living reef."""
    name: str = field(default="Coral_Ocean", init=False)
    description: str = field(default="+2 per colony (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + min(6, colonies * 2)
        return total


@dataclass
class Squid_Ocean(AlienPower):
    """Squid_Ocean - Ink sprayer."""
    name: str = field(default="Squid_Ocean", init=False)
    description: str = field(default="+4 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 4
        return total


@dataclass
class Anglerfish_Ocean(AlienPower):
    """Anglerfish_Ocean - Deep sea lure."""
    name: str = field(default="Anglerfish_Ocean", init=False)
    description: str = field(default="+5 with 2 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 2:
            return total + 5
        return total


OCEAN_CREATURE_POWERS = [
    Whale_Ocean, Dolphin_Ocean, Shark_Ocean, Octopus_Ocean, Jellyfish_Ocean,
    Seahorse_Ocean, Starfish_Ocean, Crab_Ocean, Eel_Ocean, Lobster_Ocean,
    Clam_Ocean, Manta_Ocean, Coral_Ocean, Squid_Ocean, Anglerfish_Ocean
]

for power_class in OCEAN_CREATURE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
