"""
Fantasy Powers for Cosmic Encounter.

Aliens inspired by fantasy and fairy tale concepts.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Wizard_Alt(AlienPower):
    """
    Wizard_Alt - Power of Magic.
    Once per encounter, add +5 to your total.
    """
    name: str = field(default="Wizard_Alt", init=False)
    description: str = field(
        default="+5 once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Knight_Alt(AlienPower):
    """
    Knight_Alt - Power of Honor.
    +3 when defending any player's home planets.
    """
    name: str = field(default="Knight_Alt", init=False)
    description: str = field(
        default="+3 defending any home planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dragon_Alt(AlienPower):
    """
    Dragon_Alt - Power of Fire.
    +4 on offense; opponent loses 1 extra ship when you win.
    """
    name: str = field(default="Dragon_Alt", init=False)
    description: str = field(
        default="+4 offense, opponent loses extra ship.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Princess_Alt(AlienPower):
    """
    Princess_Alt - Power of Royalty.
    Allies always join your side when invited.
    """
    name: str = field(default="Princess_Alt", init=False)
    description: str = field(
        default="Allies always accept invitations.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goblin(AlienPower):
    """
    Goblin - Power to Steal.
    When you lose, take 1 random card from winner.
    """
    name: str = field(default="Goblin", init=False)
    description: str = field(
        default="Take 1 card from winner when losing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Elf(AlienPower):
    """
    Elf - Power of Precision.
    Your negotiate cards count as attack 06.
    """
    name: str = field(default="Elf", init=False)
    description: str = field(
        default="Negotiates become attack 06.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dwarf(AlienPower):
    """
    Dwarf - Power of Craft.
    +2 when you have 3+ cards in hand.
    """
    name: str = field(default="Dwarf", init=False)
    description: str = field(
        default="+2 with 3+ cards in hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Troll_Alt(AlienPower):
    """
    Troll_Alt - Power of Regeneration.
    Return 1 ship from warp at end of each encounter.
    """
    name: str = field(default="Troll_Alt", init=False)
    description: str = field(
        default="Return 1 ship from warp each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Witch(AlienPower):
    """
    Witch - Power of Curses.
    Opponent's highest card counts as their lowest.
    """
    name: str = field(default="Witch", init=False)
    description: str = field(
        default="Flip opponent's card value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Fairy_Alt(AlienPower):
    """
    Fairy_Alt - Power of Wishes.
    Once per game, automatically win an encounter.
    """
    name: str = field(default="Fairy_Alt", init=False)
    description: str = field(
        default="Auto-win once per game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Warlock(AlienPower):
    """
    Warlock - Power of Pacts.
    +2 for each deal you've made this game.
    """
    name: str = field(default="Warlock", init=False)
    description: str = field(
        default="+2 per deal made (max +6).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Paladin(AlienPower):
    """
    Paladin - Power of Justice.
    +5 against players who have attacked you this game.
    """
    name: str = field(default="Paladin", init=False)
    description: str = field(
        default="+5 vs players who attacked you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mage(AlienPower):
    """
    Mage - Power of Spells.
    Draw 2 cards when you play a negotiate.
    """
    name: str = field(default="Mage", init=False)
    description: str = field(
        default="Draw 2 cards when playing negotiate.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Necromancer_Alt(AlienPower):
    """
    Necromancer_Alt - Power of the Dead.
    +1 for each ship in the warp.
    """
    name: str = field(default="Necromancer_Alt", init=False)
    description: str = field(
        default="+1 per ship in warp (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Alchemist_Alt(AlienPower):
    """
    Alchemist_Alt - Power of Transformation.
    Convert any card to a negotiate or vice versa.
    """
    name: str = field(default="Alchemist_Alt", init=False)
    description: str = field(
        default="Transform card types.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all fantasy powers
AlienRegistry.register(Wizard_Alt())
AlienRegistry.register(Knight_Alt())
AlienRegistry.register(Dragon_Alt())
AlienRegistry.register(Princess_Alt())
AlienRegistry.register(Goblin())
AlienRegistry.register(Elf())
AlienRegistry.register(Dwarf())
AlienRegistry.register(Troll_Alt())
AlienRegistry.register(Witch())
AlienRegistry.register(Fairy_Alt())
AlienRegistry.register(Warlock())
AlienRegistry.register(Paladin())
AlienRegistry.register(Mage())
AlienRegistry.register(Necromancer_Alt())
AlienRegistry.register(Alchemist_Alt())
