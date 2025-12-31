"""
Legendary alien powers - rare and powerful abilities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Ace(AlienPower):
    """
    Ace - Master pilot.
    Your ships always escape to colonies instead of going to warp.
    """
    name: str = field(default="Ace", init=False)
    description: str = field(
        default="Ships escape to colonies instead of warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, reason: str) -> int:
        # Ships return to colonies instead of warp
        player.return_ships_to_colonies(count, player.home_planets)
        return 0  # No ships go to warp


@dataclass
class Basilisk(AlienPower):
    """
    Basilisk - Petrifying gaze.
    Opponent's attack card is treated as 0 if they look at it.
    """
    name: str = field(default="Basilisk", init=False)
    description: str = field(
        default="Opponent's card treated as 0 sometimes.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Coordinator(AlienPower):
    """
    Coordinator - Alliance commander.
    Allied ships count as double for total calculation.
    """
    name: str = field(default="Coordinator", init=False)
    description: str = field(
        default="Allied ships count double.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Diplomat(AlienPower):
    """
    Diplomat - Peace advocate.
    Can force both players to negotiate.
    """
    name: str = field(default="Diplomat", init=False)
    description: str = field(
        default="Force both players to negotiate.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Emperor(AlienPower):
    """
    Emperor - Absolute ruler.
    You choose who the defender must ally with.
    """
    name: str = field(default="Emperor", init=False)
    description: str = field(
        default="Control defender's alliance choices.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Fortress(AlienPower):
    """
    Fortress - Impenetrable defense.
    +8 when defending your home planets.
    """
    name: str = field(default="Fortress", init=False)
    description: str = field(
        default="Major bonus defending home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        if side == Side.DEFENSE and game.defense_planet:
            if game.defense_planet.owner == player:
                return value + 8
        return value


@dataclass
class Gambit(AlienPower):
    """
    Gambit - Risk taker.
    Can double attack value but lose all ships if you lose.
    """
    name: str = field(default="Gambit", init=False)
    description: str = field(
        default="Double attack, but lose all ships if defeated.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Heretic(AlienPower):
    """
    Heretic - Defies conventions.
    Wins ties instead of defense.
    """
    name: str = field(default="Heretic", init=False)
    description: str = field(
        default="Win ties as offense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Immortal(AlienPower):
    """
    Immortal - Cannot be eliminated.
    Always keep at least 1 ship on each home planet.
    """
    name: str = field(default="Immortal", init=False)
    description: str = field(
        default="Cannot lose last ship on home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jinx(AlienPower):
    """
    Jinx - Curse bringer.
    Opponent must play lowest attack card.
    """
    name: str = field(default="Jinx", init=False)
    description: str = field(
        default="Force opponent to play lowest card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Knight(AlienPower):
    """
    Knight - Noble warrior.
    +2 for each ally on your side.
    """
    name: str = field(default="Knight", init=False)
    description: str = field(
        default="Bonus per allied player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        allies = game.offense_allies if side == Side.OFFENSE else game.defense_allies
        return total + (len(allies) * 2)


@dataclass
class Leech(AlienPower):
    """
    Leech - Energy vampire.
    Steal opponent's card bonus.
    """
    name: str = field(default="Leech", init=False)
    description: str = field(
        default="Reduce opponent's attack card by 5.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monarch(AlienPower):
    """
    Monarch - Sovereign ruler.
    Draw an extra card at start of each turn.
    """
    name: str = field(default="Monarch", init=False)
    description: str = field(
        default="Draw extra card at turn start.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if game.offense == player:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Noble(AlienPower):
    """
    Noble - High standing.
    Other players cannot attack you if they have more colonies.
    """
    name: str = field(default="Noble", init=False)
    description: str = field(
        default="Leaders cannot attack you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Overlord(AlienPower):
    """
    Overlord - Dominating presence.
    Can attack any player regardless of destiny.
    """
    name: str = field(default="Overlord", init=False)
    description: str = field(
        default="Choose defender regardless of destiny.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Predator(AlienPower):
    """
    Predator - Hunts weak prey.
    +5 against players with fewer ships than you.
    """
    name: str = field(default="Predator", init=False)
    description: str = field(
        default="Bonus vs players with fewer ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        my_ships = player.total_ships_in_play(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_ships = opponent.total_ships_in_play(game.planets)
            if my_ships > opp_ships:
                return value + 5
        return value


@dataclass
class Queller(AlienPower):
    """
    Queller - Suppresses abilities.
    Opponent's alien power is nullified.
    """
    name: str = field(default="Queller", init=False)
    description: str = field(
        default="Nullify opponent's alien power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ravager(AlienPower):
    """
    Ravager - Destroyer of colonies.
    Remove opponent's colony when you win.
    """
    name: str = field(default="Ravager", init=False)
    description: str = field(
        default="Destroy enemy colony on win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Striker(AlienPower):
    """
    Striker - First strike advantage.
    Deal damage before opponent can respond.
    """
    name: str = field(default="Striker", init=False)
    description: str = field(
        default="Attack first in encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Tycoon(AlienPower):
    """
    Tycoon - Wealthy merchant.
    Start with extra cards.
    """
    name: str = field(default="Tycoon", init=False)
    description: str = field(
        default="Start with 4 extra cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_game_start(self, game: "Game", player: "Player") -> None:
        cards = game.cosmic_deck.draw_multiple(4)
        player.add_cards(cards)


@dataclass
class Undertaker(AlienPower):
    """
    Undertaker - Benefits from death.
    Draw 2 cards when any ships go to warp.
    """
    name: str = field(default="Undertaker", init=False)
    description: str = field(
        default="Draw cards when ships go to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ace())
AlienRegistry.register(Basilisk())
AlienRegistry.register(Coordinator())
AlienRegistry.register(Emperor())
AlienRegistry.register(Fortress())
AlienRegistry.register(Gambit())
AlienRegistry.register(Heretic())
AlienRegistry.register(Immortal())
AlienRegistry.register(Jinx())
AlienRegistry.register(Knight())
AlienRegistry.register(Leech())
AlienRegistry.register(Monarch())
AlienRegistry.register(Noble())
AlienRegistry.register(Overlord())
AlienRegistry.register(Predator())
AlienRegistry.register(Queller())
AlienRegistry.register(Ravager())
AlienRegistry.register(Striker())
AlienRegistry.register(Tycoon())
AlienRegistry.register(Undertaker())
