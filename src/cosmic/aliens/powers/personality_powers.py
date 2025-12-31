"""
Personality themed alien powers for Cosmic Encounter.

Powers based on personality traits and psychological characteristics.
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
# CONFIDENT PERSONALITIES
# ============================================================================

@dataclass
class Optimist(AlienPower):
    """Optimist - Power of Hope. Bonus when behind."""
    name: str = field(default="Optimist", init=False)
    description: str = field(default="+4 when you have fewer colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            if my_colonies < opp_colonies:
                return base_total + 4
        return base_total


@dataclass
class Pessimist(AlienPower):
    """Pessimist - Power of Caution. Prepare for worst."""
    name: str = field(default="Pessimist", init=False)
    description: str = field(default="On loss, keep 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Narcissist(AlienPower):
    """Narcissist - Power of Self. Bonus alone."""
    name: str = field(default="Narcissist", init=False)
    description: str = field(default="+5 when you have no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        if allies == 0:
            return base_total + 5
        return base_total


@dataclass
class Humble(AlienPower):
    """Humble - Power of Modesty. Win quietly."""
    name: str = field(default="Humble", init=False)
    description: str = field(default="Winning by less than 5 draws you 2 cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# AGGRESSIVE PERSONALITIES
# ============================================================================

@dataclass
class Hothead(AlienPower):
    """Hothead - Power of Anger. Random bonus."""
    name: str = field(default="Hothead", init=False)
    description: str = field(default="Random +0 to +6 each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(0, 6)
        return base_total


@dataclass
class Stubborn(AlienPower):
    """Stubborn - Power of Persistence. Repeat attacks."""
    name: str = field(default="Stubborn", init=False)
    description: str = field(default="+2 per repeat attack on same player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    attack_count: Dict[str, int] = field(default_factory=dict)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active or side != Side.OFFENSE:
            return base_total
        if game.defense:
            count = self.attack_count.get(game.defense.name, 0)
            self.attack_count[game.defense.name] = count + 1
            return base_total + (count * 2)
        return base_total


@dataclass
class Reckless(AlienPower):
    """Reckless - Power of Abandon. High risk high reward."""
    name: str = field(default="Reckless", init=False)
    description: str = field(default="Commit all available ships. +3 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Vindictive(AlienPower):
    """Vindictive - Power of Revenge. Bonus after losses."""
    name: str = field(default="Vindictive", init=False)
    description: str = field(default="+4 after losing previous encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    lost_last: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and self.lost_last:
            self.lost_last = False
            return base_total + 4
        return base_total


# ============================================================================
# PASSIVE PERSONALITIES
# ============================================================================

@dataclass
class Pacifist(AlienPower):
    """Pacifist - Power of Peace. Bonus for negotiating."""
    name: str = field(default="Pacifist", init=False)
    description: str = field(default="Double rewards from successful negotiations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coward(AlienPower):
    """Coward - Power of Retreat. Escape danger."""
    name: str = field(default="Coward", init=False)
    description: str = field(default="Before reveal, may retreat all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lazy(AlienPower):
    """Lazy - Power of Rest. Conserve effort."""
    name: str = field(default="Lazy", init=False)
    description: str = field(default="May skip encounter. Draw 2 cards instead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Timid(AlienPower):
    """Timid - Power of Shyness. Avoid large conflicts."""
    name: str = field(default="Timid", init=False)
    description: str = field(default="+3 when facing 3 or fewer ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            opp_ships = sum(game.defense_ships.values())
        else:
            opp_ships = sum(game.offense_ships.values())
        if opp_ships <= 3:
            return base_total + 3
        return base_total


# ============================================================================
# SOCIAL PERSONALITIES
# ============================================================================

@dataclass
class Charmer(AlienPower):
    """Charmer - Power of Persuasion. Attract allies."""
    name: str = field(default="Charmer", init=False)
    description: str = field(default="Allies commit +1 ship each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Introvert(AlienPower):
    """Introvert - Power of Solitude. Bonus alone."""
    name: str = field(default="Introvert", init=False)
    description: str = field(default="+4 with no allies on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        if allies == 0:
            return base_total + 4
        return base_total


@dataclass
class Extrovert(AlienPower):
    """Extrovert - Power of Connection. Bonus with allies."""
    name: str = field(default="Extrovert", init=False)
    description: str = field(default="+2 per ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 2)


@dataclass
class Diplomat(AlienPower):
    """Diplomat - Power of Negotiation. Better deals."""
    name: str = field(default="Diplomat", init=False)
    description: str = field(default="Both players gain colony in negotiation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# CUNNING PERSONALITIES
# ============================================================================

@dataclass
class Schemer(AlienPower):
    """Schemer - Power of Plans. See opponent cards."""
    name: str = field(default="Schemer", init=False)
    description: str = field(default="See 2 cards from opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Suspicious(AlienPower):
    """Suspicious - Power of Doubt. Anti-bluff bonus."""
    name: str = field(default="Suspicious", init=False)
    description: str = field(default="+3 when opponent plays negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Paranoid(AlienPower):
    """Paranoid - Power of Distrust. Defense bonus."""
    name: str = field(default="Paranoid", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Trickster(AlienPower):
    """Trickster - Power of Mischief. Random effects."""
    name: str = field(default="Trickster", init=False)
    description: str = field(default="Flip coin: heads +4, tails opponent -4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and random.random() < 0.3:
            if random.random() < 0.5:
                return base_total + 4
        return base_total


# Register all personality powers
PERSONALITY_POWERS = [
    Optimist, Pessimist, Narcissist, Humble,
    Hothead, Stubborn, Reckless, Vindictive,
    Pacifist, Coward, Lazy, Timid,
    Charmer, Introvert, Extrovert, Diplomat,
    Schemer, Suspicious, Paranoid, Trickster,
]


# Auto-register all powers
for power_class in PERSONALITY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
