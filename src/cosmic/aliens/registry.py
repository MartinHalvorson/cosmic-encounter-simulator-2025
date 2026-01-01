"""
Registry for alien powers with expansion filtering support.

Supports filtering aliens by expansion to allow games with only
specific expansion content enabled.
"""

from typing import Dict, List, Optional, Set, Type
from .base import AlienPower
from ..types import Expansion


class AlienRegistry:
    """
    Registry for all available alien powers.
    Aliens are registered by name and can be retrieved for game setup.
    Supports filtering by expansion to enable/disable expansion content.
    """
    _aliens: Dict[str, AlienPower] = {}
    _enabled_expansions: Set[Expansion] = set(Expansion)  # All enabled by default

    @classmethod
    def register(cls, alien: AlienPower) -> None:
        """Register an alien power."""
        cls._aliens[alien.name.lower()] = alien

    @classmethod
    def get(cls, name: str) -> Optional[AlienPower]:
        """Get an alien power by name (case-insensitive)."""
        return cls._aliens.get(name.lower())

    @classmethod
    def get_all(cls) -> List[AlienPower]:
        """Get all registered alien powers."""
        return list(cls._aliens.values())

    @classmethod
    def get_names(cls) -> List[str]:
        """Get names of all registered alien powers."""
        return [a.name for a in cls._aliens.values()]

    @classmethod
    def count(cls) -> int:
        """Number of registered aliens."""
        return len(cls._aliens)

    @classmethod
    def clear(cls) -> None:
        """Clear all registered aliens (for testing)."""
        cls._aliens.clear()

    # =========================================================================
    # EXPANSION FILTERING
    # =========================================================================

    @classmethod
    def set_enabled_expansions(cls, expansions: Set[Expansion]) -> None:
        """
        Set which expansions are enabled for alien selection.

        Args:
            expansions: Set of Expansion enums to enable
        """
        cls._enabled_expansions = set(expansions)

    @classmethod
    def enable_expansion(cls, expansion: Expansion) -> None:
        """Enable a specific expansion."""
        cls._enabled_expansions.add(expansion)

    @classmethod
    def disable_expansion(cls, expansion: Expansion) -> None:
        """Disable a specific expansion."""
        cls._enabled_expansions.discard(expansion)

    @classmethod
    def enable_all_expansions(cls) -> None:
        """Enable all expansions."""
        cls._enabled_expansions = set(Expansion)

    @classmethod
    def enable_base_game_only(cls) -> None:
        """Enable only the base game (no expansions)."""
        cls._enabled_expansions = {Expansion.BASE}

    @classmethod
    def get_enabled_expansions(cls) -> Set[Expansion]:
        """Get currently enabled expansions."""
        return cls._enabled_expansions.copy()

    @classmethod
    def is_expansion_enabled(cls, expansion: Expansion) -> bool:
        """Check if an expansion is enabled."""
        return expansion in cls._enabled_expansions

    @classmethod
    def get_by_expansion(cls, expansion: Expansion) -> List[AlienPower]:
        """Get all aliens from a specific expansion."""
        return [a for a in cls._aliens.values() if a.expansion == expansion]

    @classmethod
    def get_enabled_aliens(cls) -> List[AlienPower]:
        """Get all aliens from currently enabled expansions."""
        return [a for a in cls._aliens.values()
                if a.expansion in cls._enabled_expansions]

    @classmethod
    def get_enabled_names(cls) -> List[str]:
        """Get names of aliens from enabled expansions."""
        return [a.name for a in cls.get_enabled_aliens()]

    @classmethod
    def count_enabled(cls) -> int:
        """Count aliens from enabled expansions."""
        return len(cls.get_enabled_aliens())

    @classmethod
    def count_by_expansion(cls) -> Dict[Expansion, int]:
        """Count aliens by expansion."""
        counts = {exp: 0 for exp in Expansion}
        for alien in cls._aliens.values():
            counts[alien.expansion] += 1
        return counts

    @classmethod
    def get_expansion_summary(cls) -> str:
        """Get a summary of alien counts by expansion."""
        counts = cls.count_by_expansion()
        lines = ["Alien counts by expansion:"]
        for exp in Expansion:
            enabled = "+" if exp in cls._enabled_expansions else "-"
            lines.append(f"  [{enabled}] {exp.value}: {counts[exp]} aliens")
        lines.append(f"  Total registered: {cls.count()}")
        lines.append(f"  Total enabled: {cls.count_enabled()}")
        return "\n".join(lines)


def get_all_aliens() -> List[AlienPower]:
    """Get all registered alien powers."""
    return AlienRegistry.get_all()


def get_alien(name: str) -> Optional[AlienPower]:
    """Get an alien power by name."""
    return AlienRegistry.get(name)


# Import all power implementations to register them
from .powers import *  # noqa: F401, F403, E402
