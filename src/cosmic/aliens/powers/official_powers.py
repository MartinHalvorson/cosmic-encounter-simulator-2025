"""
Official Cosmic Encounter alien powers from Fantasy Flight Games.

Contains all 238 aliens from:
- Base Game (2008): 50 aliens
- Cosmic Incursion (2010): 20 aliens
- Cosmic Conflict (2011): 20 aliens
- Cosmic Alliance (2012): 20 aliens
- Cosmic Storm (2013): 25 aliens
- Cosmic Dominion (2014): 30 aliens
- Cosmic Eons (2016): 30 aliens
- Cosmic Odyssey (2022): 42 aliens (includes alternate versions)
- Promos: 1 alien
"""

from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Expansion
from ..registry import AlienRegistry

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


# =============================================================================
# BASE GAME ALIENS (50)
# =============================================================================

@dataclass
class Amoeba(AlienPower):
    """You have the power to Ooze. As a main player, after alliances are formed,
    you may add up to four ships from any of your other colonies to your side."""
    name: str = field(default="Amoeba", init=False)
    description: str = field(default="Add ships from other colonies to encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Antimatter(AlienPower):
    """You have the power of Negation. As a main player, when totals are compared,
    the lower total wins instead of the higher."""
    name: str = field(default="Antimatter", init=False)
    description: str = field(default="Lower total wins instead of higher.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Barbarian(AlienPower):
    """You have the power to Pillage. As offense, if you lose the encounter,
    you still collect compensation from the defense."""
    name: str = field(default="Barbarian", init=False)
    description: str = field(default="Collect compensation even when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Calculator(AlienPower):
    """You have the power to Calculate. As a main player, before cards are selected,
    you may announce a total. If your announced total matches your final total exactly,
    you automatically win."""
    name: str = field(default="Calculator", init=False)
    description: str = field(default="Win by predicting exact total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Chosen(AlienPower):
    """You have the power of Destiny. As offense, instead of drawing from the destiny
    deck, you may choose any player to have an encounter against."""
    name: str = field(default="Chosen", init=False)
    description: str = field(default="Choose encounter target instead of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Citadel(AlienPower):
    """You have the power to Fortify. As defense, each of your ships on the targeted
    planet counts as two ships."""
    name: str = field(default="Citadel", init=False)
    description: str = field(default="Defending ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Clone(AlienPower):
    """You have the power to Replicate. Whenever you lose an encounter card to the
    discard pile, you may immediately retrieve it to your hand."""
    name: str = field(default="Clone", init=False)
    description: str = field(default="Retrieve encounter cards after playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Cudgel(AlienPower):
    """You have the power to Stun. As a main player, after cards are selected but
    before they are revealed, you may force your opponent to play their lowest
    encounter card instead."""
    name: str = field(default="Cudgel", init=False)
    description: str = field(default="Force opponent to play lowest card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Dictator(AlienPower):
    """You have the power to Oppress. As a main player, you control where your
    allies' ships are placed during the encounter."""
    name: str = field(default="Dictator", init=False)
    description: str = field(default="Control ally ship placement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fido(AlienPower):
    """You have the power to Fetch. Once per encounter, you may retrieve any one
    card from the discard pile and add it to your hand."""
    name: str = field(default="Fido", init=False)
    description: str = field(default="Retrieve card from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Filch(AlienPower):
    """You have the power to Steal. As a main player, before cards are selected,
    you may randomly draw one card from your opponent's hand and add it to yours."""
    name: str = field(default="Filch", init=False)
    description: str = field(default="Steal random card from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fodder(AlienPower):
    """You have the power to Sacrifice. As offense, after cards are revealed,
    you may send any of your ships from the encounter to the warp to add 1 to
    your total for each ship sacrificed."""
    name: str = field(default="Fodder", init=False)
    description: str = field(default="Sacrifice ships for +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Gambler(AlienPower):
    """You have the power to Risk. As a main player, after cards are revealed,
    you may draw a card from the deck. If it's an encounter card, swap it with
    your played card; otherwise, discard it."""
    name: str = field(default="Gambler", init=False)
    description: str = field(default="Risk drawing to replace played card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Grudge(AlienPower):
    """You have the power of Vendetta. Place a grudge token on any player who
    wins an encounter against you. You get +4 against players with grudge tokens."""
    name: str = field(default="Grudge", init=False)
    description: str = field(default="+4 against players who defeated you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Hacker(AlienPower):
    """You have the power to Peek. As a main player, before cards are selected,
    you may look at your opponent's hand and choose which card they must play."""
    name: str = field(default="Hacker", init=False)
    description: str = field(default="See opponent's hand and choose their card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Hate(AlienPower):
    """You have the power of Vengeance. You get +1 for each ship you have lost
    in previous encounters against your current opponent this game."""
    name: str = field(default="Hate", init=False)
    description: str = field(default="+1 per ship lost to current opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Healer(AlienPower):
    """You have the power to Heal. Whenever any player's ships would go to the warp,
    you may prevent up to 3 of them from going, returning them to colonies instead."""
    name: str = field(default="Healer", init=False)
    description: str = field(default="Save ships from going to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Human(AlienPower):
    """You have the power of Humanity. As a main player, you may add 4 to your
    total after encounter cards are revealed."""
    name: str = field(default="Human", init=False)
    description: str = field(default="+4 to encounter total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Kamikaze(AlienPower):
    """You have the power of Self-Destruction. As offense, after alliances are formed,
    you may triple the value of your ships (each counts as 3) but all your ships in
    the encounter go to the warp regardless of outcome."""
    name: str = field(default="Kamikaze", init=False)
    description: str = field(default="Triple ship value but lose them all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Loser(AlienPower):
    """You have the power to Win by Losing. As a main player, if you would lose
    an encounter, you win instead (and vice versa)."""
    name: str = field(default="Loser", init=False)
    description: str = field(default="Win when you would lose, lose when you would win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Machine(AlienPower):
    """You have the power of Continuity. As offense, after winning an encounter,
    you may have another encounter."""
    name: str = field(default="Machine", init=False)
    description: str = field(default="Extra encounter after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Macron(AlienPower):
    """You have the power of Mass. Each of your ships counts as 4 instead of 1.
    You may only have 1-4 ships in any encounter."""
    name: str = field(default="Macron", init=False)
    description: str = field(default="Ships count as 4 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Masochist(AlienPower):
    """You have the power to Enjoy Pain. Whenever you lose ships to the warp,
    draw one card for each ship lost."""
    name: str = field(default="Masochist", init=False)
    description: str = field(default="Draw card per ship sent to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Mind(AlienPower):
    """You have the power of Foresight. As a main player, before cards are selected,
    you may look at your opponent's hand."""
    name: str = field(default="Mind", init=False)
    description: str = field(default="See opponent's hand before selecting.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Mirror(AlienPower):
    """You have the power to Copy. As a main player, you may use your opponent's
    alien power instead of your own for this encounter."""
    name: str = field(default="Mirror", init=False)
    description: str = field(default="Use opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Miser(AlienPower):
    """You have the power to Hoard. Whenever you draw a new hand, you may keep
    one card from your old hand."""
    name: str = field(default="Miser", init=False)
    description: str = field(default="Keep one card when drawing new hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Mite(AlienPower):
    """You have the power of Infection. You cannot ally normally. Instead, before
    alliances, place one of your ships on any planet in the encounter. If your side
    wins, your ship stays; otherwise, it goes to warp."""
    name: str = field(default="Mite", init=False)
    description: str = field(default="Place ship instead of allying normally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Mutant(AlienPower):
    """You have the power to Mutate. Once per encounter, you may discard your hand
    and draw 8 new cards."""
    name: str = field(default="Mutant", init=False)
    description: str = field(default="Discard hand and draw 8 new cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Observer(AlienPower):
    """You have the power to Watch. Whenever you are not a main player or ally,
    you draw one card from the deck."""
    name: str = field(default="Observer", init=False)
    description: str = field(default="Draw card when not in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.NOT_INVOLVED], init=False)


@dataclass
class Oracle(AlienPower):
    """You have the power to Foresee. As a main player, your opponent must play
    their encounter card face-up while yours remains hidden until reveal."""
    name: str = field(default="Oracle", init=False)
    description: str = field(default="Opponent plays card face-up.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Pacifist(AlienPower):
    """You have the power of Peace. As a main player, you automatically win if
    both you and your opponent play negotiate cards."""
    name: str = field(default="Pacifist", init=False)
    description: str = field(default="Win if both players negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Parasite(AlienPower):
    """You have the power to Infest. You may join either side of any encounter
    uninvited, adding your ships to that side."""
    name: str = field(default="Parasite", init=False)
    description: str = field(default="Join any encounter uninvited.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Philanthropist(AlienPower):
    """You have the power to Give. At the start of each encounter, you must give
    one card from your hand to another player. For each card given this way, draw one."""
    name: str = field(default="Philanthropist", init=False)
    description: str = field(default="Must give cards but draw replacements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Reincarnator(AlienPower):
    """You have the power to be Reborn. When you lose your last home colony,
    discard your alien sheet and draw a new one."""
    name: str = field(default="Reincarnator", init=False)
    description: str = field(default="Get new alien when losing last home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Remora(AlienPower):
    """You have the power to Suck. Whenever any player receives cards from the deck
    or as compensation, you receive one card too."""
    name: str = field(default="Remora", init=False)
    description: str = field(default="Get card when others draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Reserve(AlienPower):
    """You have the power to Delay. As a main player, you may call for allies
    before selecting encounter cards."""
    name: str = field(default="Reserve", init=False)
    description: str = field(default="Call allies before selecting cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Shadow(AlienPower):
    """You have the power to Lurk. After encounter cards are revealed, you may
    join the winning side as an ally (even if not invited)."""
    name: str = field(default="Shadow", init=False)
    description: str = field(default="Join winning side after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Sorcerer(AlienPower):
    """You have the power to Switch. As a main player, after cards are selected
    but before reveal, you may switch encounter cards with your opponent."""
    name: str = field(default="Sorcerer", init=False)
    description: str = field(default="Switch cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Spiff(AlienPower):
    """You have the power to Crash Land. As offense, when you lose an encounter,
    one of your ships from the gate may land on the targeted planet anyway."""
    name: str = field(default="Spiff", init=False)
    description: str = field(default="Land one ship even when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class TickTock(AlienPower):
    """You have the power of Time. Place 10 tokens on this sheet at game start.
    Remove one each encounter. If reduced to 0 and you have at least one foreign colony,
    you win alone."""
    name: str = field(default="TickTock", init=False)
    description: str = field(default="Win alone after 10 encounters if foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    has_alternate_win: bool = True


@dataclass
class Trader(AlienPower):
    """You have the power to Trade. As a main player, before cards are selected,
    you may swap hands with any other player."""
    name: str = field(default="Trader", init=False)
    description: str = field(default="Swap hands with any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Tripler(AlienPower):
    """You have the power to Triple. As a main player, your encounter card value
    is tripled."""
    name: str = field(default="Tripler", init=False)
    description: str = field(default="Triple encounter card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Vacuum(AlienPower):
    """You have the power to Suck In. When you win an encounter, losing ships go
    to your colonies as prisoners instead of the warp."""
    name: str = field(default="Vacuum", init=False)
    description: str = field(default="Capture losing ships as prisoners.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Virus(AlienPower):
    """You have the power to Multiply. As a main player, multiply your encounter
    card value by your number of ships instead of adding them."""
    name: str = field(default="Virus", init=False)
    description: str = field(default="Multiply card by ships instead of adding.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Void(AlienPower):
    """You have the power to Eradicate. When you win an encounter, losing ships
    are removed from the game instead of going to the warp."""
    name: str = field(default="Void", init=False)
    description: str = field(default="Remove losing ships from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Vulch(AlienPower):
    """You have the power to Scrounge. Whenever any player plays an artifact card,
    you may take it for yourself instead of it going to the discard pile."""
    name: str = field(default="Vulch", init=False)
    description: str = field(default="Take played artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Warpish(AlienPower):
    """You have the power of Warp Speed. Ships you have in the warp may be added
    to your side in encounters as if they were in your colonies."""
    name: str = field(default="Warpish", init=False)
    description: str = field(default="Use warp ships in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Warrior(AlienPower):
    """You have the power of the Bonus. For each ship you have in the warp, add
    1 to your total as a main player."""
    name: str = field(default="Warrior", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Will(AlienPower):
    """You have the power of Willpower. As a main player, after encounter cards
    are revealed, you may force both players to play the same card type next encounter."""
    name: str = field(default="Will", init=False)
    description: str = field(default="Force same card type next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Zombie(AlienPower):
    """You have the power of Immortality. Your ships never go to the warp. Instead,
    return them to any of your colonies."""
    name: str = field(default="Zombie", init=False)
    description: str = field(default="Ships return to colonies instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


# =============================================================================
# COSMIC INCURSION ALIENS (20)
# =============================================================================

@dataclass
class Bully(AlienPower):
    """You have the power to Intimidate. As a main player against an opponent with
    fewer ships in the encounter, you may force them to negotiate."""
    name: str = field(default="Bully", init=False)
    description: str = field(default="Force weaker opponent to negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Chronos(AlienPower):
    """You have the power of Time Travel. After an encounter ends, you may undo
    everything and replay the encounter from the start."""
    name: str = field(default="Chronos", init=False)
    description: str = field(default="Replay encounter from start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Cryo(AlienPower):
    """You have the power to Preserve. Ships you lose go to your alien sheet frozen
    instead of the warp. Return them to colonies when you win an encounter."""
    name: str = field(default="Cryo", init=False)
    description: str = field(default="Freeze lost ships, thaw on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Deuce(AlienPower):
    """You have the power of Duality. As a main player, you may play two encounter
    cards and use the total of both."""
    name: str = field(default="Deuce", init=False)
    description: str = field(default="Play two encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Disease(AlienPower):
    """You have the power of Contagion. When you win an encounter, place disease
    tokens on opponent. Each token gives -1 in future encounters."""
    name: str = field(default="Disease", init=False)
    description: str = field(default="Infect opponents with -1 tokens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Ethic(AlienPower):
    """You have the power of Guilt. As a main player, allies on the opposing side
    must give you one card or one ship."""
    name: str = field(default="Ethic", init=False)
    description: str = field(default="Opposing allies pay you tribute.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fungus(AlienPower):
    """You have the power to Adhere. Ships that ally with you remain in the
    encounter for subsequent encounters this turn."""
    name: str = field(default="Fungus", init=False)
    description: str = field(default="Allied ships stick for multiple encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Fury(AlienPower):
    """You have the power of Rage. Each time you lose ships, gain +2 to your
    total for the rest of the game (cumulative)."""
    name: str = field(default="Fury", init=False)
    description: str = field(default="Permanent +2 each time you lose ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Genius(AlienPower):
    """You have the power to Outwit. Before cards are revealed, predict opponent's
    card value. If correct, win automatically."""
    name: str = field(default="Genius", init=False)
    description: str = field(default="Win by predicting opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Ghoul(AlienPower):
    """You have the power to Feast. When ships go to the warp, draw one card from
    the deck for every three ships that went there."""
    name: str = field(default="Ghoul", init=False)
    description: str = field(default="Draw card per 3 ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Guerrilla(AlienPower):
    """You have the power of Attrition. As a main player, before cards are revealed,
    you may send one opposing ship to the warp."""
    name: str = field(default="Guerrilla", init=False)
    description: str = field(default="Send one opposing ship to warp before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Leviathan(AlienPower):
    """You have the power of Worldships. Your home planets can move. As offense,
    you may move one home planet to the targeted system."""
    name: str = field(default="Leviathan", init=False)
    description: str = field(default="Move home planets to other systems.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Locust(AlienPower):
    """You have the power to Devour. When you win an encounter as offense,
    remove the colony - no one can have ships there."""
    name: str = field(default="Locust", init=False)
    description: str = field(default="Destroy planets you conquer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Magician(AlienPower):
    """You have the power of Prestidigitation. As a main player, after reveal,
    make your played card disappear and draw a new one to play instead."""
    name: str = field(default="Magician", init=False)
    description: str = field(default="Replace played card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Mercenary(AlienPower):
    """You have the power of Bounty Hunting. When allying, the main player must
    pay you one card per ship you commit, or you don't ally."""
    name: str = field(default="Mercenary", init=False)
    description: str = field(default="Get paid to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Merchant(AlienPower):
    """You have the power to Trade. Once per encounter, you may buy a card from
    any player for one of your ships (their choice of which card)."""
    name: str = field(default="Merchant", init=False)
    description: str = field(default="Buy cards with ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Plant(AlienPower):
    """You have the power of Grafting. Ships you commit to successful offensive
    encounters stay on the planet as permanent roots, not returning to colonies."""
    name: str = field(default="Plant", init=False)
    description: str = field(default="Establish permanent presence on planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Seeker(AlienPower):
    """You have the power of Truth. Once per encounter, you may ask any player
    a yes/no question about their hand. They must answer honestly."""
    name: str = field(default="Seeker", init=False)
    description: str = field(default="Ask truthful questions about hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Sniveler(AlienPower):
    """You have the power to Whine. At the start of each encounter, if you have
    fewer home colonies than another player, draw two cards."""
    name: str = field(default="Sniveler", init=False)
    description: str = field(default="Draw cards when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Symbiote(AlienPower):
    """You have the power of Bonding. At game start, bond with another player.
    You share colonies - when either wins, both get the benefit."""
    name: str = field(default="Symbiote", init=False)
    description: str = field(default="Share victories with bonded player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


# Register all official powers
_official_powers = [
    # Base Game
    Amoeba, Antimatter, Barbarian, Calculator, Chosen, Citadel, Clone, Cudgel,
    Dictator, Fido, Filch, Fodder, Gambler, Grudge, Hacker, Hate, Healer, Human,
    Kamikaze, Loser, Machine, Macron, Masochist, Mind, Mirror, Miser, Mite, Mutant,
    Observer, Oracle, Pacifist, Parasite, Philanthropist, Reincarnator, Remora,
    Reserve, Shadow, Sorcerer, Spiff, TickTock, Trader, Tripler, Vacuum, Virus,
    Void, Vulch, Warpish, Warrior, Will, Zombie,
    # Cosmic Incursion
    Bully, Chronos, Cryo, Deuce, Disease, Ethic, Fungus, Fury, Genius, Ghoul,
    Guerrilla, Leviathan, Locust, Magician, Mercenary, Merchant, Plant, Seeker,
    Sniveler, Symbiote,
]

for power_class in _official_powers:
    AlienRegistry.register(power_class())
