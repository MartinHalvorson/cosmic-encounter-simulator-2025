"""
Space Stations - Cosmic Alliance Expansion Feature.

Space Stations are permanent installations that provide ongoing benefits.
Each player can build space stations on their home planets.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

if TYPE_CHECKING:
    from .game import Game
    from .player import Player
    from .planet import Planet


class StationType(Enum):
    """Types of space stations available."""
    # Offensive Stations
    BATTLE_STATION = auto()      # +3 to attack total
    LAUNCH_PAD = auto()          # Commit +1 ship to encounters
    COMMAND_CENTER = auto()      # Draw 1 extra card when attacking

    # Defensive Stations
    SHIELD_GENERATOR = auto()    # +3 to defense total
    WARP_GATE = auto()           # Retrieve 1 extra ship from warp on regroup
    REPAIR_BAY = auto()          # Ships return here instead of warp (once per encounter)

    # Economic Stations
    TRADING_POST = auto()        # Draw 1 card when making successful deal
    RESOURCE_HUB = auto()        # Start of turn: draw 1 card if < 4 cards
    TECH_LAB = auto()            # +1 tech research progress per win

    # Strategic Stations
    OBSERVATORY = auto()         # Look at destiny deck top card before drawing
    RELAY_BEACON = auto()        # May invite 1 extra ally
    DOCKING_BAY = auto()         # Store up to 2 ships here for later use


@dataclass
class SpaceStation:
    """A space station installed on a planet."""
    station_type: StationType
    planet: Optional["Planet"] = None
    owner: Optional["Player"] = None
    is_active: bool = True

    # Docking bay specific: stored ships
    stored_ships: int = 0

    @property
    def name(self) -> str:
        """Human-readable station name."""
        return self.station_type.name.replace("_", " ").title()

    @property
    def description(self) -> str:
        """Get station ability description."""
        descriptions = {
            StationType.BATTLE_STATION: "+3 to your attack total when you are offense",
            StationType.LAUNCH_PAD: "Commit up to 5 ships instead of 4",
            StationType.COMMAND_CENTER: "Draw 1 extra card after winning as offense",
            StationType.SHIELD_GENERATOR: "+3 to your defense total",
            StationType.WARP_GATE: "Retrieve 2 ships from warp during regroup instead of 1",
            StationType.REPAIR_BAY: "Once per encounter, 1 ship goes here instead of warp",
            StationType.TRADING_POST: "Draw 1 card when you make a successful deal",
            StationType.RESOURCE_HUB: "Start of turn: draw 1 card if you have fewer than 4",
            StationType.TECH_LAB: "Gain +1 tech research progress when you win",
            StationType.OBSERVATORY: "Look at top destiny card before your turn begins",
            StationType.RELAY_BEACON: "May invite 1 additional ally",
            StationType.DOCKING_BAY: "Store up to 2 ships here; deploy them to any encounter",
        }
        return descriptions.get(self.station_type, "Unknown station type")

    def destroy(self) -> None:
        """Mark station as destroyed."""
        self.is_active = False
        self.stored_ships = 0

    def apply_attack_bonus(self, is_offense: bool) -> int:
        """Get attack bonus from this station."""
        if not self.is_active:
            return 0

        if self.station_type == StationType.BATTLE_STATION and is_offense:
            return 3
        if self.station_type == StationType.SHIELD_GENERATOR and not is_offense:
            return 3
        return 0

    def get_max_ships_bonus(self) -> int:
        """Get bonus to max ships that can be committed."""
        if not self.is_active:
            return 0

        if self.station_type == StationType.LAUNCH_PAD:
            return 1
        return 0

    def get_warp_retrieval_bonus(self) -> int:
        """Get bonus ships retrieved from warp during regroup."""
        if not self.is_active:
            return 0

        if self.station_type == StationType.WARP_GATE:
            return 1
        return 0

    def get_ally_invite_bonus(self) -> int:
        """Get bonus to number of allies that can be invited."""
        if not self.is_active:
            return 0

        if self.station_type == StationType.RELAY_BEACON:
            return 1
        return 0

    def should_draw_card_on_deal(self) -> bool:
        """Check if station grants card draw on successful deal."""
        return self.is_active and self.station_type == StationType.TRADING_POST

    def should_draw_card_on_win(self, is_offense: bool) -> bool:
        """Check if station grants card draw on win."""
        return (self.is_active and
                self.station_type == StationType.COMMAND_CENTER and
                is_offense)

    def should_draw_card_on_turn_start(self, hand_size: int) -> bool:
        """Check if station grants card draw at turn start."""
        return (self.is_active and
                self.station_type == StationType.RESOURCE_HUB and
                hand_size < 4)

    def should_preview_destiny(self) -> bool:
        """Check if station allows previewing destiny deck."""
        return self.is_active and self.station_type == StationType.OBSERVATORY

    def can_prevent_warp(self) -> bool:
        """Check if station can prevent a ship from going to warp."""
        return self.is_active and self.station_type == StationType.REPAIR_BAY

    def store_ship(self) -> bool:
        """Try to store a ship in the docking bay."""
        if (self.is_active and
            self.station_type == StationType.DOCKING_BAY and
            self.stored_ships < 2):
            self.stored_ships += 1
            return True
        return False

    def deploy_ships(self, count: int = None) -> int:
        """Deploy stored ships from docking bay."""
        if not self.is_active or self.station_type != StationType.DOCKING_BAY:
            return 0

        if count is None:
            count = self.stored_ships

        deployed = min(count, self.stored_ships)
        self.stored_ships -= deployed
        return deployed


@dataclass
class SpaceStationManager:
    """Manages all space stations in a game."""
    stations: Dict[str, List[SpaceStation]] = field(default_factory=dict)
    available_types: List[StationType] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if not self.available_types:
            self.available_types = list(StationType)

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator."""
        self._rng = rng

    def deal_starting_stations(
        self,
        players: List["Player"],
        stations_per_player: int = 1
    ) -> None:
        """
        Deal starting space stations to each player.

        Each player gets to choose from 2 drawn stations.
        For simulation, we randomly pick one.
        """
        for player in players:
            self.stations[player.name] = []

            # Draw 2 station types, pick one (randomly for AI)
            available = self.available_types.copy()
            if len(available) >= 2:
                choices = self._rng.sample(available, 2)
                chosen = self._rng.choice(choices)
            elif available:
                chosen = available[0]
            else:
                continue

            # Create and assign station
            station = SpaceStation(
                station_type=chosen,
                owner=player
            )
            self.stations[player.name].append(station)

    def build_station(
        self,
        player: "Player",
        planet: "Planet",
        station_type: Optional[StationType] = None
    ) -> Optional[SpaceStation]:
        """
        Build a new space station on a planet.

        Args:
            player: The player building the station
            planet: The planet to build on
            station_type: Type to build (random if not specified)

        Returns:
            The built station, or None if building failed
        """
        if player.name not in self.stations:
            self.stations[player.name] = []

        # Check if planet already has a station
        for station in self.stations[player.name]:
            if station.planet == planet and station.is_active:
                return None  # Already has station

        # Determine station type
        if station_type is None:
            available = self.available_types.copy()
            # Remove types already built by this player
            for existing in self.stations[player.name]:
                if existing.is_active and existing.station_type in available:
                    available.remove(existing.station_type)

            if not available:
                return None

            station_type = self._rng.choice(available)

        # Create station
        station = SpaceStation(
            station_type=station_type,
            planet=planet,
            owner=player
        )
        self.stations[player.name].append(station)
        return station

    def get_player_stations(
        self,
        player: "Player",
        active_only: bool = True
    ) -> List[SpaceStation]:
        """Get all stations owned by a player."""
        if player.name not in self.stations:
            return []

        stations = self.stations[player.name]
        if active_only:
            return [s for s in stations if s.is_active]
        return stations

    def get_station_on_planet(
        self,
        planet: "Planet"
    ) -> Optional[SpaceStation]:
        """Get the active station on a specific planet, if any."""
        for player_stations in self.stations.values():
            for station in player_stations:
                if station.planet == planet and station.is_active:
                    return station
        return None

    def check_station_destruction(
        self,
        planet: "Planet",
        player_name: str
    ) -> Optional[SpaceStation]:
        """
        Check if a station should be destroyed because
        the player lost all ships on that planet.

        Returns destroyed station if applicable.
        """
        if player_name not in self.stations:
            return None

        for station in self.stations[player_name]:
            if (station.planet == planet and
                station.is_active and
                not planet.has_colony(player_name)):
                station.destroy()
                return station
        return None

    def get_attack_bonus(self, player: "Player", is_offense: bool) -> int:
        """Get total attack bonus from player's stations."""
        total = 0
        for station in self.get_player_stations(player):
            total += station.apply_attack_bonus(is_offense)
        return total

    def get_max_ships_bonus(self, player: "Player") -> int:
        """Get bonus to maximum ships player can commit."""
        total = 0
        for station in self.get_player_stations(player):
            total += station.get_max_ships_bonus()
        return total

    def get_warp_retrieval_bonus(self, player: "Player") -> int:
        """Get bonus to ships retrieved from warp."""
        total = 0
        for station in self.get_player_stations(player):
            total += station.get_warp_retrieval_bonus()
        return total

    def get_ally_invite_bonus(self, player: "Player") -> int:
        """Get bonus to allies that can be invited."""
        total = 0
        for station in self.get_player_stations(player):
            total += station.get_ally_invite_bonus()
        return total

    def on_successful_deal(
        self,
        player: "Player",
        game: "Game"
    ) -> int:
        """
        Handle successful deal - draw cards from Trading Post.
        Returns number of cards drawn.
        """
        cards_drawn = 0
        for station in self.get_player_stations(player):
            if station.should_draw_card_on_deal():
                card = game.cosmic_deck.draw()
                if card:
                    player.add_card(card)
                    cards_drawn += 1
        return cards_drawn

    def on_encounter_win(
        self,
        player: "Player",
        game: "Game",
        is_offense: bool
    ) -> int:
        """
        Handle encounter win - draw cards from Command Center.
        Returns number of cards drawn.
        """
        cards_drawn = 0
        for station in self.get_player_stations(player):
            if station.should_draw_card_on_win(is_offense):
                card = game.cosmic_deck.draw()
                if card:
                    player.add_card(card)
                    cards_drawn += 1
        return cards_drawn

    def on_turn_start(
        self,
        player: "Player",
        game: "Game"
    ) -> int:
        """
        Handle turn start - draw cards from Resource Hub.
        Returns number of cards drawn.
        """
        cards_drawn = 0
        for station in self.get_player_stations(player):
            if station.should_draw_card_on_turn_start(len(player.hand)):
                card = game.cosmic_deck.draw()
                if card:
                    player.add_card(card)
                    cards_drawn += 1
        return cards_drawn

    def can_preview_destiny(self, player: "Player") -> bool:
        """Check if player can preview destiny deck."""
        for station in self.get_player_stations(player):
            if station.should_preview_destiny():
                return True
        return False

    def try_prevent_warp(
        self,
        player: "Player"
    ) -> Optional[SpaceStation]:
        """
        Try to use Repair Bay to prevent a ship from going to warp.
        Returns the station used, or None.
        """
        for station in self.get_player_stations(player):
            if station.can_prevent_warp():
                # Mark as used for this encounter (would need tracking)
                return station
        return None

    def get_deployable_ships(self, player: "Player") -> int:
        """Get total ships that can be deployed from Docking Bays."""
        total = 0
        for station in self.get_player_stations(player):
            if station.station_type == StationType.DOCKING_BAY:
                total += station.stored_ships
        return total

    def deploy_docked_ships(self, player: "Player", count: int) -> int:
        """Deploy ships from Docking Bays."""
        deployed = 0
        for station in self.get_player_stations(player):
            if station.station_type == StationType.DOCKING_BAY:
                deployed += station.deploy_ships(count - deployed)
                if deployed >= count:
                    break
        return deployed
