"""
Personality-based AI strategies for Cosmic Encounter.

These AIs have distinct playstyles that affect their decision-making:
- AggressiveAI: Commits maximum ships, plays highest cards, rarely negotiates
- CautiousAI: Conserves resources, negotiates more, avoids risky encounters
- OpportunisticAI: Allies frequently, targets weak players
- SocialAI: Focuses on alliances and deals over combat
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, TYPE_CHECKING

from .base import AIStrategy

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import EncounterCard
    from ..types import Side


@dataclass
class AggressiveAI(AIStrategy):
    """
    Aggressive AI that maximizes combat power.

    Traits:
    - Always commits maximum ships
    - Plays highest attack cards
    - Rarely negotiates (only when forced)
    - Takes second encounters whenever possible
    - Invites few allies (wants glory alone)
    """
    name: str = field(default="AggressiveAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Always play highest attack card."""
        attack_cards = player.get_attack_cards()
        if attack_cards:
            return max(attack_cards, key=lambda c: c.value)

        # Forced to use other cards
        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Always commit maximum ships."""
        return max_ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Rarely invite allies - want to win alone."""
        # Only invite if we're likely to lose
        hand_strength = self.get_hand_strength(player)
        if hand_strength < 0.3:
            # Invite one ally if desperate
            if potential_allies:
                return [self._rng.choice(potential_allies)]
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Accept offense side for chance to gain colonies."""
        from ..types import Side
        if invited_by_offense:
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit maximum ships as ally too."""
        return max_ships

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack planet with most ships (challenge strongest)."""
        planets = defense.home_planets
        if not planets:
            return None

        return max(
            planets,
            key=lambda p: p.get_ships(defense.name)
        )

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Rarely accept deals - prefer to fight."""
        # Only deal if it's very favorable
        return None

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power if it helps combat."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Always take second encounter if possible."""
        cards = player.get_encounter_cards()
        return len(cards) > 0


