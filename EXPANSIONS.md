# Cosmic Encounter Simulator - Official Expansions

This simulator contains only **official Fantasy Flight Games** aliens from the
Cosmic Encounter game and its expansions. No custom/homebrew aliens are included.

## Expansion Overview

| Expansion | Year | Aliens | Notes |
|-----------|------|--------|-------|
| **Base Game** | 2008 | 50 | Core game aliens |
| **Cosmic Incursion** | 2010 | 20 | Adds reward deck, 6th player support |
| **Cosmic Conflict** | 2011 | 20 | Adds hazard deck, 7th player support |
| **Cosmic Alliance** | 2012 | 20 | Adds team rules, 8th player support |
| **Cosmic Storm** | 2013 | 25 | Adds space stations |
| **Cosmic Dominion** | 2014 | 30 | Adds reward deck variant |
| **Cosmic Eons** | 2016 | 30 | Adds hidden alliances variant |
| **Cosmic Odyssey** | 2022 | 42 | Includes 11 alternate timeline aliens |
| **Promos** | Various | 1 | Demon (promotional alien) |

**Total: 238 official aliens**

## Using Expansion Filtering

The simulator supports enabling/disabling specific expansions. This allows you
to simulate games using only the aliens from expansions you own or prefer.

### Python API

```python
from src.cosmic.aliens.registry import AlienRegistry
from src.cosmic.types import Expansion

# Enable only base game
AlienRegistry.enable_base_game_only()
print(f"Base game: {AlienRegistry.count_enabled()} aliens")

# Enable specific expansions
AlienRegistry.set_enabled_expansions({
    Expansion.BASE,
    Expansion.COSMIC_INCURSION,
    Expansion.COSMIC_CONFLICT
})
print(f"First 3 sets: {AlienRegistry.count_enabled()} aliens")

# Enable all expansions (default)
AlienRegistry.enable_all_expansions()
print(f"All expansions: {AlienRegistry.count_enabled()} aliens")

# Get summary of expansion status
print(AlienRegistry.get_expansion_summary())

# Get aliens from a specific expansion
dominion_aliens = AlienRegistry.get_by_expansion(Expansion.COSMIC_DOMINION)
print(f"Cosmic Dominion aliens: {[a.name for a in dominion_aliens]}")

# Get only enabled aliens for game selection
enabled = AlienRegistry.get_enabled_aliens()
```

### Available Expansions

The `Expansion` enum contains:
- `Expansion.BASE` - Base Game (2008)
- `Expansion.COSMIC_INCURSION` - Cosmic Incursion (2010)
- `Expansion.COSMIC_CONFLICT` - Cosmic Conflict (2011)
- `Expansion.COSMIC_ALLIANCE` - Cosmic Alliance (2012)
- `Expansion.COSMIC_STORM` - Cosmic Storm (2013)
- `Expansion.COSMIC_DOMINION` - Cosmic Dominion (2014)
- `Expansion.COSMIC_EONS` - Cosmic Eons (2016)
- `Expansion.COSMIC_ODYSSEY` - Cosmic Odyssey (2022)
- `Expansion.HOMEBREW` - Custom aliens (none currently registered)

## Alien Categories

Each alien has a **power category** that indicates complexity:

- **Green** - Simple, straightforward powers (recommended for beginners)
- **Yellow** - Moderate complexity
- **Red** - Complex or game-warping powers (for experienced players)

## Alternate Timeline Aliens

Cosmic Odyssey introduced "alternate timeline" versions of existing aliens.
These provide different mechanical interpretations of classic aliens:

| Alternate Alien | Original From | Key Difference |
|-----------------|---------------|----------------|
| Brute_Alt | Cosmic Storm | Different crushing mechanic |
| Daredevil_Alt | Cosmic Dominion | Different risk/reward |
| Demon_Alt | Promo | Different dark power usage |
| Grumpus_Alt | Cosmic Storm | Different token accumulation |
| Locust_Alt | Cosmic Incursion | Forces opponent discard on win |
| Masochist_Alt | Base Game | Bonus based on warp ships |
| Perfectionist_Alt | Cosmic Eons | Different precision mechanic |
| Sadist_Alt | Cosmic Conflict | Different torment mechanic |
| Schizoid_Alt | Cosmic Alliance | Different madness mechanic |
| Void_Alt | Base Game | Different eradication mechanic |
| Zombie_Alt | Base Game | Different resurrection mechanic |
| The Meek | New in Odyssey | Wins by losing encounters |

## Base Game Aliens (50)

Amoeba, Antimatter, Barbarian, Calculator, Chosen, Citadel, Clone, Cudgel,
Dictator, Fido, Filch, Fodder, Gambler, Grudge, Hacker, Hate, Healer, Human,
Kamikaze, Loser, Machine, Macron, Masochist, Mind, Mirror, Miser, Mite, Mutant,
Observer, Oracle, Pacifist, Parasite, Philanthropist, Reincarnator, Remora,
Reserve, Shadow, Sorcerer, Spiff, Tick-Tock, Trader, Tripler, Vacuum, Virus,
Void, Vulch, Warpish, Warrior, Will, Zombie, Demon (promo)

## Recommended Expansion Combinations

### New Players (Base Only)
```python
AlienRegistry.enable_base_game_only()
```
50 aliens, all mechanics from the core game.

### Casual Play (Base + First 2 Expansions)
```python
AlienRegistry.set_enabled_expansions({
    Expansion.BASE,
    Expansion.COSMIC_INCURSION,
    Expansion.COSMIC_CONFLICT
})
```
90 aliens, supports up to 7 players.

### Full Experience (All Expansions)
```python
AlienRegistry.enable_all_expansions()
```
238 aliens, all official content.

## Notes for Accuracy

This simulator models the official FFG Cosmic Encounter rules as closely as
possible. Some simplifications are made for simulation purposes:

1. **Negotiation** - Simplified to random card exchanges
2. **Timing** - Sequential resolution of simultaneous effects
3. **Artifacts** - Basic artifact card effects
4. **Complex Powers** - Some complex powers simplified for simulation

The goal is to capture the statistical behavior of the game across thousands
of simulations, not to replicate exact physical gameplay.
