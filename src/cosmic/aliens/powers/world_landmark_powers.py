"""
World Landmark Powers - Famous landmark themed aliens.
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
class Eiffel_Landmark(AlienPower):
    """Eiffel_Landmark - Iron lady."""
    name: str = field(default="Eiffel_Landmark", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Colosseum_Landmark(AlienPower):
    """Colosseum_Landmark - Ancient arena."""
    name: str = field(default="Colosseum_Landmark", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Pyramid_Landmark(AlienPower):
    """Pyramid_Landmark - Ancient wonder."""
    name: str = field(default="Pyramid_Landmark", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, game.current_turn)
        return total


@dataclass
class Great_Wall_Landmark(AlienPower):
    """Great_Wall_Landmark - Defensive marvel."""
    name: str = field(default="Great_Wall_Landmark", init=False)
    description: str = field(default="+6 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class Taj_Mahal_Landmark(AlienPower):
    """Taj_Mahal_Landmark - Beauty eternal."""
    name: str = field(default="Taj_Mahal_Landmark", init=False)
    description: str = field(default="+5 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 5
        return total


@dataclass
class Statue_Liberty_Landmark(AlienPower):
    """Statue_Liberty_Landmark - Freedom torch."""
    name: str = field(default="Statue_Liberty_Landmark", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Big_Ben_Landmark(AlienPower):
    """Big_Ben_Landmark - Timely power."""
    name: str = field(default="Big_Ben_Landmark", init=False)
    description: str = field(default="+4 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 4
        return total


@dataclass
class Sydney_Opera_Landmark(AlienPower):
    """Sydney_Opera_Landmark - Artistic shell."""
    name: str = field(default="Sydney_Opera_Landmark", init=False)
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
class Machu_Picchu_Landmark(AlienPower):
    """Machu_Picchu_Landmark - Mountain citadel."""
    name: str = field(default="Machu_Picchu_Landmark", init=False)
    description: str = field(default="+5 with 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 5
        return total


@dataclass
class Stonehenge_Landmark(AlienPower):
    """Stonehenge_Landmark - Ancient mystery."""
    name: str = field(default="Stonehenge_Landmark", init=False)
    description: str = field(default="+2 plus random +0-4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + random.randint(0, 4)
        return total


@dataclass
class Petra_Landmark(AlienPower):
    """Petra_Landmark - Rose city."""
    name: str = field(default="Petra_Landmark", init=False)
    description: str = field(default="+5 when alone.", init=False)
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
            return total + 5
        return total


@dataclass
class Christ_Redeemer_Landmark(AlienPower):
    """Christ_Redeemer_Landmark - Open arms."""
    name: str = field(default="Christ_Redeemer_Landmark", init=False)
    description: str = field(default="+5 with allies.", init=False)
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
            return total + 5
        return total


@dataclass
class Angkor_Wat_Landmark(AlienPower):
    """Angkor_Wat_Landmark - Temple city."""
    name: str = field(default="Angkor_Wat_Landmark", init=False)
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
class Parthenon_Landmark(AlienPower):
    """Parthenon_Landmark - Greek glory."""
    name: str = field(default="Parthenon_Landmark", init=False)
    description: str = field(default="+1 per card (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, len(player.hand))
        return total


@dataclass
class Leaning_Tower_Landmark(AlienPower):
    """Leaning_Tower_Landmark - Tilted marvel."""
    name: str = field(default="Leaning_Tower_Landmark", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


WORLD_LANDMARK_POWERS = [
    Eiffel_Landmark, Colosseum_Landmark, Pyramid_Landmark, Great_Wall_Landmark,
    Taj_Mahal_Landmark, Statue_Liberty_Landmark, Big_Ben_Landmark,
    Sydney_Opera_Landmark, Machu_Picchu_Landmark, Stonehenge_Landmark,
    Petra_Landmark, Christ_Redeemer_Landmark, Angkor_Wat_Landmark,
    Parthenon_Landmark, Leaning_Tower_Landmark
]

for power_class in WORLD_LANDMARK_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
