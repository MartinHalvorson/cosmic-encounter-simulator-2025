"""
Economy themed alien powers for Cosmic Encounter.

Powers themed around resources, trade, wealth, and economic concepts.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# WEALTH ACCUMULATION
# ============================================================================

@dataclass
class Miser(AlienPower):
    """Miser - Power of Hoarding. Bonus for large hand."""
    name: str = field(default="Miser", init=False)
    description: str = field(default="+1 per 2 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (len(player.hand) // 2)
        return base_total


@dataclass
class Tycoon(AlienPower):
    """Tycoon - Power of Empire. +2 per home colony."""
    name: str = field(default="Tycoon", init=False)
    description: str = field(default="+2 per home planet colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in game.planets
                               if p.owner == player and p.has_colony(player.name))
            return base_total + (home_colonies * 2)
        return base_total


@dataclass
class Mogul(AlienPower):
    """Mogul - Power of Influence. Draw extra cards on win."""
    name: str = field(default="Mogul", init=False)
    description: str = field(default="Draw 2 extra cards when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Investor(AlienPower):
    """Investor - Power of Growth. Cards accumulate value."""
    name: str = field(default="Investor", init=False)
    description: str = field(default="+1 per card with value 10+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            high_cards = sum(1 for c in player.hand if hasattr(c, 'value') and c.value >= 10)
            return base_total + high_cards
        return base_total


# ============================================================================
# TRADE AND COMMERCE
# ============================================================================

@dataclass
class Merchant(AlienPower):
    """Merchant - Power of Trade. Exchange cards for benefits."""
    name: str = field(default="Merchant", init=False)
    description: str = field(default="Discard 1 card: +3 to encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Broker(AlienPower):
    """Broker - Power of Deals. Profit from negotiations."""
    name: str = field(default="Broker", init=False)
    description: str = field(default="Draw 1 card whenever players negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smuggler(AlienPower):
    """Smuggler - Power of Contraband. Hidden advantages."""
    name: str = field(default="Smuggler", init=False)
    description: str = field(default="Play cards face-down. Reveal after opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Auctioneer(AlienPower):
    """Auctioneer - Power of Bidding. Cards go to highest bidder."""
    name: str = field(default="Auctioneer", init=False)
    description: str = field(default="Highest card played takes both.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# RESOURCES AND PRODUCTION
# ============================================================================

@dataclass
class Miner(AlienPower):
    """Miner - Power of Extraction. Draw from bottom of deck."""
    name: str = field(default="Miner", init=False)
    description: str = field(default="Draw from bottom of deck instead of top.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Farmer(AlienPower):
    """Farmer - Power of Growth. Ships grow on home planets."""
    name: str = field(default="Farmer", init=False)
    description: str = field(default="Add 1 ship to home planets each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Manufacturer(AlienPower):
    """Manufacturer - Power of Production. Build ships faster."""
    name: str = field(default="Manufacturer", init=False)
    description: str = field(default="Retrieve 2 ships from warp instead of 1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Refiner(AlienPower):
    """Refiner - Power of Processing. Improve cards."""
    name: str = field(default="Refiner", init=False)
    description: str = field(default="Your attack cards are +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


# ============================================================================
# BANKING AND FINANCE
# ============================================================================

@dataclass
class Banker(AlienPower):
    """Banker - Power of Savings. Store cards for later."""
    name: str = field(default="Banker", init=False)
    description: str = field(default="Set aside up to 3 cards. Retrieve any time.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    saved_cards: List = field(default_factory=list)


@dataclass
class Lender(AlienPower):
    """Lender - Power of Loans. Temporary strength boost."""
    name: str = field(default="Lender", init=False)
    description: str = field(default="+5 now, but -3 next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    debt_active: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if self.debt_active:
            self.debt_active = False
            return base_total - 3
        if random.random() < 0.5:
            self.debt_active = True
            return base_total + 5
        return base_total


@dataclass
class Taxer(AlienPower):
    """Taxer - Power of Collection. Take from losers."""
    name: str = field(default="Taxer", init=False)
    description: str = field(default="Draw 1 card from losing side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Insurer(AlienPower):
    """Insurer - Power of Protection. Reduce losses."""
    name: str = field(default="Insurer", init=False)
    description: str = field(default="Lose only half ships (rounded up) on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# MARKET DYNAMICS
# ============================================================================

@dataclass
class Speculator(AlienPower):
    """Speculator - Power of Risk. Double or nothing."""
    name: str = field(default="Speculator", init=False)
    description: str = field(default="Flip coin: win = +8, lose = -4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and random.random() < 0.3:
            if random.random() < 0.5:
                return base_total + 8
            else:
                return max(0, base_total - 4)
        return base_total


@dataclass
class Monopolist(AlienPower):
    """Monopolist - Power of Control. Bonus in specific encounters."""
    name: str = field(default="Monopolist", init=False)
    description: str = field(default="+4 when opponent has 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and opponent.count_foreign_colonies(game.planets) >= 3:
            return base_total + 4
        return base_total


@dataclass
class Competitor(AlienPower):
    """Competitor - Power of Rivalry. Bonus vs leading player."""
    name: str = field(default="Competitor", init=False)
    description: str = field(default="+5 vs player with most colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Entrepreneur(AlienPower):
    """Entrepreneur - Power of Innovation. Unique advantages."""
    name: str = field(default="Entrepreneur", init=False)
    description: str = field(default="+3 on first attack each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all economy powers
ECONOMY_POWERS = [
    Miser, Tycoon, Mogul, Investor,
    Merchant, Broker, Smuggler, Auctioneer,
    Miner, Farmer, Manufacturer, Refiner,
    Banker, Lender, Taxer, Insurer,
    Speculator, Monopolist, Competitor, Entrepreneur,
]


# Auto-register all powers
for power_class in ECONOMY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
