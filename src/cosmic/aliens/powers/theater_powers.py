"""
Theater Powers for Cosmic Encounter.

Aliens inspired by theatrical and performance arts.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Actor(AlienPower):
    """
    Actor - Power to Perform.
    You may play any card type as any other card type.
    """
    name: str = "Actor"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Director(AlienPower):
    """
    Director - Power to Control.
    You choose which ally ships join each side.
    """
    name: str = "Director"
    timing: PowerTiming = PowerTiming.ALLIANCE
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Playwright(AlienPower):
    """
    Playwright - Power to Script.
    Before destiny, declare the outcome. If you're right, gain 2 cards.
    """
    name: str = "Playwright"
    timing: PowerTiming = PowerTiming.DESTINY
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Critic(AlienPower):
    """
    Critic - Power to Judge.
    After cards are revealed, you may cancel the encounter.
    """
    name: str = "Critic"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Understudy(AlienPower):
    """
    Understudy - Power to Replace.
    You may use any player's alien power instead of your own.
    """
    name: str = "Understudy"
    timing: PowerTiming = PowerTiming.CONSTANT
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Stagehand(AlienPower):
    """
    Stagehand - Power Behind Scenes.
    Add +2 when you are not the main player in an encounter.
    """
    name: str = "Stagehand"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +2 when ally."""
        if not player.power_active:
            return base_total
        if player != game.offense and player != game.defense:
            return base_total + 2
        return base_total


@dataclass
class Prompter(AlienPower):
    """
    Prompter - Power to Hint.
    You may show an ally your card before they commit ships.
    """
    name: str = "Prompter"
    timing: PowerTiming = PowerTiming.ALLIANCE
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Costumer(AlienPower):
    """
    Costumer - Power to Disguise.
    Your card is revealed as a different card type than played.
    """
    name: str = "Costumer"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Producer(AlienPower):
    """
    Producer - Power to Fund.
    You may spend cards to add +3 each to your total.
    """
    name: str = "Producer"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Audience(AlienPower):
    """
    Audience - Power of Reception.
    When not involved, you may cheer (+2) or boo (-2) either side.
    """
    name: str = "Audience"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Mime(AlienPower):
    """
    Mime - Power of Silence.
    Your plays are made face-down and revealed last.
    """
    name: str = "Mime"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Comedian(AlienPower):
    """
    Comedian - Power to Amuse.
    When you lose, draw 1 card. When you win, draw 2.
    """
    name: str = "Comedian"
    timing: PowerTiming = PowerTiming.RESOLUTION
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Tragedian(AlienPower):
    """
    Tragedian - Power of Drama.
    When you lose, opponent also loses 1 ship.
    """
    name: str = "Tragedian"
    timing: PowerTiming = PowerTiming.LOSE_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Improvisor(AlienPower):
    """
    Improvisor - Power of Spontaneity.
    You may change your card after seeing opponent's card.
    """
    name: str = "Improvisor"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Narrator(AlienPower):
    """
    Narrator - Power of Story.
    Once per game, describe the outcome of an encounter. It happens.
    """
    name: str = "Narrator"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


# Register all theater powers
def register_theater_powers():
    from ..registry import AlienRegistry

    powers = [
        Actor(),
        Director(),
        Playwright(),
        Critic(),
        Understudy(),
        Stagehand(),
        Prompter(),
        Costumer(),
        Producer(),
        Audience(),
        Mime(),
        Comedian(),
        Tragedian(),
        Improvisor(),
        Narrator(),
    ]

    for power in powers:
        AlienRegistry.register(power)


# Auto-register on import
register_theater_powers()
