"""
Tech Deck - Technology cards from Cosmic Incursion expansion.

Tech cards represent advanced technologies that players can research.
Each tech has a research cost and provides an ongoing benefit once completed.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from enum import Enum, auto

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


class TechCategory(Enum):
    """Categories of tech cards."""
    COMBAT = auto()      # Improves combat ability
    ECONOMY = auto()     # Card draw and resource generation
    DEFENSE = auto()     # Defensive benefits
    MOVEMENT = auto()    # Ship manipulation
    SPECIAL = auto()     # Unique effects


@dataclass
class TechCard:
    """
    A technology card that can be researched.

    research_cost: Number of successful encounters to complete research
    effect_description: Description of what the tech does
    category: Type of technology
    """
    name: str
    research_cost: int
    effect_description: str
    category: TechCategory
    is_researched: bool = False
    research_progress: int = 0
    owner: Optional["Player"] = None

    def __str__(self) -> str:
        status = "Complete" if self.is_researched else f"{self.research_progress}/{self.research_cost}"
        return f"Tech: {self.name} [{status}]"

    def add_research(self, amount: int = 1) -> bool:
        """
        Add research progress. Returns True if research is now complete.
        """
        if self.is_researched:
            return True
        self.research_progress += amount
        if self.research_progress >= self.research_cost:
            self.is_researched = True
            return True
        return False

    def reset(self) -> None:
        """Reset tech to unresearched state."""
        self.is_researched = False
        self.research_progress = 0
        self.owner = None


# Combat tech effects
TECH_EFFECTS: Dict[str, Dict[str, Any]] = {
    # Combat Technologies
    "Plasma Thruster": {
        "category": TechCategory.COMBAT,
        "cost": 2,
        "description": "+2 to your attack total in encounters.",
        "combat_bonus": 2
    },
    "Stellar Shield": {
        "category": TechCategory.DEFENSE,
        "cost": 2,
        "description": "+2 to your defense total in encounters.",
        "defense_bonus": 2
    },
    "Omega Missile": {
        "category": TechCategory.COMBAT,
        "cost": 3,
        "description": "+4 to your attack total when you have 4 ships.",
        "conditional_bonus": {"ships": 4, "bonus": 4}
    },
    "Neutron Bomb": {
        "category": TechCategory.COMBAT,
        "cost": 4,
        "description": "When you win, send all opponent ships to warp (not colonies).",
        "devastate": True
    },

    # Economy Technologies
    "Genesis Device": {
        "category": TechCategory.ECONOMY,
        "cost": 3,
        "description": "Draw 2 cards at the start of your turn.",
        "turn_draw": 2
    },
    "Replicator": {
        "category": TechCategory.ECONOMY,
        "cost": 2,
        "description": "When you draw cards, draw 1 extra card.",
        "extra_draw": 1
    },
    "Quantum Factory": {
        "category": TechCategory.ECONOMY,
        "cost": 3,
        "description": "At start of turn, you may discard 2 cards to draw 3.",
        "card_exchange": {"discard": 2, "draw": 3}
    },
    "Trade Hub": {
        "category": TechCategory.ECONOMY,
        "cost": 2,
        "description": "When making a deal, both players draw 1 card.",
        "deal_bonus": 1
    },

    # Defense Technologies
    "Force Wall": {
        "category": TechCategory.DEFENSE,
        "cost": 3,
        "description": "When defending, opponent allies provide only half ships (round up).",
        "ally_reduction": 0.5
    },
    "Warp Stabilizer": {
        "category": TechCategory.DEFENSE,
        "cost": 2,
        "description": "Once per encounter, return 1 ship from warp to colonies.",
        "warp_recovery": 1
    },
    "Regeneration Matrix": {
        "category": TechCategory.DEFENSE,
        "cost": 4,
        "description": "Ships lost as offense return to colonies instead of warp.",
        "prevent_warp": True
    },
    "Disruption Field": {
        "category": TechCategory.DEFENSE,
        "cost": 3,
        "description": "Cancel one artifact played against you per encounter.",
        "artifact_immunity": True
    },

    # Movement Technologies
    "Warp Gate": {
        "category": TechCategory.MOVEMENT,
        "cost": 2,
        "description": "Ships from any colony may join your encounters.",
        "universal_launch": True
    },
    "Gravity Well": {
        "category": TechCategory.MOVEMENT,
        "cost": 3,
        "description": "Your allies may commit up to 5 ships.",
        "ally_ships_max": 5
    },
    "Phase Shifter": {
        "category": TechCategory.MOVEMENT,
        "cost": 3,
        "description": "When retreating, ships go to any colony, not just home.",
        "retreat_anywhere": True
    },
    "Hyperspace Drive": {
        "category": TechCategory.MOVEMENT,
        "cost": 4,
        "description": "Take 3 encounters per turn instead of 2.",
        "extra_encounter": True
    },

    # Special Technologies
    "Temporal Flux": {
        "category": TechCategory.SPECIAL,
        "cost": 4,
        "description": "Once per game, take an extra turn.",
        "extra_turn": True,
        "one_use": True
    },
    "Mind Scanner": {
        "category": TechCategory.SPECIAL,
        "cost": 2,
        "description": "Look at opponent's hand before each encounter.",
        "see_hand": True
    },
    "Power Amplifier": {
        "category": TechCategory.SPECIAL,
        "cost": 3,
        "description": "Your alien power cannot be zapped or negated.",
        "power_protection": True
    },
    "Cloak Generator": {
        "category": TechCategory.SPECIAL,
        "cost": 2,
        "description": "Opponent reveals card first in encounters.",
        "reveal_first": True
    },
    "Null Field": {
        "category": TechCategory.SPECIAL,
        "cost": 3,
        "description": "Opponent's alien power is disabled against you.",
        "disable_power": True
    },
    "Victory Core": {
        "category": TechCategory.SPECIAL,
        "cost": 5,
        "description": "Need only 4 colonies to win instead of 5.",
        "reduced_win": 4
    }
}


@dataclass
class TechDeck:
    """
    The technology deck containing all available tech cards.
    """
    draw_pile: List[TechCard] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if not self.draw_pile:
            self._initialize_deck()
            self.shuffle()

    def _initialize_deck(self) -> None:
        """Create all technology cards."""
        for name, data in TECH_EFFECTS.items():
            tech = TechCard(
                name=name,
                research_cost=data["cost"],
                effect_description=data["description"],
                category=data["category"]
            )
            self.draw_pile.append(tech)

    def shuffle(self) -> None:
        """Shuffle the tech deck."""
        self._rng.shuffle(self.draw_pile)

    def draw(self) -> Optional[TechCard]:
        """Draw a tech card from the deck."""
        if not self.draw_pile:
            return None
        return self.draw_pile.pop()

    def draw_multiple(self, count: int) -> List[TechCard]:
        """Draw multiple tech cards."""
        cards = []
        for _ in range(count):
            card = self.draw()
            if card:
                cards.append(card)
        return cards

    def return_card(self, tech: TechCard) -> None:
        """Return a tech card to the bottom of the deck."""
        tech.reset()
        self.draw_pile.insert(0, tech)

    def cards_remaining(self) -> int:
        """Number of tech cards remaining."""
        return len(self.draw_pile)

    def set_rng(self, rng: random.Random) -> None:
        """Set random number generator for reproducibility."""
        self._rng = rng


@dataclass
class PlayerTechState:
    """
    Tracks a player's technology research state.
    """
    current_research: Optional[TechCard] = None
    completed_techs: List[TechCard] = field(default_factory=list)
    available_techs: List[TechCard] = field(default_factory=list)

    def start_research(self, tech: TechCard) -> bool:
        """
        Start researching a tech. Returns False if already researching.
        """
        if self.current_research is not None:
            return False
        if tech in self.completed_techs:
            return False
        self.current_research = tech
        return True

    def add_research_progress(self, amount: int = 1) -> Optional[TechCard]:
        """
        Add research progress. Returns the completed tech if finished.
        """
        if self.current_research is None:
            return None

        if self.current_research.add_research(amount):
            completed = self.current_research
            self.completed_techs.append(completed)
            self.current_research = None
            return completed
        return None

    def abandon_research(self) -> Optional[TechCard]:
        """Abandon current research. Returns the abandoned tech."""
        if self.current_research is None:
            return None
        abandoned = self.current_research
        self.current_research = None
        return abandoned

    def has_tech(self, tech_name: str) -> bool:
        """Check if player has completed a specific tech."""
        return any(t.name == tech_name for t in self.completed_techs)

    def get_combat_bonus(self, is_offense: bool, ship_count: int = 0) -> int:
        """Calculate total combat bonus from all completed techs."""
        bonus = 0
        for tech in self.completed_techs:
            effect = TECH_EFFECTS.get(tech.name, {})

            if is_offense and "combat_bonus" in effect:
                bonus += effect["combat_bonus"]

            if not is_offense and "defense_bonus" in effect:
                bonus += effect["defense_bonus"]

            # Conditional bonuses
            if "conditional_bonus" in effect:
                cond = effect["conditional_bonus"]
                if ship_count >= cond.get("ships", 0):
                    bonus += cond["bonus"]

        return bonus

    def get_extra_draw(self) -> int:
        """Get extra cards to draw from techs."""
        extra = 0
        for tech in self.completed_techs:
            effect = TECH_EFFECTS.get(tech.name, {})
            extra += effect.get("extra_draw", 0)
        return extra

    def has_power_protection(self) -> bool:
        """Check if player's power is protected from zapping."""
        for tech in self.completed_techs:
            effect = TECH_EFFECTS.get(tech.name, {})
            if effect.get("power_protection"):
                return True
        return False

    def get_reduced_win_condition(self) -> int:
        """Get modified win condition (colonies needed)."""
        for tech in self.completed_techs:
            effect = TECH_EFFECTS.get(tech.name, {})
            if "reduced_win" in effect:
                return effect["reduced_win"]
        return 5  # Default

    def __str__(self) -> str:
        lines = []
        if self.current_research:
            lines.append(f"Researching: {self.current_research}")
        if self.completed_techs:
            lines.append(f"Completed: {[t.name for t in self.completed_techs]}")
        return " | ".join(lines) if lines else "No tech"
