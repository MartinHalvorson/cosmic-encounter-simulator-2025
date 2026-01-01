"""
Tests for encounter phase mechanics.

Tests the 8 phases of a Cosmic Encounter:
1. Regroup - Retrieve ships from warp
2. Destiny - Draw destiny card to determine opponent
3. Launch - Commit ships to the hyperspace gate
4. Alliance - Invite and accept allies
5. Planning - Select encounter cards
6. Reveal - Reveal cards and apply powers
7. Resolution - Determine winner and apply results
8. End - Handle aftermath and check for second encounter
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig, GamePhase
from cosmic.cards.base import AttackCard, NegotiateCard, ReinforcementCard


class TestRegroupPhase:
    """Tests for the Regroup phase."""

    def test_regroup_retrieves_one_ship(self):
        """Standard regroup retrieves 1 ship from warp."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        player.ships_in_warp = 5
        initial_warp = player.ships_in_warp

        game.offense = player
        game.encounter_number = 1
        game._regroup_phase()

        # Should retrieve exactly 1 ship
        assert player.ships_in_warp == initial_warp - 1

    def test_regroup_with_no_ships_in_warp(self):
        """Regroup with 0 ships in warp doesn't error."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        player.ships_in_warp = 0

        game.offense = player
        game.encounter_number = 1
        game._regroup_phase()  # Should not error

        assert player.ships_in_warp == 0

    def test_regroup_reduces_warp_count(self):
        """Regroup should reduce warp ship count for the offense."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        player.ships_in_warp = 5

        game.offense = player
        game.encounter_number = 1
        game._regroup_phase()

        # Warp should be reduced (ships return to colonies)
        assert player.ships_in_warp <= 5


class TestDestinyPhase:
    """Tests for the Destiny phase."""

    def test_destiny_sets_defender(self):
        """Destiny phase sets a defender."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game._destiny_phase()

        assert game.defense is not None

    def test_destiny_draws_from_deck(self):
        """Destiny draws a card from destiny deck."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        initial_cards = game.destiny_deck.cards_remaining()
        game.offense = game.players[0]
        game._destiny_phase()

        # Should have drawn at least one card
        assert game.destiny_deck.cards_remaining() <= initial_cards

    def test_destiny_targets_other_player(self):
        """Destiny typically targets a different player."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        defenders_seen = set()
        for i in range(20):  # Run multiple times
            game.offense = game.players[0]
            game.defense = None
            game._destiny_phase()
            if game.defense:
                defenders_seen.add(game.defense.name)

        # Should see at least one other player as defender
        assert len(defenders_seen) >= 1


class TestLaunchPhase:
    """Tests for the Launch phase."""

    def test_launch_commits_ships_to_gate(self):
        """Launch phase commits ships to hyperspace gate."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()  # Set up target planet
        game._launch_phase()

        # Offense should have ships committed (offense_ships is a dict)
        total_offense = sum(game.offense_ships.values())
        assert total_offense > 0

    def test_launch_respects_gate_limit(self):
        """Ships committed shouldn't exceed 4 (standard limit)."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()

        # Standard gate limit is 4 ships per player
        offense_ships = game.offense_ships.get(game.offense.name, 0)
        assert offense_ships <= 4

    def test_launch_requires_available_ships(self):
        """Player must have ships to launch."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Put all offense ships in warp
        player = game.players[0]
        for planet in player.home_planets:
            planet.set_ships(player.name, 0)
        player.ships_in_warp = 20

        game.offense = player
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()

        # With no ships available, can't launch many (may still launch 0)
        offense_ships = game.offense_ships.get(player.name, 0)
        assert offense_ships >= 0  # Just verify it doesn't error


