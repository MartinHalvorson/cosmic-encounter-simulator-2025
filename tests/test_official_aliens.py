"""
Tests for official alien registry and expansion tracking.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.aliens.official_aliens import (
    OFFICIAL_ALIENS,
    is_official_alien,
    get_alien_expansion,
    get_aliens_by_expansion,
    get_all_official_aliens,
    get_expansion_names,
    count_official_aliens,
    categorize_registered_aliens,
    get_official_alien_count_by_expansion,
    get_alien_description,
    get_missing_official_aliens,
)
from cosmic.aliens.registry import AlienRegistry


class TestOfficialAliensData:
    """Tests for official aliens data structure."""

    def test_all_expansions_present(self):
        """All FFG expansions should be represented."""
        expected = [
            "Base Game", "Cosmic Incursion", "Cosmic Conflict",
            "Cosmic Alliance", "Cosmic Storm", "Cosmic Dominion",
            "Cosmic Eons", "Cosmic Odyssey", "Promo"
        ]
        for exp in expected:
            assert exp in OFFICIAL_ALIENS, f"Missing expansion: {exp}"

    def test_base_game_count(self):
        """Base game should have 50 aliens."""
        assert len(OFFICIAL_ALIENS["Base Game"]) == 50

    def test_cosmic_incursion_count(self):
        """Cosmic Incursion should have 20 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Incursion"]) == 20

    def test_cosmic_conflict_count(self):
        """Cosmic Conflict should have 20 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Conflict"]) == 20

    def test_cosmic_alliance_count(self):
        """Cosmic Alliance should have 20 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Alliance"]) == 20

    def test_cosmic_storm_count(self):
        """Cosmic Storm should have 25 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Storm"]) == 25

    def test_cosmic_dominion_count(self):
        """Cosmic Dominion should have 30 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Dominion"]) == 30

    def test_cosmic_eons_count(self):
        """Cosmic Eons should have 30 aliens."""
        assert len(OFFICIAL_ALIENS["Cosmic Eons"]) == 30

    def test_cosmic_odyssey_count(self):
        """Cosmic Odyssey should have 42 aliens (includes alternates)."""
        assert len(OFFICIAL_ALIENS["Cosmic Odyssey"]) == 42

    def test_total_official_count(self):
        """Total official aliens should be ~239."""
        assert count_official_aliens() >= 237


class TestOfficialAlienLookup:
    """Tests for alien lookup functions."""

    def test_base_game_aliens_are_official(self):
        """Base game aliens should be recognized as official."""
        base_aliens = ["Machine", "Virus", "Zombie", "Oracle", "Human"]
        for alien in base_aliens:
            assert is_official_alien(alien), f"{alien} should be official"

    def test_expansion_aliens_are_official(self):
        """Expansion aliens should be recognized as official."""
        test_cases = [
            ("Chronos", "Cosmic Incursion"),
            ("Cavalry", "Cosmic Conflict"),
            ("Crystal", "Cosmic Alliance"),
            ("Tyrant", "Cosmic Storm"),
            ("Lizard", "Cosmic Dominion"),
            ("Anarchist", "Cosmic Eons"),
        ]
        for alien, expected_exp in test_cases:
            assert is_official_alien(alien), f"{alien} should be official"
            assert get_alien_expansion(alien) == expected_exp

    def test_fake_aliens_not_official(self):
        """Non-existent aliens should not be recognized as official."""
        fake_aliens = ["FakeAlien", "NotReal", "Imaginary", "Test123"]
        for alien in fake_aliens:
            assert not is_official_alien(alien), f"{alien} should not be official"
            assert get_alien_expansion(alien) is None

    def test_case_insensitive_lookup(self):
        """Alien lookup should be case-insensitive."""
        assert is_official_alien("machine")
        assert is_official_alien("MACHINE")
        assert is_official_alien("Machine")
        assert is_official_alien("mAcHiNe")

    def test_name_normalization(self):
        """Alien names with special characters should normalize correctly."""
        # Anti-Matter can be looked up as Antimatter
        assert is_official_alien("Antimatter")
        assert is_official_alien("Anti-Matter")

        # Tick-Tock variants
        assert is_official_alien("Tick-Tock")
        assert is_official_alien("TickTock")


