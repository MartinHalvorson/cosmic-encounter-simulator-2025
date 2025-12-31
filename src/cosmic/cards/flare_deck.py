"""
The Flare Deck - special cards that provide alien power effects.

Each flare card has two effects:
- Wild: Can be used by any player
- Super: Can only be used by a player with the matching alien power
"""

import random
from typing import List, Dict, Optional, TYPE_CHECKING
from dataclasses import dataclass, field

from .base import Card, FlareCard
from ..aliens.registry import AlienRegistry

if TYPE_CHECKING:
    from ..player import Player


@dataclass
class FlareDeck:
    """
    The flare deck contains one flare for each alien in the game.
    Flares are shuffled into the cosmic deck at game start.
    """
    draw_pile: List[FlareCard] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def create_flares_for_game(self, alien_names: List[str]) -> List[FlareCard]:
        """
        Create flare cards for the aliens in the current game.
        Per rules: only include flares for aliens that are in the game.
        """
        flares = []
        for name in alien_names:
            flare = self._create_flare_for_alien(name)
            if flare:
                flares.append(flare)
        return flares

    def _create_flare_for_alien(self, alien_name: str) -> Optional[FlareCard]:
        """Create a flare card for a specific alien."""
        # Get flare effects based on the alien
        effects = FLARE_EFFECTS.get(alien_name)
        if effects:
            return FlareCard(
                alien_name=alien_name,
                wild_effect=effects.get('wild', f"Wild: Gain a minor {alien_name} benefit."),
                super_effect=effects.get('super', f"Super: Gain a major {alien_name} benefit.")
            )
        # Default flare for aliens without specific effects
        return FlareCard(
            alien_name=alien_name,
            wild_effect=f"Wild: Once per encounter, gain +2 to your total.",
            super_effect=f"Super: Once per encounter, gain +4 to your total."
        )

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator for reproducibility."""
        self._rng = rng


# Flare effects for various aliens
# Wild effects are weaker versions usable by anyone
# Super effects are stronger and only usable by the matching alien
FLARE_EFFECTS: Dict[str, Dict[str, str]] = {
    "Machine": {
        "wild": "Wild: Take one extra encounter this turn.",
        "super": "Super: Take two extra encounters this turn."
    },
    "Virus": {
        "wild": "Wild: Add your ships to your total (instead of your opponent adding theirs).",
        "super": "Super: Triple your ship count when adding to total."
    },
    "Zombie": {
        "wild": "Wild: Return 2 ships from the warp to any of your colonies.",
        "super": "Super: Return all your ships from the warp."
    },
    "Oracle": {
        "wild": "Wild: Look at your opponent's encounter card before playing yours.",
        "super": "Super: Look at opponent's card and force them to play a different one."
    },
    "Sorcerer": {
        "wild": "Wild: Swap encounter cards with any player after reveal.",
        "super": "Super: Swap hands with any player."
    },
    "Loser": {
        "wild": "Wild: If you would lose, win instead (once).",
        "super": "Super: Automatically lose the encounter and win."
    },
    "Macron": {
        "wild": "Wild: Your ships count as 2 each this encounter.",
        "super": "Super: Your ships count as 5 each this encounter."
    },
    "Clone": {
        "wild": "Wild: Copy the card you just played from the discard.",
        "super": "Super: Play the same card again without discarding."
    },
    "Trader": {
        "wild": "Wild: Draw 2 cards from the deck.",
        "super": "Super: Trade hands with any player."
    },
    "Pacifist": {
        "wild": "Wild: If you play a Negotiate, add 10 to your total.",
        "super": "Super: If you play a Negotiate and win, gain an extra colony."
    },
    "Human": {
        "wild": "Wild: Add +3 to your total.",
        "super": "Super: Add +6 to your total."
    },
    "Parasite": {
        "wild": "Wild: Join an encounter as an ally without invitation.",
        "super": "Super: Join both sides of an encounter."
    },
    "Warpish": {
        "wild": "Wild: Send 2 opponent ships to the warp.",
        "super": "Super: Send 4 opponent ships to the warp."
    },
    "Symbiote": {
        "wild": "Wild: Double the ships on one of your colonies.",
        "super": "Super: Triple the ships on one of your colonies."
    },
    "Void": {
        "wild": "Wild: Remove one opposing ship from the game (to the void).",
        "super": "Super: Remove all ships from one planet to the void."
    },
    "Assassin": {
        "wild": "Wild: Eliminate 1 opponent ship from the encounter.",
        "super": "Super: Eliminate up to 3 opponent ships from the encounter."
    },
    "Healer": {
        "wild": "Wild: Return 3 ships from any warp to colonies.",
        "super": "Super: Return all ships from the warp to colonies."
    },
    "Warrior": {
        "wild": "Wild: Add +1 for each of your ships in the warp.",
        "super": "Super: Add +2 for each of your ships in the warp."
    },
    "Chosen": {
        "wild": "Wild: Add the top card of the deck to your total.",
        "super": "Super: Add the top 2 cards of the deck to your total."
    },
    "Filch": {
        "wild": "Wild: Steal a random card from one opponent.",
        "super": "Super: Steal 2 cards from one opponent."
    },
    "Gambler": {
        "wild": "Wild: Flip a coin. If heads, double your card value.",
        "super": "Super: Triple your card value on heads, normal on tails."
    },
    "Shadow": {
        "wild": "Wild: Add 2 ships from colonies to the encounter.",
        "super": "Super: Add 4 ships from colonies to the encounter."
    },
    "Tripler": {
        "wild": "Wild: Triple a single digit on your attack card.",
        "super": "Super: Triple your entire attack card value."
    },
    "Spiff": {
        "wild": "Wild: Draw 1 card from the rewards deck.",
        "super": "Super: Draw 2 cards from the rewards deck."
    },
    "Remora": {
        "wild": "Wild: Draw 1 card whenever another player draws.",
        "super": "Super: Draw 2 cards whenever another player draws."
    },
    "Calculator": {
        "wild": "Wild: Increase your card value by the number of cards in your hand.",
        "super": "Super: Double your card value based on cards in hand."
    },
    "Chronos": {
        "wild": "Wild: Take another turn after this one.",
        "super": "Super: Take two additional turns."
    },
    "Disease": {
        "wild": "Wild: Spread 1 of your ships to an opponent's colony.",
        "super": "Super: Spread 2 ships to different opponent colonies."
    },
    "Mutant": {
        "wild": "Wild: Draw 2 cards, keep 1, discard 1.",
        "super": "Super: Draw 4 cards, keep 2, discard 2."
    },
    "Mirror": {
        "wild": "Wild: Reverse the digits of your attack card.",
        "super": "Super: Reverse opponent's attack card digits too."
    },
    "Grudge": {
        "wild": "Wild: Add +3 against a player who attacked you.",
        "super": "Super: Add +6 against any player who has attacked you."
    },
    "Ethic": {
        "wild": "Wild: Force all players to play face-up this encounter.",
        "super": "Super: See all cards before choosing yours."
    },
    "Mite": {
        "wild": "Wild: Look at the top 3 cards of any deck.",
        "super": "Super: Rearrange the top 3 cards of any deck."
    },
    "Negator": {
        "wild": "Wild: Cancel one alien power this encounter.",
        "super": "Super: Cancel all alien powers this encounter."
    },
    "Sniveler": {
        "wild": "Wild: Force one player to give you 1 card.",
        "super": "Super: Force each opponent to give you 1 card."
    },
    "Tick-Tock": {
        "wild": "Wild: Add 1 token to any player's Tick-Tock counter.",
        "super": "Super: Win immediately if you have 10+ tokens."
    },
    "Masochist": {
        "wild": "Wild: Lose 1 ship to gain 1 card.",
        "super": "Super: Lose ships to gain equal cards, then win if you have 0 ships."
    },
    "Reincarnator": {
        "wild": "Wild: Draw a new alien power from the unused pile.",
        "super": "Super: Choose any alien power from the unused pile."
    },
    "Hate": {
        "wild": "Wild: Add +4 against your nemesis.",
        "super": "Super: Add +8 against your nemesis."
    },
    "Phantom": {
        "wild": "Wild: Return lost ships to colonies instead of warp.",
        "super": "Super: Ships never go to warp, always return home."
    },
    "Diplomat": {
        "wild": "Wild: Force a deal to succeed.",
        "super": "Super: Gain 2 colonies from a forced deal."
    },
    "Vulture": {
        "wild": "Wild: Draw 1 card when any ship goes to warp.",
        "super": "Super: Draw 2 cards when any ship goes to warp."
    },
    "Grief": {
        "wild": "Wild: When you lose ships, one opponent loses 1.",
        "super": "Super: When you lose ships, all opponents lose 1 each."
    },
    "Fodder": {
        "wild": "Wild: Sacrifice 1 ship for +2 to total.",
        "super": "Super: Sacrifice any ships for +3 each."
    },
    "Horde": {
        "wild": "Wild: Return 1 ship from warp at encounter start.",
        "super": "Super: Return 2 ships from warp at encounter start."
    },
    "Roach": {
        "wild": "Wild: Return 2 ships when losing last colony.",
        "super": "Super: Return 4 ships when losing last colony."
    },
}