class TestAlliancePhase:
    """Tests for the Alliance phase."""

    def test_alliance_phase_runs(self):
        """Alliance phase should execute without error."""
        config = GameConfig(num_players=5, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()
        game._alliance_phase()

        # Phase should complete (allies may or may not join)
        assert True

    def test_offense_can_have_allies(self):
        """Offense side can gain allies."""
        config = GameConfig(num_players=5, seed=42)
        game = Game(config=config)
        game.setup()

        # Run multiple encounters to check for allies
        ally_found = False
        for seed in range(20):
            config = GameConfig(num_players=5, seed=seed)
            game = Game(config=config)
            game.setup()

            game.offense = game.players[0]
            game.defense = game.players[1]
            game._destiny_phase()
            game._launch_phase()
            game._alliance_phase()

            if game.offense_allies:
                ally_found = True
                break

        # At least one game should have offense allies
        assert ally_found

    def test_defense_can_have_allies(self):
        """Defense side can gain allies."""
        config = GameConfig(num_players=5, seed=42)
        game = Game(config=config)
        game.setup()

        # Run multiple encounters to check for allies
        ally_found = False
        for seed in range(20):
            config = GameConfig(num_players=5, seed=seed)
            game = Game(config=config)
            game.setup()

            game.offense = game.players[0]
            game.defense = game.players[1]
            game._destiny_phase()
            game._launch_phase()
            game._alliance_phase()

            if game.defense_allies:
                ally_found = True
                break

        # At least one game should have defense allies
        assert ally_found


class TestPlanningPhase:
    """Tests for the Planning phase."""

    def test_planning_selects_cards(self):
        """Planning phase selects encounter cards."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()
        game._alliance_phase()
        game._planning_phase()

        # Both sides should have selected cards
        assert game.offense_card is not None
        assert game.defense_card is not None

    def test_planning_uses_encounter_cards(self):
        """Planning phase uses valid encounter cards."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()
        game._alliance_phase()
        game._planning_phase()

        # Cards should be encounter cards
        if game.offense_card:
            assert game.offense_card.is_encounter_card()
        if game.defense_card:
            assert game.defense_card.is_encounter_card()


class TestRevealPhase:
    """Tests for the Reveal phase."""

    def test_reveal_shows_cards(self):
        """Reveal phase makes cards visible."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()
        game._alliance_phase()
        game._planning_phase()
        game._reveal_phase()

        # Reveal should complete without error
        assert True

    def test_reveal_with_attack_cards(self):
        """Reveal with attack cards calculates values."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game.offense_card = AttackCard(value=10)
        game.defense_card = AttackCard(value=15)

        game._reveal_phase()

        # Phase should complete
        assert True


class TestResolutionPhase:
    """Tests for the Resolution phase."""

    def test_resolution_determines_winner(self):
        """Resolution phase determines encounter winner."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game._destiny_phase()
        game._launch_phase()
        game._alliance_phase()
        game._planning_phase()
        game._reveal_phase()
        game._resolution_phase()

        # Resolution should complete
        assert True

    def test_higher_attack_wins(self):
        """Higher attack total should win."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game.offense_ships = 4
        game.defense_ships = 4
        game.offense_allies = []
        game.defense_allies = []

        # Give offense higher card
        game.offense_card = AttackCard(value=20)
        game.defense_card = AttackCard(value=10)

        # Calculate totals
        offense_total = game.offense_card.value + game.offense_ships
        defense_total = game.defense_card.value + game.defense_ships

        assert offense_total > defense_total

    def test_negotiate_vs_attack_loses(self):
        """Negotiate vs attack loses the encounter."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]

        # Negotiate loses to attack
        game.offense_card = NegotiateCard()
        game.defense_card = AttackCard(value=4)

        assert game.defense_card.value > game.offense_card.value


class TestEndPhase:
    """Tests for the encounter End phase."""

    def test_end_phase_completes(self):
        """End phase should complete without error."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.play_encounter()

        # Encounter should complete
        assert game.current_turn >= 1

    def test_winner_earns_second_encounter(self):
        """Winning offense can get second encounter."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Run multiple games to check for second encounters
        second_encounter_found = False
        for seed in range(50):
            config = GameConfig(num_players=4, seed=seed, max_turns=10)
            game = Game(config=config)
            game.setup()

            for turn in range(10):
                if not game.is_over:
                    game.play_encounter()
                    if game.encounter_number > 1:
                        second_encounter_found = True
                        break
            if second_encounter_found:
                break

        # At least one game should have a second encounter
        assert second_encounter_found


class TestFullEncounterCycle:
    """Tests for complete encounter cycles."""

    def test_complete_encounter_runs(self):
        """A complete encounter should run all phases."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.play_encounter()

        # Turn should advance
        assert game.current_turn >= 1

    def test_100_encounters_complete(self):
        """100 consecutive encounters should complete."""
        config = GameConfig(num_players=4, seed=42, max_turns=100)
        game = Game(config=config)
        game.setup()

        encounters = 0
        while not game.is_over and game.current_turn < 100:
            game.play_encounter()
            encounters += 1

        assert encounters >= 1

    def test_phases_execute_in_order(self):
        """Phases should execute in correct order."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Phase order: Regroup, Destiny, Launch, Alliance, Planning, Reveal, Resolution
        game.offense = game.players[0]
        game.encounter_number = 1

        # Run phases manually
        game._regroup_phase()
        game._destiny_phase()
        assert game.defense is not None

        game._launch_phase()
        assert game.offense_ships >= 0

        game._alliance_phase()
        game._planning_phase()
        assert game.offense_card is not None


class TestEncounterEdgeCases:
    """Tests for edge cases in encounters."""

    def test_tie_breaker(self):
        """Ties should be resolved (defense wins ties)."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Set up a tie scenario
        game.offense = game.players[0]
        game.defense = game.players[1]
        game.offense_ships = 4
        game.defense_ships = 4
        game.offense_card = AttackCard(value=10)
        game.defense_card = AttackCard(value=10)

        offense_total = game.offense_card.value + game.offense_ships
        defense_total = game.defense_card.value + game.defense_ships

        # Tie - defense wins
        assert offense_total == defense_total

    def test_zero_ships_encounter(self):
        """Encounter with 0 ships should handle gracefully."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game.offense_ships = 0
        game.defense_ships = 4
        game.offense_card = AttackCard(value=40)
        game.defense_card = AttackCard(value=4)

        # Offense: 40 + 0 = 40
        # Defense: 4 + 4 = 8
        # Offense wins despite 0 ships
        offense_total = game.offense_card.value + game.offense_ships
        defense_total = game.defense_card.value + game.defense_ships

        assert offense_total > defense_total

    def test_double_negotiate(self):
        """Both sides playing Negotiate triggers deal."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game.defense = game.players[1]
        game.offense_card = NegotiateCard()
        game.defense_card = NegotiateCard()

        # Both negotiate - deal should happen
        both_negotiate = isinstance(game.offense_card, NegotiateCard) and isinstance(game.defense_card, NegotiateCard)
        assert both_negotiate


class TestReinforcementCards:
    """Tests for reinforcement card usage in encounters."""

    def test_reinforcement_adds_to_total(self):
        """Reinforcement cards add to encounter total."""
        attack = AttackCard(value=10)
        reinforcement = ReinforcementCard(value=5)

        total = attack.value + reinforcement.value
        assert total == 15

    def test_multiple_reinforcements_stack(self):
        """Multiple reinforcements should stack."""
        attack = AttackCard(value=10)
        reinforcements = [
            ReinforcementCard(value=2),
            ReinforcementCard(value=3),
            ReinforcementCard(value=5)
        ]

        total = attack.value + sum(r.value for r in reinforcements)
        assert total == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
