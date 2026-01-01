"""
Emotion Powers for Cosmic Encounter.

Aliens inspired by human emotions and feelings.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Joy(AlienPower):
    """Joy - Power of Happiness."""
    name: str = field(default="Joy", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Anger(AlienPower):
    """Anger - Power of Rage."""
    name: str = field(default="Anger", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Fear(AlienPower):
    """Fear - Power of Terror."""
    name: str = field(default="Fear", init=False)
    description: str = field(default="Opponent loses 1 ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sadness(AlienPower):
    """Sadness - Power of Grief."""
    name: str = field(default="Sadness", init=False)
    description: str = field(default="+4 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Love(AlienPower):
    """Love - Power of Affection."""
    name: str = field(default="Love", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hope(AlienPower):
    """Hope - Power of Optimism."""
    name: str = field(default="Hope", init=False)
    description: str = field(default="+4 when behind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Envy(AlienPower):
    """Envy - Power of Jealousy."""
    name: str = field(default="Envy", init=False)
    description: str = field(default="Copy opponent bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pride(AlienPower):
    """Pride - Power of Confidence."""
    name: str = field(default="Pride", init=False)
    description: str = field(default="+4 with most colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Surprise(AlienPower):
    """Surprise - Power of Shock."""
    name: str = field(default="Surprise", init=False)
    description: str = field(default="Random +1 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 6)
        return base_total


@dataclass
class Disgust(AlienPower):
    """Disgust - Power of Revulsion."""
    name: str = field(default="Disgust", init=False)
    description: str = field(default="Reject bad alliances.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Courage(AlienPower):
    """Courage - Power of Bravery."""
    name: str = field(default="Courage", init=False)
    description: str = field(default="+5 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Anxiety(AlienPower):
    """Anxiety - Power of Worry."""
    name: str = field(default="Anxiety", init=False)
    description: str = field(default="See next destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Calm(AlienPower):
    """Calm - Power of Serenity."""
    name: str = field(default="Calm", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Excitement(AlienPower):
    """Excitement - Power of Thrill."""
    name: str = field(default="Excitement", init=False)
    description: str = field(default="+2 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Awe(AlienPower):
    """Awe - Power of Wonder."""
    name: str = field(default="Awe", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


# Register all aliens
for alien_class in [
    Joy, Anger, Fear, Sadness, Love,
    Hope, Envy, Pride, Surprise, Disgust,
    Courage, Anxiety, Calm, Excitement, Awe,
]:
    AlienRegistry.register(alien_class())
