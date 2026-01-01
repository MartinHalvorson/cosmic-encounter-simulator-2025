"""
Body Part Powers for Cosmic Encounter.

Aliens inspired by body parts and anatomy.
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
class Heart_Body(AlienPower):
    """Heart_Body - Power of Life."""
    name: str = field(default="Heart_Body", init=False)
    description: str = field(default="Retrieve 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(min(2, player.ships_in_warp))


@dataclass
class Brain_Body(AlienPower):
    """Brain_Body - Power of Thought."""
    name: str = field(default="Brain_Body", init=False)
    description: str = field(default="Draw extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Fist(AlienPower):
    """Fist - Power of Strike."""
    name: str = field(default="Fist", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Eye_Body(AlienPower):
    """Eye_Body - Power of Sight."""
    name: str = field(default="Eye_Body", init=False)
    description: str = field(default="See opponent cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ear_Body(AlienPower):
    """Ear_Body - Power of Hearing."""
    name: str = field(default="Ear_Body", init=False)
    description: str = field(default="Detect traps.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spine(AlienPower):
    """Spine - Power of Support."""
    name: str = field(default="Spine", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Muscle(AlienPower):
    """Muscle - Power of Force."""
    name: str = field(default="Muscle", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Bone_Body(AlienPower):
    """Bone_Body - Power of Structure."""
    name: str = field(default="Bone_Body", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Nerve(AlienPower):
    """Nerve - Power of Signal."""
    name: str = field(default="Nerve", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Skin(AlienPower):
    """Skin - Power of Protection."""
    name: str = field(default="Skin", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Lung(AlienPower):
    """Lung - Power of Breath."""
    name: str = field(default="Lung", init=False)
    description: str = field(default="+2 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Liver(AlienPower):
    """Liver - Power of Regeneration."""
    name: str = field(default="Liver", init=False)
    description: str = field(default="Retrieve 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


# Register all aliens
for alien_class in [
    Heart_Body, Brain_Body, Fist, Eye_Body, Ear_Body,
    Spine, Muscle, Bone_Body, Nerve, Skin,
    Lung, Liver,
]:
    AlienRegistry.register(alien_class())
