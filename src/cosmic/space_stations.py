"""
Space Station expansion for Cosmic Encounter.

From the Cosmic Eons expansion - Space Stations are structures that can be
built on colonies to provide ongoing benefits.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
from enum import Enum, auto

if TYPE_CHECKING:
    from .game import Game
    from .player import Player
    from .planet import Planet


class StationType(Enum):
    """Types of space stations."""
    DEFENSE = auto()        # Provides defensive bonuses
    ATTACK = auto()         # Provides offensive bonuses
    ECONOMIC = auto()       # Provides card/resource benefits
    SPECIAL = auto()        # Unique effects


@dataclass
class SpaceStation:
    """
    A space station that can be built on a colony.

    Space stations provide ongoing benefits to their owner when
    defending or using the colony where they're built.
    """
    name: str
    station_type: StationType
    description: str
    defense_bonus: int = 0
    attack_bonus: int = 0
    card_draw: int = 0
    special_ability: Optional[str] = None
    owner: Optional["Player"] = None
    location: Optional["Planet"] = None
    is_active: bool = True

    def on_defense(self, game: "Game", player: "Player") -> int:
        """
        Called when defending the colony with this station.
        Returns bonus to add to defense total.
        """
        if not self.is_active:
            return 0
        return self.defense_bonus

    def on_attack(self, game: "Game", player: "Player") -> int:
        """
        Called when attacking from the colony with this station.
        Returns bonus to add to attack total.
        """
        if not self.is_active:
            return 0
        return self.attack_bonus

    def on_encounter_end(self, game: "Game", player: "Player", won: bool) -> None:
        """Called at the end of an encounter involving this station."""
        if not self.is_active:
            return

        # Draw cards if station provides card draw and player won
        if won and self.card_draw > 0:
            cards = game.cosmic_deck.draw_multiple(self.card_draw)
            player.add_cards(cards)


# Pre-defined space stations from Cosmic Eons
SPACE_STATIONS: Dict[str, SpaceStation] = {}


def _register_station(station: SpaceStation) -> SpaceStation:
    """Register a space station type."""
    SPACE_STATIONS[station.name.lower()] = station
    return station


# Defense Stations
_register_station(SpaceStation(
    name="Fortress",
    station_type=StationType.DEFENSE,
    description="+5 to defense when defending this colony.",
    defense_bonus=5
))

_register_station(SpaceStation(
    name="Shield Generator",
    station_type=StationType.DEFENSE,
    description="+3 to defense, opponent's reinforcements reduced by 1.",
    defense_bonus=3
))

_register_station(SpaceStation(
    name="Bunker",
    station_type=StationType.DEFENSE,
    description="+2 to defense, ships can't be sent to warp on a tie.",
    defense_bonus=2,
    special_ability="no_warp_on_tie"
))

_register_station(SpaceStation(
    name="Citadel",
    station_type=StationType.DEFENSE,
    description="+4 to defense when defending with 3+ ships.",
    defense_bonus=4,
    special_ability="requires_3_ships"
))


# Attack Stations
_register_station(SpaceStation(
    name="Launch Bay",
    station_type=StationType.ATTACK,
    description="+3 to attack when launching from this colony.",
    attack_bonus=3
))

_register_station(SpaceStation(
    name="Weapons Platform",
    station_type=StationType.ATTACK,
    description="+4 to attack, -1 to defense.",
    attack_bonus=4,
    defense_bonus=-1
))

_register_station(SpaceStation(
    name="Assault Base",
    station_type=StationType.ATTACK,
    description="+2 to attack, draw 1 card when winning as offense.",
    attack_bonus=2,
    card_draw=1
))


# Economic Stations
_register_station(SpaceStation(
    name="Trade Hub",
    station_type=StationType.ECONOMIC,
    description="Draw 1 card at start of each encounter you're involved in.",
    card_draw=1
))

_register_station(SpaceStation(
    name="Research Lab",
    station_type=StationType.ECONOMIC,
    description="Draw 2 cards when you successfully defend this colony.",
    card_draw=2
))

_register_station(SpaceStation(
    name="Mining Facility",
    station_type=StationType.ECONOMIC,
    description="Once per turn, look at top card of deck and decide to draw or not.",
    special_ability="peek_draw"
))


# Special Stations
_register_station(SpaceStation(
    name="Warp Gate",
    station_type=StationType.SPECIAL,
    description="Ships can return from warp to this colony instead of home.",
    special_ability="warp_return"
))

_register_station(SpaceStation(
    name="Communication Array",
    station_type=StationType.SPECIAL,
    description="When alliances are formed, you may invite one additional ally.",
    special_ability="extra_ally"
))

_register_station(SpaceStation(
    name="Cloning Vats",
    station_type=StationType.SPECIAL,
    description="When you lose ships from this colony, return half (round up) to colony.",
    special_ability="half_ships_return"
))

_register_station(SpaceStation(
    name="Time Beacon",
    station_type=StationType.SPECIAL,
    description="Once per game, replay an encounter where you lost.",
    special_ability="replay_encounter"
))

_register_station(SpaceStation(
    name="Dimensional Gate",
    station_type=StationType.SPECIAL,
    description="Ships from this colony count double but you can only send half.",
    special_ability="double_value_half_ships"
))


class SpaceStationManager:
    """
    Manages space stations in a game.

    Handles building, destroying, and applying station effects.
    """

    def __init__(self, game: "Game"):
        self.game = game
        self.built_stations: Dict[str, SpaceStation] = {}  # planet_id -> station
        self.player_stations: Dict[str, List[SpaceStation]] = {}  # player_name -> stations
        self.available_stations: List[str] = list(SPACE_STATIONS.keys())

    def build_station(
        self,
        player: "Player",
        planet: "Planet",
        station_name: str
    ) -> bool:
        """
        Build a space station on a colony.

        Requirements:
        - Player must have a colony on the planet
        - No station already exists on the planet
        - Station type must be available

        Returns True if successful.
        """
        # Check requirements
        if not planet.has_colony(player.name):
            return False

        planet_id = f"{planet.owner.name}_{planet.index}"
        if planet_id in self.built_stations:
            return False

        station_name_lower = station_name.lower()
        if station_name_lower not in SPACE_STATIONS:
            return False

        if station_name_lower not in self.available_stations:
            return False

        # Build the station
        template = SPACE_STATIONS[station_name_lower]
        station = SpaceStation(
            name=template.name,
            station_type=template.station_type,
            description=template.description,
            defense_bonus=template.defense_bonus,
            attack_bonus=template.attack_bonus,
            card_draw=template.card_draw,
            special_ability=template.special_ability,
            owner=player,
            location=planet,
            is_active=True
        )

        self.built_stations[planet_id] = station
        self.available_stations.remove(station_name_lower)

        if player.name not in self.player_stations:
            self.player_stations[player.name] = []
        self.player_stations[player.name].append(station)

        return True

    def destroy_station(self, planet: "Planet") -> Optional[SpaceStation]:
        """
        Destroy the station on a planet.

        Returns the destroyed station, or None if no station exists.
        """
        planet_id = f"{planet.owner.name}_{planet.index}"
        station = self.built_stations.pop(planet_id, None)

        if station:
            station.is_active = False
            if station.owner and station.owner.name in self.player_stations:
                if station in self.player_stations[station.owner.name]:
                    self.player_stations[station.owner.name].remove(station)

        return station

    def get_station(self, planet: "Planet") -> Optional[SpaceStation]:
        """Get the station on a planet, if any."""
        planet_id = f"{planet.owner.name}_{planet.index}"
        return self.built_stations.get(planet_id)

    def get_player_stations(self, player: "Player") -> List[SpaceStation]:
        """Get all stations owned by a player."""
        return self.player_stations.get(player.name, [])

    def get_defense_bonus(self, planet: "Planet", player: "Player") -> int:
        """Get total defense bonus from station on this planet."""
        station = self.get_station(planet)
        if not station or station.owner != player:
            return 0
        return station.on_defense(self.game, player)

    def get_attack_bonus(self, planet: "Planet", player: "Player") -> int:
        """Get attack bonus from station on launch planet."""
        station = self.get_station(planet)
        if not station or station.owner != player:
            return 0
        return station.on_attack(self.game, player)

    def apply_encounter_end(
        self,
        planet: "Planet",
        player: "Player",
        won: bool
    ) -> None:
        """Apply station effects at end of encounter."""
        station = self.get_station(planet)
        if station and station.owner == player:
            station.on_encounter_end(self.game, player, won)


def get_station_names() -> List[str]:
    """Get names of all available station types."""
    return [s.name for s in SPACE_STATIONS.values()]


def get_station(name: str) -> Optional[SpaceStation]:
    """Get a station template by name."""
    return SPACE_STATIONS.get(name.lower())
