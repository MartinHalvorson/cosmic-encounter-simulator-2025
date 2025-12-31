"""
Rift Cards (Cosmic Odyssey expansion).

Rifts are special reward deck cards that create traps and surprise effects:
- When drawn as rewards, they can free ships from warp
- When taken from another player's hand, they trigger against the taker
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING
from enum import Enum

from .base import Card, CardType

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


class RiftType(Enum):
    """Types of Rift cards."""
    WARP_RIFT = "warp_rift"       # Free ships from warp when drawn
    TRAP_RIFT = "trap_rift"       # Sends taker's ships to warp
    MIRROR_RIFT = "mirror_rift"   # Reflects effect back
    VOID_RIFT = "void_rift"       # Removes ships from game
    TIME_RIFT = "time_rift"       # Allows replay of encounter


@dataclass
class RiftCard(Card):
    """
    A Rift card from the Cosmic Odyssey expansion.

    Rifts have two modes:
    1. When drawn normally: benefit the drawer
    2. When stolen/taken: hurt the taker (booby trap)
    """
    card_type: CardType = field(default=CardType.ARTIFACT, init=False)
    rift_type: RiftType = RiftType.WARP_RIFT
    ships_affected: int = 2  # How many ships are affected

    def is_encounter_card(self) -> bool:
        return False

    @property
    def name(self) -> str:
        return f"{self.rift_type.value}_rift"

    def __str__(self) -> str:
        return f"Rift ({self.rift_type.name}, {self.ships_affected} ships)"

    def on_draw(self, game: "Game", player: "Player") -> str:
        """
        Effect when drawn normally (as reward).
        Generally beneficial to the player.
        """
        effect = ""

        if self.rift_type == RiftType.WARP_RIFT:
            # Free ships from warp
            retrieved = player.retrieve_ships_from_warp(self.ships_affected)
            if retrieved > 0:
                player.return_ships_to_colonies(retrieved, player.home_planets)
                effect = f"{player.name} frees {retrieved} ships from warp via Rift!"

        elif self.rift_type == RiftType.TRAP_RIFT:
            # When drawn normally, no immediate effect - stays in hand as trap
            effect = f"{player.name} draws a Trap Rift (will harm anyone who takes it)"

        elif self.rift_type == RiftType.MIRROR_RIFT:
            # Stays in hand - reflects next attack
            effect = f"{player.name} draws a Mirror Rift (protects against next power)"

        elif self.rift_type == RiftType.VOID_RIFT:
            # Dangerous - player may choose to discard
            effect = f"{player.name} draws a Void Rift (handle with care!)"

        elif self.rift_type == RiftType.TIME_RIFT:
            # Powerful - allows encounter replay
            effect = f"{player.name} draws a Time Rift (can replay an encounter)"

        return effect

    def on_stolen(self, game: "Game", thief: "Player", victim: "Player") -> str:
        """
        Effect when card is stolen/taken from another player.
        Generally harmful to the thief.
        """
        effect = ""

        if self.rift_type == RiftType.WARP_RIFT:
            # Reverses - sends thief's ships to warp
            ships_to_warp = min(self.ships_affected, thief.total_ships_in_play(game.planets))
            if ships_to_warp > 0:
                thief.get_ships_from_colonies(ships_to_warp, game.planets)
                thief.send_ships_to_warp(ships_to_warp)
                effect = f"Warp Rift traps {thief.name}! {ships_to_warp} ships sent to warp!"

        elif self.rift_type == RiftType.TRAP_RIFT:
            # Full damage
            ships_to_warp = self.ships_affected + 1  # Traps are worse
            actual = min(ships_to_warp, thief.total_ships_in_play(game.planets))
            if actual > 0:
                thief.get_ships_from_colonies(actual, game.planets)
                thief.send_ships_to_warp(actual)
                effect = f"Trap Rift springs on {thief.name}! {actual} ships sent to warp!"

        elif self.rift_type == RiftType.MIRROR_RIFT:
            # Reflects - thief gives victim cards
            cards_to_give = min(2, thief.hand_size())
            if cards_to_give > 0:
                for _ in range(cards_to_give):
                    if thief.hand:
                        card = thief.hand.pop()
                        victim.add_card(card)
                effect = f"Mirror Rift reflects! {thief.name} gives {cards_to_give} cards to {victim.name}!"

        elif self.rift_type == RiftType.VOID_RIFT:
            # Most dangerous - ships removed from game entirely
            ships_lost = min(1, thief.total_ships_in_play(game.planets))
            if ships_lost > 0:
                thief.get_ships_from_colonies(ships_lost, game.planets, exclude_last_ship=False)
                # Ships are voided, not sent to warp
                effect = f"Void Rift activates! {thief.name} loses {ships_lost} ship(s) permanently!"

        elif self.rift_type == RiftType.TIME_RIFT:
            # Thief loses a turn
            effect = f"Time Rift disrupts {thief.name}'s timeline! (loses next turn)"

        return effect


class RiftDeck:
    """
    Manages the Rift cards for a game.
    Rifts are typically shuffled into the Rewards deck.
    """

    @staticmethod
    def create_standard_rifts() -> List[RiftCard]:
        """Create the standard set of Rift cards."""
        rifts = [
            # 4 Warp Rifts (most common, moderate effect)
            RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=2),
            RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=2),
            RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=3),
            RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=3),

            # 3 Trap Rifts (defensive booby traps)
            RiftCard(rift_type=RiftType.TRAP_RIFT, ships_affected=2),
            RiftCard(rift_type=RiftType.TRAP_RIFT, ships_affected=3),
            RiftCard(rift_type=RiftType.TRAP_RIFT, ships_affected=4),

            # 2 Mirror Rifts (reflect effects)
            RiftCard(rift_type=RiftType.MIRROR_RIFT, ships_affected=2),
            RiftCard(rift_type=RiftType.MIRROR_RIFT, ships_affected=2),

            # 1 Void Rift (most dangerous)
            RiftCard(rift_type=RiftType.VOID_RIFT, ships_affected=1),

            # 2 Time Rifts (powerful utility)
            RiftCard(rift_type=RiftType.TIME_RIFT, ships_affected=1),
            RiftCard(rift_type=RiftType.TIME_RIFT, ships_affected=1),
        ]
        return rifts


def is_rift_card(card: Card) -> bool:
    """Check if a card is a Rift card."""
    return isinstance(card, RiftCard)


def handle_card_taken(
    game: "Game",
    card: Card,
    thief: "Player",
    victim: "Player"
) -> Optional[str]:
    """
    Handle when a card is taken from one player by another.
    If it's a Rift, trigger the trap effect.
    """
    if isinstance(card, RiftCard):
        return card.on_stolen(game, thief, victim)
    return None
