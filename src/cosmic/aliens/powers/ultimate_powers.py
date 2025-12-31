"""
Ultimate alien powers for Cosmic Encounter.
Adding 25 more unique powers.
"""

from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Catalyst(AlienPower):
    """
    Catalyst - Amplifies losses.
    When you win, the loser loses double ships to the warp.
    """
    name: str = field(default="Catalyst", init=False)
    description: str = field(default="Losers lose double ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Arcane(AlienPower):
    """
    Arcane - Mystic foresight.
    You may look at the top 3 cards of the deck during planning.
    """
    name: str = field(default="Arcane", init=False)
    description: str = field(default="See top 3 deck cards during planning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Banshee(AlienPower):
    """
    Banshee - Wailing cry.
    When you lose, opponent discards a card from their hand.
    """
    name: str = field(default="Banshee", init=False)
    description: str = field(default="Loser makes opponent discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chronos(AlienPower):
    """
    Chronos - Time manipulation.
    Once per encounter, you may redo your card selection.
    """
    name: str = field(default="Chronos", init=False)
    description: str = field(default="Redo card selection once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Diplomat(AlienPower):
    """
    Diplomat - Diplomatic immunity.
    Your negotiates count as Attack 10 against attacks.
    """
    name: str = field(default="Diplomat", init=False)
    description: str = field(default="Negotiates are Attack 10 vs attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Elemental(AlienPower):
    """
    Elemental - Power of nature.
    Add +2 to your total for each colony you have on foreign planets.
    """
    name: str = field(default="Elemental", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", current_total: int, side: Side) -> int:
        if not player.power_active:
            return current_total
        colonies = player.count_foreign_colonies(game.planets)
        return current_total + (colonies * 2)


@dataclass
class Forge(AlienPower):
    """
    Forge - Victory spoils.
    After winning, you may draw an extra card from the deck.
    """
    name: str = field(default="Forge", init=False)
    description: str = field(default="Draw extra card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(self, game: "Game", player: "Player", as_main: bool) -> None:
        if not player.power_active:
            return
        card = game.cosmic_deck.draw()
        player.add_card(card)


@dataclass
class Gremlin(AlienPower):
    """
    Gremlin - Saboteur.
    Opponents' reinforcement cards add to your total instead.
    """
    name: str = field(default="Gremlin", init=False)
    description: str = field(default="Steal opponent reinforcements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Herald(AlienPower):
    """
    Herald - Rally cry.
    Allies joining your side commit +1 extra ship.
    """
    name: str = field(default="Herald", init=False)
    description: str = field(default="Allies commit +1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Illusionist(AlienPower):
    """
    Illusionist - Deceptive.
    Your attack card appears as a different value until reveal.
    """
    name: str = field(default="Illusionist", init=False)
    description: str = field(default="Hide your card's true value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Juggernaut(AlienPower):
    """
    Juggernaut - Unstoppable force.
    Add +1 to your total for each ship you have in the warp.
    """
    name: str = field(default="Juggernaut", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", current_total: int, side: Side) -> int:
        if not player.power_active:
            return current_total
        return current_total + player.ships_in_warp


@dataclass
class KeeperPower(AlienPower):
    """
    Keeper - Card hoarder.
    When you would discard an encounter card, keep it instead.
    """
    name: str = field(default="Keeper", init=False)
    description: str = field(default="Keep discarded encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Legion(AlienPower):
    """
    Legion - Overwhelming force.
    You may commit up to 6 ships per encounter instead of 4.
    """
    name: str = field(default="Legion", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mystic(AlienPower):
    """
    Mystic - Seer.
    Once per turn, predict the destiny card - if correct, gain a colony.
    """
    name: str = field(default="Mystic", init=False)
    description: str = field(default="Predict destiny for colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Noble(AlienPower):
    """
    Noble - Commanding presence.
    Other players must accept your alliance invitations.
    """
    name: str = field(default="Noble", init=False)
    description: str = field(default="Forced alliance acceptance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class OraclePower(AlienPower):
    """
    Oracle - Prescient.
    Look at opponent's encounter card before selecting yours.
    """
    name: str = field(default="Oracle", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Phantom(AlienPower):
    """
    Phantom - Ethereal.
    Your ships don't go to the warp, they return to colonies.
    """
    name: str = field(default="Phantom", init=False)
    description: str = field(default="Ships return to colonies, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", ship_count: int, reason: str) -> int:
        if not player.power_active:
            return ship_count
        # Return ships to colonies instead
        player.return_ships_to_colonies(ship_count, player.home_planets)
        return 0


@dataclass
class QuartermasterPower(AlienPower):
    """
    Quartermaster - Supply officer.
    Draw a card whenever you retrieve ships from the warp.
    """
    name: str = field(default="Quartermaster", init=False)
    description: str = field(default="Draw card when retrieving ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ravager(AlienPower):
    """
    Ravager - Destructive force.
    When you win as offense, send defender's ships on other planets to warp.
    """
    name: str = field(default="Ravager", init=False)
    description: str = field(default="Destroy defender's other ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class SentinelPower(AlienPower):
    """
    Sentinel - Guardian.
    Add +4 to defense when defending your home planets.
    """
    name: str = field(default="Sentinel", init=False)
    description: str = field(default="+4 defense on home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", current_total: int, side: Side) -> int:
        if not player.power_active or side != Side.DEFENSE:
            return current_total
        if game.defense == player and game.defense_planet in player.home_planets:
            return current_total + 4
        return current_total


@dataclass
class Tempest(AlienPower):
    """
    Tempest - Storm bringer.
    Once per encounter, force a player to discard and redraw their hand.
    """
    name: str = field(default="Tempest", init=False)
    description: str = field(default="Force hand redraw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Usurper(AlienPower):
    """
    Usurper - Power grabber.
    When you win with a negotiate, gain 2 colonies instead of 1.
    """
    name: str = field(default="Usurper", init=False)
    description: str = field(default="Double negotiate colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class VanguardPower(AlienPower):
    """
    Vanguard - First strike.
    You attack first - if you would win, opponent doesn't play a card.
    """
    name: str = field(default="Vanguard", init=False)
    description: str = field(default="Attack first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wrath(AlienPower):
    """
    Wrath - Vengeful.
    When you lose as defense, the offense loses 2 ships to the warp.
    """
    name: str = field(default="Wrath", init=False)
    description: str = field(default="Offense loses 2 ships when you lose defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main: bool) -> None:
        if not as_main or not player.power_active:
            return
        if game.defense == player and game.offense:
            game.offense.send_ships_to_warp(min(2, game.offense.total_ships_in_play(game.planets)))


@dataclass
class Zealot(AlienPower):
    """
    Zealot - Fanatical.
    Your morph cards copy the highest attack card played this game.
    """
    name: str = field(default="Zealot", init=False)
    description: str = field(default="Morph copies best attack ever.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Catalyst())
AlienRegistry.register(Arcane())
AlienRegistry.register(Banshee())
AlienRegistry.register(Chronos())
AlienRegistry.register(Diplomat())
AlienRegistry.register(Elemental())
AlienRegistry.register(Forge())
AlienRegistry.register(Gremlin())
AlienRegistry.register(Herald())
AlienRegistry.register(Illusionist())
AlienRegistry.register(Juggernaut())
AlienRegistry.register(KeeperPower())
AlienRegistry.register(Legion())
AlienRegistry.register(Mystic())
AlienRegistry.register(Noble())
AlienRegistry.register(OraclePower())
AlienRegistry.register(Phantom())
AlienRegistry.register(QuartermasterPower())
AlienRegistry.register(Ravager())
AlienRegistry.register(SentinelPower())
AlienRegistry.register(Tempest())
AlienRegistry.register(Usurper())
AlienRegistry.register(VanguardPower())
AlienRegistry.register(Wrath())
AlienRegistry.register(Zealot())