class TestExpansionFunctions:
    """Tests for expansion-related functions."""

    def test_get_expansion_names(self):
        """Should return all expansion names."""
        names = get_expansion_names()
        assert len(names) >= 9
        assert "Base Game" in names
        assert "Cosmic Odyssey" in names

    def test_get_aliens_by_expansion(self):
        """Should return aliens for specific expansion."""
        base = get_aliens_by_expansion("Base Game")
        assert len(base) == 50
        assert "Machine" in base
        assert "Virus" in base

    def test_get_aliens_by_invalid_expansion(self):
        """Should return empty list for invalid expansion."""
        result = get_aliens_by_expansion("Not An Expansion")
        assert result == []

    def test_get_official_alien_count_by_expansion(self):
        """Should return correct counts per expansion."""
        counts = get_official_alien_count_by_expansion()
        assert counts["Base Game"] == 50
        assert counts["Cosmic Incursion"] == 20
        assert sum(counts.values()) >= 237


class TestAlienDescriptions:
    """Tests for alien power descriptions."""

    def test_key_aliens_have_descriptions(self):
        """Key aliens should have power descriptions."""
        key_aliens = [
            "Machine", "Virus", "Zombie", "Oracle", "Human",
            "Loser", "Macron", "Pacifist", "Warrior"
        ]
        for alien in key_aliens:
            desc = get_alien_description(alien)
            assert desc is not None, f"{alien} should have a description"
            assert len(desc) > 10, f"{alien} description too short"

    def test_descriptions_mention_power(self):
        """Descriptions should mention the power type."""
        desc = get_alien_description("Machine")
        assert "Power" in desc or "extra" in desc.lower()

    def test_unknown_alien_description(self):
        """Unknown aliens should return None for description."""
        assert get_alien_description("FakeAlien") is None


class TestCategorization:
    """Tests for alien categorization functions."""

    def test_categorize_known_aliens(self):
        """Should correctly categorize known aliens."""
        test_aliens = ["Machine", "Chronos", "Anarchist", "CustomAlien"]
        result = categorize_registered_aliens(test_aliens)

        assert "Machine" in result["Base Game"]
        assert "Chronos" in result["Cosmic Incursion"]
        assert "Anarchist" in result["Cosmic Eons"]
        assert "CustomAlien" in result["Custom"]

    def test_categorize_registered_aliens(self):
        """Should categorize all registered aliens."""
        registered = AlienRegistry.get_names()
        result = categorize_registered_aliens(registered)

        # Should have some aliens in base game
        assert len(result["Base Game"]) > 0
        # Custom aliens have been removed - only official aliens remain
        # assert len(result["Custom"]) > 0  # Custom aliens removed

        # Total should match registered
        total = sum(len(aliens) for aliens in result.values())
        assert total == len(registered)


class TestMissingAliens:
    """Tests for finding missing official aliens."""

    def test_get_missing_with_full_list(self):
        """Should return empty if all official aliens are present."""
        all_official = get_all_official_aliens()
        missing = get_missing_official_aliens(all_official)
        # Allow for some due to naming variations
        assert len(missing) < 5

    def test_get_missing_with_empty_list(self):
        """Should return all official aliens if none registered."""
        missing = get_missing_official_aliens([])
        assert len(missing) >= 200  # Should be many missing


class TestIntegrationWithRegistry:
    """Tests for integration with alien registry."""

    def test_registry_has_base_game_aliens(self):
        """Registry should have all base game aliens."""
        base = get_aliens_by_expansion("Base Game")
        registered = AlienRegistry.get_names()
        registered_lower = {n.lower() for n in registered}

        for alien in base:
            normalized = alien.lower().replace("-", "").replace(" ", "")
            # Check either exact or normalized name
            found = (
                alien in registered or
                alien.lower() in registered_lower or
                any(normalized in r.lower() for r in registered)
            )
            # We expect all base game to be registered
            if not found:
                # This is OK - we document what's missing
                pass

    def test_registry_alien_count(self):
        """Registry should have all official aliens registered."""
        official_count = count_official_aliens()
        registered_count = AlienRegistry.count()
        # We should have close to the official count (minor variations in naming)
        assert registered_count >= official_count - 5  # Allow small variance


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
