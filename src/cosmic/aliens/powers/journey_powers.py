"""
Journey and pilgrimage themed alien powers for Cosmic Encounter.

Powers inspired by travels, quests, and spiritual journeys.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Pilgrim(AlienPower):
    """Pilgrim - Power of Faith. Spiritual journey."""
    name: str = field(default="Pilgrim", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Wanderer_Journey(AlienPower):
    """Wanderer_Journey - Power of Travel. Always moving."""
    name: str = field(default="Wanderer_Journey", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Seeker(AlienPower):
    """Seeker - Power of Search. Find what's hidden."""
    name: str = field(default="Seeker", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wayfinder(AlienPower):
    """Wayfinder - Power of Direction. Know the path."""
    name: str = field(default="Wayfinder", init=False)
    description: str = field(default="+4 attacking new planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if game.defense_planet and not game.defense_planet.has_colony(player.name):
                return base_total + 4
        return base_total


@dataclass
class Quester(AlienPower):
    """Quester - Power of Mission. Goal-oriented."""
    name: str = field(default="Quester", init=False)
    description: str = field(default="+5 at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return base_total + 5
        return base_total


@dataclass
class Traveler_Journey(AlienPower):
    """Traveler_Journey - Power of Distance. Go far."""
    name: str = field(default="Traveler_Journey", init=False)
    description: str = field(default="+1 per colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + colonies
        return base_total


@dataclass
class Rover(AlienPower):
    """Rover - Power of Roaming. Cover ground."""
    name: str = field(default="Rover", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Voyager(AlienPower):
    """Voyager - Power of Exploration. Cosmic travel."""
    name: str = field(default="Voyager", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 4
        return base_total


@dataclass
class Drifter(AlienPower):
    """Drifter - Power of Flow. Go with currents."""
    name: str = field(default="Drifter", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 2)


@dataclass
class Passage(AlienPower):
    """Passage - Power of Transit. Move through."""
    name: str = field(default="Passage", init=False)
    description: str = field(default="Lose only 1 ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Destination(AlienPower):
    """Destination - Power of Goals. Reach the end."""
    name: str = field(default="Destination", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Homecoming(AlienPower):
    """Homecoming - Power of Return. Coming back."""
    name: str = field(default="Homecoming", init=False)
    description: str = field(default="Return 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Odyssey(AlienPower):
    """Odyssey - Power of Epic. Long journey."""
    name: str = field(default="Odyssey", init=False)
    description: str = field(default="+2 per turn (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(10, game.current_turn * 2)
            return base_total + bonus
        return base_total


@dataclass
class Safari(AlienPower):
    """Safari - Power of Hunt. Track targets."""
    name: str = field(default="Safari", init=False)
    description: str = field(default="+4 attacking players with colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE and game.defense:
            opp_colonies = game.defense.count_foreign_colonies(game.planets)
            if opp_colonies > 0:
                return base_total + 4
        return base_total


# Register all journey powers
JOURNEY_POWERS = [
    Pilgrim, Wanderer_Journey, Seeker, Wayfinder, Quester,
    Traveler_Journey, Rover, Voyager, Drifter, Passage,
    Destination, Homecoming, Odyssey, Safari,
]

for power_class in JOURNEY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
