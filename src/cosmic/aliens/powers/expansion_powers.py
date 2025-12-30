"""
Additional alien powers from Cosmic Encounter expansions.
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
class Assassin(AlienPower):
    """
    Assassin - Target opponent's ships go to warp even if you lose.
    """
    name: str = field(default="Assassin", init=False)
    description: str = field(
        default="Defense ships go to warp even if you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Butler(AlienPower):
    """
    Butler - Collect cards discarded by other players.
    """
    name: str = field(default="Butler", init=False)
    description: str = field(
        default="Collect one card whenever others discard.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Changeling(AlienPower):
    """
    Changeling - Copy an opponent's alien power.
    """
    name: str = field(default="Changeling", init=False)
    description: str = field(
        default="Use opponent's alien power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Chronos(AlienPower):
    """
    Chronos - Restart encounters.
    """
    name: str = field(default="Chronos", init=False)
    description: str = field(
        default="Restart encounter after reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Claw(AlienPower):
    """
    Claw - Force opponents to ally with you.
    """
    name: str = field(default="Claw", init=False)
    description: str = field(
        default="Force one player to ally with you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Crone(AlienPower):
    """
    Crone - Curse opponents to lose power.
    """
    name: str = field(default="Crone", init=False)
    description: str = field(
        default="Disable an opponent's power for the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dictator(AlienPower):
    """
    Dictator - Control alliance decisions.
    """
    name: str = field(default="Dictator", init=False)
    description: str = field(
        default="Control all alliance decisions.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Empath(AlienPower):
    """
    Empath - Know opponent's encounter card value.
    """
    name: str = field(default="Empath", init=False)
    description: str = field(
        default="Know opponent's card value before reveal.",
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
class Ethic(AlienPower):
    """
    Ethic - Force fair encounters.
    """
    name: str = field(default="Ethic", init=False)
    description: str = field(
        default="Force equal ship counts in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Gambler(AlienPower):
    """
    Gambler - Double the stakes.
    """
    name: str = field(default="Gambler", init=False)
    description: str = field(
        default="Both sides lose ships regardless of outcome.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Grudge(AlienPower):
    """
    Grudge - Gain strength from defeats.
    """
    name: str = field(default="Grudge", init=False)
    description: str = field(
        default="Gain tokens from losses, add to combat total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Human(AlienPower):
    """
    Human - Gain +4 in all encounters.
    """
    name: str = field(default="Human", init=False)
    description: str = field(
        default="+4 in all encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Mutant(AlienPower):
    """
    Mutant - Refill hand at start of each turn.
    """
    name: str = field(default="Mutant", init=False)
    description: str = field(
        default="Draw up to 8 cards at turn start.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active and game.offense == player:
            while len(player.hand) < 8:
                card = game.cosmic_deck.draw()
                player.add_card(card)


@dataclass
class Negator(AlienPower):
    """
    Negator - Cancel alien powers.
    """
    name: str = field(default="Negator", init=False)
    description: str = field(
        default="Cancel another player's power use.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Observer(AlienPower):
    """
    Observer - See all hidden information.
    """
    name: str = field(default="Observer", init=False)
    description: str = field(
        default="See all hidden cards and hands.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pentaform(AlienPower):
    """
    Pentaform - Start with 5 alien powers.
    """
    name: str = field(default="Pentaform", init=False)
    description: str = field(
        default="Start with 5 powers, lose one per lost encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Giver(AlienPower):
    """
    Giver - Draw extra cards for others.
    """
    name: str = field(default="Giver", init=False)
    description: str = field(
        default="Give extra drawn cards to other players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seeker(AlienPower):
    """
    Seeker - Search the deck for specific cards.
    """
    name: str = field(default="Seeker", init=False)
    description: str = field(
        default="Search deck for cards when drawing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sheriff(AlienPower):
    """
    Sheriff - Prevent attacks on other players.
    """
    name: str = field(default="Sheriff", init=False)
    description: str = field(
        default="Force attacks to target you instead.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sniveler(AlienPower):
    """
    Sniveler - Whine for advantages.
    """
    name: str = field(default="Sniveler", init=False)
    description: str = field(
        default="Whine for +5 if no one helps you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Surge(AlienPower):
    """
    Surge - Add extra ships mid-encounter.
    """
    name: str = field(default="Surge", init=False)
    description: str = field(
        default="Add ships after cards are revealed.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Yin(AlienPower):
    """
    Yin - Win ties.
    """
    name: str = field(default="Yin", init=False)
    description: str = field(
        default="Win all ties.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Fido(AlienPower):
    """
    Fido - Retrieve ships when winning.
    """
    name: str = field(default="Fido", init=False)
    description: str = field(
        default="Win: retrieve all ships from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        if as_main_player and player.power_active:
            ships = player.ships_in_warp
            retrieved = player.retrieve_ships_from_warp(ships)
            player.return_ships_to_colonies(retrieved, player.home_planets)


@dataclass
class Visionary(AlienPower):
    """
    Visionary - Predict and benefit from correct predictions.
    """
    name: str = field(default="Visionary", init=False)
    description: str = field(
        default="Predict encounter outcome for bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Silencer(AlienPower):
    """
    Silencer - Prevent players from speaking.
    """
    name: str = field(default="Silencer", init=False)
    description: str = field(
        default="Silence a player each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Philanthropist_Alt(AlienPower):
    """
    Altruist - Give away ships for cards.
    """
    name: str = field(default="Altruist", init=False)
    description: str = field(
        default="Give ships to others, draw cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Assassin())
AlienRegistry.register(Butler())
AlienRegistry.register(Changeling())
AlienRegistry.register(Chronos())
AlienRegistry.register(Claw())
AlienRegistry.register(Crone())
AlienRegistry.register(Dictator())
AlienRegistry.register(Empath())
AlienRegistry.register(Ethic())
AlienRegistry.register(Gambler())
AlienRegistry.register(Grudge())
AlienRegistry.register(Human())
AlienRegistry.register(Mutant())
AlienRegistry.register(Negator())
AlienRegistry.register(Observer())
AlienRegistry.register(Pentaform())
AlienRegistry.register(Giver())
AlienRegistry.register(Seeker())
AlienRegistry.register(Sheriff())
AlienRegistry.register(Sniveler())
AlienRegistry.register(Surge())
AlienRegistry.register(Yin())
AlienRegistry.register(Fido())
AlienRegistry.register(Visionary())
AlienRegistry.register(Silencer())
AlienRegistry.register(Philanthropist_Alt())