@dataclass
class CautiousAI(AIStrategy):
    """
    Cautious AI that conserves resources.

    Traits:
    - Commits minimal ships when possible
    - Saves best cards for important encounters
    - Negotiates when appropriate
    - Avoids risky second encounters
    - Seeks alliances for protection
    """
    name: str = field(default="CautiousAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Play conservatively - don't waste best cards.
        Use negotiate more often.
        """
        cards = player.get_encounter_cards()
        if not cards:
            return None

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        # Consider negotiating more often
        if negotiate_cards:
            hand_strength = self.get_hand_strength(player)
            if hand_strength < 0.4 or (not is_offense and hand_strength < 0.6):
                return negotiate_cards[0]

        if attack_cards:
            # Play 4th or 5th best card - save the good ones
            sorted_cards = sorted(attack_cards, key=lambda c: c.value, reverse=True)
            index = min(3, len(sorted_cards) - 1)
            return sorted_cards[index]

        return cards[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit minimal ships to preserve resources."""
        if max_ships <= 1:
            return max_ships

        # Only commit 1-2 ships usually
        hand_strength = self.get_hand_strength(player)
        if hand_strength > 0.6:
            return 1  # Good hand, don't need many ships
        elif hand_strength > 0.3:
            return 2
        else:
            return 3  # Weak hand, need ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite allies for safety."""
        # Invite up to 2 allies
        count = min(2, len(potential_allies))
        if count > 0:
            return self._rng.sample(potential_allies, count)
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Prefer defense side (less risk, still get rewards)."""
        from ..types import Side
        if invited_by_defense:
            return Side.DEFENSE
        if invited_by_offense:
            # Only join offense if likely to win
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit minimal ships as ally."""
        return 1

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack planet with fewest enemy ships."""
        planets = defense.home_planets
        if not planets:
            return None

        return min(
            planets,
            key=lambda p: p.get_ships(defense.name)
        )

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Accept deals when possible."""
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power only when beneficial and not risky."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Only take second encounter if hand is still strong."""
        cards = player.get_encounter_cards()
        if len(cards) < 3:
            return False
        return self.get_hand_strength(player) > 0.5


@dataclass
class OpportunisticAI(AIStrategy):
    """
    Opportunistic AI that exploits weaknesses.

    Traits:
    - Targets weak players
    - Allies with winning side
    - Adapts card play to situation
    - Takes calculated risks
    """
    name: str = field(default="OpportunisticAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Play just enough to win."""
        cards = player.get_encounter_cards()
        if not cards:
            return None

        attack_cards = player.get_attack_cards()

        if is_offense:
            # Estimate defense strength
            defense_ships = len(game.defense_ships) if game.defense_ships else 4
            # Play card just strong enough to probably win
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                for card in sorted_cards:
                    if card.value + 4 > defense_ships + 10:
                        return card
                return sorted_cards[-1]  # Play highest if none sufficient
        else:
            # Defense: check if worth fighting
            offense_colonies = game.offense.count_foreign_colonies(game.planets)
            if offense_colonies >= 4:
                # Opponent close to winning - fight hard
                if attack_cards:
                    return max(attack_cards, key=lambda c: c.value)

            # Otherwise play medium card
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                mid_index = len(sorted_cards) // 2
                return sorted_cards[mid_index]

        return cards[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit ships based on opponent strength."""
        return max(2, max_ships - 1)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite players with strong hands."""
        invites = []
        for p in potential_allies:
            if len(p.hand) >= 6:  # Has cards to help
                invites.append(p)
            if len(invites) >= 2:
                break
        return invites

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Join the likely winner."""
        from ..types import Side

        # Estimate who will win based on colonies and hand size
        offense_strength = (
            offense.count_foreign_colonies(game.planets) +
            len(offense.hand) * 0.3
        )
        defense_strength = (
            defense.count_foreign_colonies(game.planets) +
            len(defense.hand) * 0.3
        )

        if invited_by_offense and offense_strength > defense_strength:
            return Side.OFFENSE
        if invited_by_defense:
            return Side.DEFENSE
        if invited_by_offense:
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit moderate ships."""
        return min(3, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack based on strategic value."""
        planets = defense.home_planets
        if not planets:
            return None

        # Prefer planets where we can establish foothold
        # (fewer ships but not empty)
        return min(
            planets,
            key=lambda p: p.get_ships(defense.name) if p.get_ships(defense.name) > 0 else 100
        )

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Accept deal if beneficial."""
        # Accept if we need cards
        if len(player.hand) < 5:
            return {"type": "colony_swap"}
        return None

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power opportunistically."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter if good opportunity."""
        cards = player.get_encounter_cards()
        return len(cards) >= 2 and self.get_hand_strength(player) > 0.3


@dataclass
class SocialAI(AIStrategy):
    """
    Social AI focused on alliances and diplomacy.

    Traits:
    - Always invites all possible allies
    - Accepts most alliance invitations
    - Prefers negotiation over combat
    - Makes deals whenever possible
    """
    name: str = field(default="SocialAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Prefer negotiate cards."""
        negotiate_cards = player.get_negotiate_cards()
        if negotiate_cards:
            return negotiate_cards[0]

        attack_cards = player.get_attack_cards()
        if attack_cards:
            # Play low attack if forced to fight
            return min(attack_cards, key=lambda c: c.value)

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit moderate ships."""
        return max(2, max_ships // 2)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite everyone!"""
        return list(potential_allies)

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Accept any invitation."""
        from ..types import Side
        if invited_by_offense:
            return Side.OFFENSE
        if invited_by_defense:
            return Side.DEFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit ships to help allies."""
        return max(2, max_ships - 1)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Random planet selection."""
        planets = defense.home_planets
        if not planets:
            return None
        return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Always try to deal."""
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power if it helps diplomacy."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter for more interaction."""
        cards = player.get_encounter_cards()
        return len(cards) >= 3


@dataclass
class AdaptiveAI(AIStrategy):
    """
    Adaptive AI that changes strategy based on game state.

    Traits:
    - Plays aggressively when behind
    - Plays cautiously when ahead
    - Targets leader when not winning
    - Defends aggressively when threatened
    """
    name: str = field(default="AdaptiveAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def _get_position(self, game: "Game", player: "Player") -> str:
        """Determine player's position: 'leading', 'contending', 'behind'."""
        my_colonies = player.count_foreign_colonies(game.planets)

        all_colonies = [
            p.count_foreign_colonies(game.planets)
            for p in game.players
        ]
        max_colonies = max(all_colonies)
        avg_colonies = sum(all_colonies) / len(all_colonies)

        if my_colonies == max_colonies and my_colonies >= 3:
            return 'leading'
        elif my_colonies >= avg_colonies:
            return 'contending'
        else:
            return 'behind'

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Adapt card selection to position."""
        position = self._get_position(game, player)
        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        if position == 'leading':
            # Play conservatively when ahead
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                return sorted_cards[len(sorted_cards) // 2]  # Medium card
            if negotiate_cards:
                return negotiate_cards[0]

        elif position == 'behind':
            # Play aggressively when behind
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        else:  # contending
            if is_offense and attack_cards:
                return max(attack_cards, key=lambda c: c.value)
            elif attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                return sorted_cards[min(2, len(sorted_cards)-1)]

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Adapt ship commitment to position."""
        position = self._get_position(game, player)

        if position == 'behind':
            return max_ships  # Go all in when behind
        elif position == 'leading':
            return max(1, max_ships - 2)  # Conserve when ahead
        else:
            return max(2, max_ships - 1)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite based on position."""
        position = self._get_position(game, player)

        if position == 'behind':
            # Need help when behind
            return list(potential_allies)
        elif position == 'leading':
            # Don't share wins when ahead
            return []
        else:
            # Invite 1-2 when contending
            count = min(2, len(potential_allies))
            if count > 0:
                return self._rng.sample(potential_allies, count)
            return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Join side that benefits our position."""
        from ..types import Side
        position = self._get_position(game, player)

        # Check if offense is leading
        offense_colonies = offense.count_foreign_colonies(game.planets)
        defense_colonies = defense.count_foreign_colonies(game.planets)

        if position == 'leading':
            # Don't help others win
            return None

        if invited_by_defense and offense_colonies >= 4:
            # Help stop leader
            return Side.DEFENSE

        if invited_by_offense:
            return Side.OFFENSE
        if invited_by_defense:
            return Side.DEFENSE

        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit based on stakes."""
        return max(2, max_ships - 1)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack strategic targets."""
        planets = defense.home_planets
        if not planets:
            return None

        position = self._get_position(game, player)

        if position == 'behind':
            # Attack weakest to guarantee colony
            return min(planets, key=lambda p: p.get_ships(defense.name))
        else:
            # Random attack
            return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Deal based on position."""
        position = self._get_position(game, player)

        if position == 'behind':
            return {"type": "colony_swap"}  # Need progress
        elif position == 'leading':
            return None  # Don't give opponent colonies
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Second encounter based on position."""
        position = self._get_position(game, player)
        cards = player.get_encounter_cards()

        if position == 'behind' and len(cards) >= 2:
            return True
        if position == 'contending' and len(cards) >= 3:
            return True
        return False
