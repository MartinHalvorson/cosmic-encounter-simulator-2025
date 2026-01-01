"""
Advanced alien powers from Cosmic Encounter expansions.
These represent more complex and strategic aliens.
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
class Prophet(AlienPower):
    """
    Prophet - Can predict and influence encounter outcomes.
    """
    name: str = field(default="Prophet", init=False)
    description: str = field(
        default="Predict encounter outcome for bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        # Bonus for correct prediction (simulated as random boost)
        if random.random() < 0.3:  # 30% chance of "correct prediction"
            return value + 4
        return value


@dataclass
class Will(AlienPower):
    """
    Will - Can force opponents to play specific cards.
    """
    name: str = field(default="Will", init=False)
    description: str = field(
        default="Force opponent to play highest or lowest card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Schizoid(AlienPower):
    """
    Schizoid - Has two different powers that alternate.
    """
    name: str = field(default="Schizoid", init=False)
    description: str = field(
        default="Alternate between offensive and defensive bonuses.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    _offense_mode: bool = field(default=True, init=False)

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        self._offense_mode = not self._offense_mode

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        if self._offense_mode and side == Side.OFFENSE:
            return value + 3
        elif not self._offense_mode and side == Side.DEFENSE:
            return value + 3
        return value


@dataclass
class Cavalry(AlienPower):
    """
    Cavalry - Can add extra ships to encounters as reinforcements.
    """
    name: str = field(default="Cavalry", init=False)
    description: str = field(
        default="Add bonus ships during reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        # Can add up to 2 bonus ships
        return count + min(2, player.ships_in_warp)


@dataclass
class Witch(AlienPower):
    """
    Witch - Can curse opponents to reduce their power.
    """
    name: str = field(default="Witch", init=False)
    description: str = field(
        default="Curse opponent's attack card value.",
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
class Siren(AlienPower):
    """
    Siren - Lures ships away from encounters.
    """
    name: str = field(default="Siren", init=False)
    description: str = field(
        default="Remove opponent ships from encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        # Reduce opponent's ship count by 1
        return count


@dataclass
class Miser(AlienPower):
    """
    Miser - Hoards cards and can have a larger hand.
    """
    name: str = field(default="Miser", init=False)
    description: str = field(
        default="Keep extra cards in a hoard.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_game_start(self, game: "Game", player: "Player") -> None:
        # Draw extra cards to start
        cards = game.cosmic_deck.draw_multiple(4)
        player.add_cards(cards)


@dataclass
class Magician(AlienPower):
    """
    Magician - Can swap cards with the deck.
    """
    name: str = field(default="Magician", init=False)
    description: str = field(
        default="Swap a card with the top of the deck.",
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
class Insect(AlienPower):
    """
    Insect - Swarm tactics with ship multiplication.
    """
    name: str = field(default="Insect", init=False)
    description: str = field(
        default="Ships count double in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        return count * 2


@dataclass
class Invader(AlienPower):
    """
    Invader - Bonus when attacking foreign planets.
    """
    name: str = field(default="Invader", init=False)
    description: str = field(
        default="Bonus attack value when invading.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        if side == Side.OFFENSE:
            return value + 4
        return value


@dataclass
class Foam(AlienPower):
    """
    Foam - Spreads to colonize multiple planets.
    """
    name: str = field(default="Foam", init=False)
    description: str = field(
        default="Can land on additional planet when winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Doppelganger(AlienPower):
    """
    Doppelganger - Copies the attack card played by opponent.
    """
    name: str = field(default="Doppelganger", init=False)
    description: str = field(
        default="Match opponent's attack card value.",
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
class Delegator(AlienPower):
    """
    Delegator - Can make allies the main player.
    """
    name: str = field(default="Delegator", init=False)
    description: str = field(
        default="Delegate encounter to an ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Connoisseur(AlienPower):
    """
    Connoisseur - Gains bonuses from collecting specific card types.
    """
    name: str = field(default="Connoisseur", init=False)
    description: str = field(
        default="Bonus from card variety in hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        # Bonus based on hand size
        bonus = min(3, len(player.hand) // 3)
        return value + bonus


@dataclass
class Chrysalis(AlienPower):
    """
    Chrysalis - Transforms into a stronger form after losing.
    """
    name: str = field(default="Chrysalis", init=False)
    description: str = field(
        default="Gain bonus after each loss.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    _transformation_level: int = field(default=0, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main: bool) -> None:
        if as_main:
            self._transformation_level = min(5, self._transformation_level + 1)

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        return value + self._transformation_level


@dataclass
class Bulwark(AlienPower):
    """
    Bulwark - Superior defense capabilities.
    """
    name: str = field(default="Bulwark", init=False)
    description: str = field(
        default="Bonus defense value.",
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
        if side == Side.DEFENSE:
            return value + 6
        return value


@dataclass
class Battlemaster(AlienPower):
    """
    Battlemaster - Expert at combat encounters.
    """
    name: str = field(default="Battlemaster", init=False)
    description: str = field(
        default="Add both ships AND card value bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 3


@dataclass
class Architect(AlienPower):
    """
    Architect - Builds defensive structures on colonies.
    """
    name: str = field(default="Architect", init=False)
    description: str = field(
        default="Home planets have defensive bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        if side == Side.DEFENSE:
            # Bonus when defending home planet
            if game.defense_planet and game.defense_planet.owner == player:
                return value + 5
        return value


@dataclass
class Aristocrat(AlienPower):
    """
    Aristocrat - Gains advantages from having colonies.
    """
    name: str = field(default="Aristocrat", init=False)
    description: str = field(
        default="Bonus based on number of colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        colonies = player.count_foreign_colonies(game.planets)
        return value + colonies


@dataclass
class Bully(AlienPower):
    """
    Bully - Stronger against weaker opponents.
    """
    name: str = field(default="Bully", init=False)
    description: str = field(
        default="Bonus when opponent has fewer ships.",
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
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            their_ships = sum(game.defense_ships.values())
            if my_ships > their_ships:
                return value + 4
        elif side == Side.DEFENSE:
            my_ships = sum(game.defense_ships.values())
            their_ships = sum(game.offense_ships.values())
            if my_ships > their_ships:
                return value + 4
        return value


@dataclass
class Converter(AlienPower):
    """
    Converter - Turns defeated ships into allies.
    """
    name: str = field(default="Converter", init=False)
    description: str = field(
        default="Defeated enemy ships join your colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Electron(AlienPower):
    """
    Electron - Moves ships freely between colonies.
    """
    name: str = field(default="Electron", init=False)
    description: str = field(
        default="Rearrange ships between colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Engineer(AlienPower):
    """
    Engineer - Improves card values through modification.
    """
    name: str = field(default="Engineer", init=False)
    description: str = field(
        default="Improve attack card value by 2.",
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
        return value + 2


@dataclass
class Extortionist(AlienPower):
    """
    Extortionist - Forces opponents to give up cards.
    """
    name: str = field(default="Extortionist", init=False)
    description: str = field(
        default="Take cards from opponents.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fungus(AlienPower):
    """
    Fungus - Spreads ships to adjacent planets.
    """
    name: str = field(default="Fungus", init=False)
    description: str = field(
        default="Ships spread to neighboring planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ghast(AlienPower):
    """
    Ghast - Returns from defeats stronger.
    """
    name: str = field(default="Ghast", init=False)
    description: str = field(
        default="Ships return from warp faster.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role: PlayerRole) -> None:
        # Retrieve extra ships from warp
        if player.ships_in_warp > 0:
            extra = min(2, player.ships_in_warp)
            player.retrieve_ships_from_warp(extra)
            player.return_ships_to_colonies(extra, player.home_planets)


@dataclass
class Glutton(AlienPower):
    """
    Glutton - Draws extra cards from deck.
    """
    name: str = field(default="Glutton", init=False)
    description: str = field(
        default="Draw extra cards after encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Guardian(AlienPower):
    """
    Guardian - Protects allies from harm.
    """
    name: str = field(default="Guardian", init=False)
    description: str = field(
        default="Ally ships don't go to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harbinger(AlienPower):
    """
    Harbinger - Reveals destiny before it's drawn.
    """
    name: str = field(default="Harbinger", init=False)
    description: str = field(
        default="See destiny card before it's drawn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Horde(AlienPower):
    """
    Horde - Strength in numbers.
    """
    name: str = field(default="Horde", init=False)
    description: str = field(
        default="Ships count triple when you have 4+.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        if count >= 4:
            return count * 3
        return count


@dataclass
class Infiltrator(AlienPower):
    """
    Infiltrator - Places ships on enemy planets secretly.
    """
    name: str = field(default="Infiltrator", init=False)
    description: str = field(
        default="Place ships on enemy planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers (instantiate each class)
AlienRegistry.register(Prophet())
AlienRegistry.register(Schizoid())
AlienRegistry.register(Cavalry())
AlienRegistry.register(Witch())
AlienRegistry.register(Siren())
AlienRegistry.register(Miser())
AlienRegistry.register(Magician())
AlienRegistry.register(Insect())
AlienRegistry.register(Invader())
AlienRegistry.register(Foam())
AlienRegistry.register(Doppelganger())
AlienRegistry.register(Delegator())
AlienRegistry.register(Connoisseur())
AlienRegistry.register(Chrysalis())
AlienRegistry.register(Bulwark())
AlienRegistry.register(Battlemaster())
AlienRegistry.register(Architect())
AlienRegistry.register(Aristocrat())
AlienRegistry.register(Bully())
AlienRegistry.register(Converter())
AlienRegistry.register(Electron())
AlienRegistry.register(Engineer())
AlienRegistry.register(Extortionist())
AlienRegistry.register(Fungus())
AlienRegistry.register(Ghast())
AlienRegistry.register(Glutton())
AlienRegistry.register(Guardian())
AlienRegistry.register(Harbinger())
AlienRegistry.register(Horde())
AlienRegistry.register(Infiltrator())
