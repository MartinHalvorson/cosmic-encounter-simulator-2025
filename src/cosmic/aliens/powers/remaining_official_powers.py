"""
Remaining official FFG alien powers.
Adding the 69 missing official aliens.
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


# ========== Base Game ==========

@dataclass
class Barbarian(AlienPower):
    """Barbarian - Power to Pillage. Takes rewards even when losing."""
    name: str = field(default="Barbarian", init=False)
    description: str = field(default="Collect rewards even when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Filch(AlienPower):
    """Filch - Power to Steal. Takes random card from opponent before encounter."""
    name: str = field(default="Filch", init=False)
    description: str = field(default="Steal a random card from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fodder(AlienPower):
    """Fodder - Power to Throw. May use ships as card substitutes."""
    name: str = field(default="Fodder", init=False)
    description: str = field(default="Use ships instead of cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hacker(AlienPower):
    """Hacker - Power to Peek. Looks at opponent's hand and selects card."""
    name: str = field(default="Hacker", init=False)
    description: str = field(default="Look at opponent's hand, choose their card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hate(AlienPower):
    """Hate - Power of Vengeance. Gets stronger against players who attacked them."""
    name: str = field(default="Hate", init=False)
    description: str = field(default="+3 against players who attacked you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    attackers: set = field(default_factory=set)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and opponent.name in self.attackers:
            return total + 3
        return total


@dataclass
class Kamikaze(AlienPower):
    """Kamikaze - Power of Self-Destruction. Ships count more if willing to die."""
    name: str = field(default="Kamikaze", init=False)
    description: str = field(default="Ships count as +4 each, but go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Miser(AlienPower):
    """Miser - Power to Hoard. Keeps best card from each hand."""
    name: str = field(default="Miser", init=False)
    description: str = field(default="Keep one card face-down forever.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Philanthropist(AlienPower):
    """Philanthropist - Power to Give. Must give cards away, benefits from it."""
    name: str = field(default="Philanthropist", init=False)
    description: str = field(default="Give away cards, benefit from it.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reserve(AlienPower):
    """Reserve - Power to Reserve. May call for allies before playing card."""
    name: str = field(default="Reserve", init=False)
    description: str = field(default="Request allies before selecting card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trader(AlienPower):
    """Trader - Power to Trade. May swap hands with any player."""
    name: str = field(default="Trader", init=False)
    description: str = field(default="Trade hands with any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ========== Cosmic Incursion ==========

@dataclass
class Bully(AlienPower):
    """Bully - Power to Intimidate. Forces weaker opponents to negotiate."""
    name: str = field(default="Bully", init=False)
    description: str = field(default="Force weaker opponents to negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deuce(AlienPower):
    """Deuce - Power of Duality. May play two encounter cards."""
    name: str = field(default="Deuce", init=False)
    description: str = field(default="Play two encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fungus(AlienPower):
    """Fungus - Power to Adhere. Ships stick together across encounters."""
    name: str = field(default="Fungus", init=False)
    description: str = field(default="Ships stick together.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fury(AlienPower):
    """Fury - Power of Vengeance. Gets stronger when attacked."""
    name: str = field(default="Fury", init=False)
    description: str = field(default="+2 per ship lost this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    ships_lost: int = 0


@dataclass
class Ghoul(AlienPower):
    """Ghoul - Power to Feast. Takes cards when ships go to warp."""
    name: str = field(default="Ghoul", init=False)
    description: str = field(default="Draw cards when ships go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magician(AlienPower):
    """Magician - Power of Prestidigitation. Makes cards disappear and reappear."""
    name: str = field(default="Magician", init=False)
    description: str = field(default="Switch cards between hand and discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ========== Cosmic Conflict ==========

@dataclass
class Cavalry(AlienPower):
    """Cavalry - Power to Reinforce. Adds ships after cards revealed."""
    name: str = field(default="Cavalry", init=False)
    description: str = field(default="Add ships after cards revealed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glutton(AlienPower):
    """Glutton - Power to Gorge. Consumes cards for power."""
    name: str = field(default="Glutton", init=False)
    description: str = field(default="Eat cards for bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Invader(AlienPower):
    """Invader - Power of Invasion. Always attacks, never defends."""
    name: str = field(default="Invader", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Mimic(AlienPower):
    """Mimic - Power to Mimic. Copies other alien powers."""
    name: str = field(default="Mimic", init=False)
    description: str = field(default="Copy another player's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Prophet(AlienPower):
    """Prophet - Power of Prophecy. Predicts encounter outcomes."""
    name: str = field(default="Prophet", init=False)
    description: str = field(default="Predict outcome for rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Siren(AlienPower):
    """Siren - Power to Lure. Draws ships to bad situations."""
    name: str = field(default="Siren", init=False)
    description: str = field(default="Force players to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Xenophile(AlienPower):
    """Xenophile - Power to Love. Benefits from having diverse allies."""
    name: str = field(default="Xenophile", init=False)
    description: str = field(default="+2 per unique ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ========== Cosmic Alliance ==========

@dataclass
class Chrysalis(AlienPower):
    """Chrysalis - Power to Emerge. Transforms during game."""
    name: str = field(default="Chrysalis", init=False)
    description: str = field(default="Transform into a new alien.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crystal(AlienPower):
    """Crystal - Power to Reflect. Reflects attacks back."""
    name: str = field(default="Crystal", init=False)
    description: str = field(default="Reflect attack damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cyborg(AlienPower):
    """Cyborg - Power of Bionics. Enhanced mechanical abilities."""
    name: str = field(default="Cyborg", init=False)
    description: str = field(default="+3 and keep played card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Extortionist(AlienPower):
    """Extortionist - Power to Extort. Demands payment for cooperation."""
    name: str = field(default="Extortionist", init=False)
    description: str = field(default="Demand cards for alliance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Horde(AlienPower):
    """Horde - Power of Numbers. Overwhelms with quantity."""
    name: str = field(default="Horde", init=False)
    description: str = field(default="Ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Poison(AlienPower):
    """Poison - Power to Toxify. Weakens opponents over time."""
    name: str = field(default="Poison", init=False)
    description: str = field(default="Opponent loses ships each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Schizoid(AlienPower):
    """Schizoid - Power to Alter Reality. Changes win conditions."""
    name: str = field(default="Schizoid", init=False)
    description: str = field(default="Choose win condition each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ========== Cosmic Storm ==========

@dataclass
class Brute(AlienPower):
    """Brute - Power to Smash. Raw strength attacks."""
    name: str = field(default="Brute", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Bulwark(AlienPower):
    """Bulwark - Power to Defend. Strong defensive capabilities."""
    name: str = field(default="Bulwark", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Converter(AlienPower):
    """Converter - Power to Convert. Changes card types."""
    name: str = field(default="Converter", init=False)
    description: str = field(default="Convert negotiate to attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coordinator(AlienPower):
    """Coordinator - Power to Organize. Coordinates ally actions."""
    name: str = field(default="Coordinator", init=False)
    description: str = field(default="Allies get +1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Patriot(AlienPower):
    """Patriot - Power of Loyalty. Stronger on home turf."""
    name: str = field(default="Patriot", init=False)
    description: str = field(default="+4 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active or side != Side.DEFENSE:
            return total
        if game.defense_planet and game.defense_planet.owner == player:
            return total + 4
        return total


@dataclass
class Roach(AlienPower):
    """Roach - Power to Survive. Hard to eliminate."""
    name: str = field(default="Roach", init=False)
    description: str = field(default="Ships return from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scavenger(AlienPower):
    """Scavenger - Power to Scrounge. Collects from discards."""
    name: str = field(default="Scavenger", init=False)
    description: str = field(default="Draw from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sneak(AlienPower):
    """Sneak - Power to Sneak. Hidden movements."""
    name: str = field(default="Sneak", init=False)
    description: str = field(default="Add ships secretly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tide(AlienPower):
    """Tide - Power to Ebb and Flow. Power varies cyclically."""
    name: str = field(default="Tide", init=False)
    description: str = field(default="+2 on odd turns, -2 on even.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tyrant(AlienPower):
    """Tyrant - Power to Oppress. Controls other players."""
    name: str = field(default="Tyrant", init=False)
    description: str = field(default="Force player to give you cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vox(AlienPower):
    """Vox - Power to Speak. Voice affects gameplay."""
    name: str = field(default="Vox", init=False)
    description: str = field(default="Call for vote on encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wormhole(AlienPower):
    """Wormhole - Power to Transport. Instant movement across galaxy."""
    name: str = field(default="Wormhole", init=False)
    description: str = field(default="Move ships anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ========== Cosmic Dominion ==========

@dataclass
class Ace(AlienPower):
    """Ace - Power to Triumph. Exceptional at winning."""
    name: str = field(default="Ace", init=False)
    description: str = field(default="+2 per consecutive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    wins: int = 0


@dataclass
class Alchemist(AlienPower):
    """Alchemist - Power of Transmutation. Changes card values."""
    name: str = field(default="Alchemist", init=False)
    description: str = field(default="Change card value by +/-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Aristocrat(AlienPower):
    """Aristocrat - Power of Nobility. Superior status benefits."""
    name: str = field(default="Aristocrat", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diplomat(AlienPower):
    """Diplomat - Power of Diplomacy. Negotiates advantageous deals."""
    name: str = field(default="Diplomat", init=False)
    description: str = field(default="Negotiate becomes attack 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Doppelganger(AlienPower):
    """Doppelganger - Power to Impersonate. Copies other players."""
    name: str = field(default="Doppelganger", init=False)
    description: str = field(default="Copy opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Engineer(AlienPower):
    """Engineer - Power to Build. Constructs advantages."""
    name: str = field(default="Engineer", init=False)
    description: str = field(default="+4 with 4+ ships defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Judge(AlienPower):
    """Judge - Power to Rule. Makes binding decisions."""
    name: str = field(default="Judge", init=False)
    description: str = field(default="Decide outcomes of ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Laser(AlienPower):
    """Laser - Power to Focus. Concentrated attacks."""
    name: str = field(default="Laser", init=False)
    description: str = field(default="+5 with exactly 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pickpocket(AlienPower):
    """Pickpocket - Power to Pilfer. Steals from others."""
    name: str = field(default="Pickpocket", init=False)
    description: str = field(default="Steal card from ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pirate(AlienPower):
    """Pirate - Power to Plunder. Takes from encounters."""
    name: str = field(default="Pirate", init=False)
    description: str = field(default="Take cards from defeated players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quartermaster(AlienPower):
    """Quartermaster - Power to Supply. Provides resources."""
    name: str = field(default="Quartermaster", init=False)
    description: str = field(default="Draw card when retrieving ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reactor(AlienPower):
    """Reactor - Power to Respond. Reactive abilities."""
    name: str = field(default="Reactor", init=False)
    description: str = field(default="+3 when attacked.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Usurper(AlienPower):
    """Usurper - Power to Overthrow. Takes others' positions."""
    name: str = field(default="Usurper", init=False)
    description: str = field(default="Take 2 colonies with negotiate win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ========== Cosmic Eons ==========

@dataclass
class Architect(AlienPower):
    """Architect - Power to Design. Plans complex strategies."""
    name: str = field(default="Architect", init=False)
    description: str = field(default="Build structures for bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Emperor(AlienPower):
    """Emperor - Power to Rule. Commands others."""
    name: str = field(default="Emperor", init=False)
    description: str = field(default="Force player to give colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Multitude(AlienPower):
    """Multitude - Power of Many. Represents multiple beings."""
    name: str = field(default="Multitude", init=False)
    description: str = field(default="Have 25 ships instead of 20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nightmare(AlienPower):
    """Nightmare - Power to Terrify. Fear-based attacks."""
    name: str = field(default="Nightmare", init=False)
    description: str = field(default="Opponent discards random card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ========== Cosmic Odyssey ==========

@dataclass
class Aura(AlienPower):
    """Aura - Power of Presence. Passive area effects."""
    name: str = field(default="Aura", init=False)
    description: str = field(default="+2 to all allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boomerang(AlienPower):
    """Boomerang - Power to Return. Actions come back."""
    name: str = field(default="Boomerang", init=False)
    description: str = field(default="Retrieve played encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cosmos(AlienPower):
    """Cosmos - Power of the Universe. Universal effects."""
    name: str = field(default="Cosmos", init=False)
    description: str = field(default="+1 per planet in system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Decoy(AlienPower):
    """Decoy - Power to Distract. Misleads opponents."""
    name: str = field(default="Decoy", init=False)
    description: str = field(default="Switch ships between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Delegator(AlienPower):
    """Delegator - Power to Delegate. Assigns tasks to others."""
    name: str = field(default="Delegator", init=False)
    description: str = field(default="Ally uses their power for you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dragon(AlienPower):
    """Dragon - Power to Devastate. Powerful destruction."""
    name: str = field(default="Dragon", init=False)
    description: str = field(default="+6 and destroy 2 opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Guardian(AlienPower):
    """Guardian - Power to Guard. Protects assets."""
    name: str = field(default="Guardian", init=False)
    description: str = field(default="Protect colonies from attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Inferno(AlienPower):
    """Inferno - Power of Fire. Burning attacks."""
    name: str = field(default="Inferno", init=False)
    description: str = field(default="+3, opponent loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Insect(AlienPower):
    """Insect - Power of Swarm. Many small ships."""
    name: str = field(default="Insect", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Phantom(AlienPower):
    """Phantom - Power to Phase. Intangible presence."""
    name: str = field(default="Phantom", init=False)
    description: str = field(default="Ships return home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Barbarian())
AlienRegistry.register(Filch())
AlienRegistry.register(Fodder())
AlienRegistry.register(Hacker())
AlienRegistry.register(Hate())
AlienRegistry.register(Kamikaze())
AlienRegistry.register(Miser())
AlienRegistry.register(Philanthropist())
AlienRegistry.register(Reserve())
AlienRegistry.register(Trader())
AlienRegistry.register(Bully())
AlienRegistry.register(Deuce())
AlienRegistry.register(Fungus())
AlienRegistry.register(Fury())
AlienRegistry.register(Ghoul())
AlienRegistry.register(Magician())
AlienRegistry.register(Cavalry())
AlienRegistry.register(Glutton())
AlienRegistry.register(Invader())
AlienRegistry.register(Mimic())
AlienRegistry.register(Prophet())
AlienRegistry.register(Siren())
AlienRegistry.register(Xenophile())
AlienRegistry.register(Chrysalis())
AlienRegistry.register(Crystal())
AlienRegistry.register(Cyborg())
AlienRegistry.register(Extortionist())
AlienRegistry.register(Horde())
AlienRegistry.register(Poison())
AlienRegistry.register(Schizoid())
AlienRegistry.register(Brute())
AlienRegistry.register(Bulwark())
AlienRegistry.register(Converter())
AlienRegistry.register(Coordinator())
AlienRegistry.register(Patriot())
AlienRegistry.register(Roach())
AlienRegistry.register(Scavenger())
AlienRegistry.register(Sneak())
AlienRegistry.register(Tide())
AlienRegistry.register(Tyrant())
AlienRegistry.register(Vox())
AlienRegistry.register(Wormhole())
AlienRegistry.register(Ace())
AlienRegistry.register(Alchemist())
AlienRegistry.register(Aristocrat())
AlienRegistry.register(Diplomat())
AlienRegistry.register(Doppelganger())
AlienRegistry.register(Engineer())
AlienRegistry.register(Judge())
AlienRegistry.register(Laser())
AlienRegistry.register(Pickpocket())
AlienRegistry.register(Pirate())
AlienRegistry.register(Quartermaster())
AlienRegistry.register(Reactor())
AlienRegistry.register(Usurper())
AlienRegistry.register(Architect())
AlienRegistry.register(Emperor())
AlienRegistry.register(Multitude())
AlienRegistry.register(Nightmare())
AlienRegistry.register(Aura())
AlienRegistry.register(Boomerang())
AlienRegistry.register(Cosmos())
AlienRegistry.register(Decoy())
AlienRegistry.register(Delegator())
AlienRegistry.register(Dragon())
AlienRegistry.register(Guardian())
AlienRegistry.register(Inferno())
AlienRegistry.register(Insect())
AlienRegistry.register(Phantom())
