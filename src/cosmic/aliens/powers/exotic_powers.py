"""
Exotic alien powers from Cosmic Encounter expansions.
These represent unique and unusual aliens with creative mechanics.
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
class Aura(AlienPower):
    """
    Aura - Radiates protective energy.
    Your ships cannot be sent to the warp from your home planets.
    """
    name: str = field(default="Aura", init=False)
    description: str = field(
        default="Home planet ships are protected from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, reason: str) -> int:
        # Ships from home planets don't go to warp when defending
        if reason == "encounter_loss" and game.defense == player:
            if game.defense_planet and game.defense_planet.owner == player:
                return 0  # Protected on home planet
        return count


@dataclass
class Berserker(AlienPower):
    """
    Berserker - Gains strength from battle.
    Add +2 to your total for each encounter you've had this turn.
    """
    name: str = field(default="Berserker", init=False)
    description: str = field(
        default="Bonus for multiple encounters per turn.",
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
        # Bonus based on encounter number
        return total + (game.encounter_number * 2)


@dataclass
class Collector(AlienPower):
    """
    Collector - Hoards ships from defeated opponents.
    When you win an encounter, keep one defeated enemy ship.
    """
    name: str = field(default="Collector", init=False)
    description: str = field(
        default="Capture enemy ships when you win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Decoy(AlienPower):
    """
    Decoy - Creates false signals.
    Your attack card value is hidden until after resolution.
    """
    name: str = field(default="Decoy", init=False)
    description: str = field(
        default="Card value revealed after resolution.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Echo(AlienPower):
    """
    Echo - Repeats successful strategies.
    Can play the same card twice in a row.
    """
    name: str = field(default="Echo", init=False)
    description: str = field(
        default="Play same card again next encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fanatic(AlienPower):
    """
    Fanatic - Extreme commitment to victory.
    Must commit all available ships to encounters.
    """
    name: str = field(default="Fanatic", init=False)
    description: str = field(
        default="Always commit maximum ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Grifter(AlienPower):
    """
    Grifter - Master of deception and theft.
    Steal cards from opponents during planning.
    """
    name: str = field(default="Grifter", init=False)
    description: str = field(
        default="Steal a card during planning phase.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hawk(AlienPower):
    """
    Hawk - Aggressive predator.
    +4 attack when targeting a player with more colonies.
    """
    name: str = field(default="Hawk", init=False)
    description: str = field(
        default="Bonus when attacking colony leaders.",
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
        if side == Side.OFFENSE and game.defense:
            my_colonies = player.count_foreign_colonies(game.planets)
            their_colonies = game.defense.count_foreign_colonies(game.planets)
            if their_colonies > my_colonies:
                return value + 4
        return value


@dataclass
class Illusionist(AlienPower):
    """
    Illusionist - Creates false perceptions.
    Opponent must guess your card type or lose.
    """
    name: str = field(default="Illusionist", init=False)
    description: str = field(
        default="Opponent must guess your card type.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Judge(AlienPower):
    """
    Judge - Arbiter of encounters.
    Can declare a winner regardless of totals once per game.
    """
    name: str = field(default="Judge", init=False)
    description: str = field(
        default="Declare winner once per game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Kamikaze(AlienPower):
    """
    Kamikaze - Sacrifice for victory.
    Send all your ships to warp for +10 to attack.
    """
    name: str = field(default="Kamikaze", init=False)
    description: str = field(
        default="Sacrifice ships for massive attack bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Lurker(AlienPower):
    """
    Lurker - Waits and strikes.
    +2 for each turn you haven't had an encounter.
    """
    name: str = field(default="Lurker", init=False)
    description: str = field(
        default="Bonus from waiting between encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Martyr(AlienPower):
    """
    Martyr - Gains power from sacrifice.
    Draw 2 cards when you lose an encounter.
    """
    name: str = field(default="Martyr", init=False)
    description: str = field(
        default="Draw cards when you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main: bool) -> None:
        if as_main:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Nexus(AlienPower):
    """
    Nexus - Central hub of power.
    Can ally with both sides simultaneously.
    """
    name: str = field(default="Nexus", init=False)
    description: str = field(
        default="Can join both offense and defense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Outcast(AlienPower):
    """
    Outcast - Rejected by all.
    Cannot be allied with, but gains +3 for each rejection.
    """
    name: str = field(default="Outcast", init=False)
    description: str = field(
        default="Bonus from alliance rejections.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Prowler(AlienPower):
    """
    Prowler - Stalks prey.
    Can attack same player twice in a row.
    """
    name: str = field(default="Prowler", init=False)
    description: str = field(
        default="Choose to attack same player again.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quarantine(AlienPower):
    """
    Quarantine - Isolates threats.
    Prevent one player from being invited as ally.
    """
    name: str = field(default="Quarantine", init=False)
    description: str = field(
        default="Block one player from allying.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rebel(AlienPower):
    """
    Rebel - Fights against authority.
    Bonus when defending against the leading player.
    """
    name: str = field(default="Rebel", init=False)
    description: str = field(
        default="Bonus when defending vs leader.",
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
        if side == Side.DEFENSE and game.offense:
            # Check if offense is in the lead
            off_colonies = game.offense.count_foreign_colonies(game.planets)
            max_colonies = max(p.count_foreign_colonies(game.planets) for p in game.players)
            if off_colonies == max_colonies and off_colonies > 0:
                return value + 5
        return value


@dataclass
class Sentinel(AlienPower):
    """
    Sentinel - Eternal vigilance.
    Ships on home planets count as double for defense.
    """
    name: str = field(default="Sentinel", init=False)
    description: str = field(
        default="Double ships when defending home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        if side == Side.DEFENSE and game.defense_planet:
            if game.defense_planet.owner == player:
                return count * 2
        return count


@dataclass
class Tempest(AlienPower):
    """
    Tempest - Chaotic force of nature.
    All players must discard a random card at encounter start.
    """
    name: str = field(default="Tempest", init=False)
    description: str = field(
        default="All players discard a card each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Usurper(AlienPower):
    """
    Usurper - Seizes power.
    Can take control of opponent's colonies after winning.
    """
    name: str = field(default="Usurper", init=False)
    description: str = field(
        default="Take control of opponent's colony on win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Vandal(AlienPower):
    """
    Vandal - Destroys what it can't have.
    Remove one ship from each player when you lose.
    """
    name: str = field(default="Vandal", init=False)
    description: str = field(
        default="Others lose ships when you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wraith(AlienPower):
    """
    Wraith - Ethereal being.
    Can pass through defenses - ignore ship counts.
    """
    name: str = field(default="Wraith", init=False)
    description: str = field(
        default="Opponent's ships don't count.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Xenophobe(AlienPower):
    """
    Xenophobe - Fears outsiders.
    +3 when no allies are present on either side.
    """
    name: str = field(default="Xenophobe", init=False)
    description: str = field(
        default="Bonus in allyless encounters.",
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
        if not game.offense_allies and not game.defense_allies:
            return value + 3
        return value


@dataclass
class Yogi(AlienPower):
    """
    Yogi - Master of patience.
    Can skip encounters to gain cards.
    """
    name: str = field(default="Yogi", init=False)
    description: str = field(
        default="Skip turn to draw 3 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Zealot(AlienPower):
    """
    Zealot - Uncompromising belief.
    Cannot negotiate - must always attack.
    """
    name: str = field(default="Zealot", init=False)
    description: str = field(
        default="Cannot play negotiate cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Aura())
AlienRegistry.register(Berserker())
AlienRegistry.register(Collector())
AlienRegistry.register(Decoy())
AlienRegistry.register(Echo())
AlienRegistry.register(Fanatic())
AlienRegistry.register(Grifter())
AlienRegistry.register(Hawk())
AlienRegistry.register(Illusionist())
AlienRegistry.register(Judge())
AlienRegistry.register(Kamikaze())
AlienRegistry.register(Lurker())
AlienRegistry.register(Martyr())
AlienRegistry.register(Nexus())
AlienRegistry.register(Outcast())
AlienRegistry.register(Prowler())
AlienRegistry.register(Quarantine())
AlienRegistry.register(Rebel())
AlienRegistry.register(Sentinel())
AlienRegistry.register(Tempest())
AlienRegistry.register(Usurper())
AlienRegistry.register(Vandal())
AlienRegistry.register(Wraith())
AlienRegistry.register(Xenophobe())
AlienRegistry.register(Yogi())
AlienRegistry.register(Zealot())
