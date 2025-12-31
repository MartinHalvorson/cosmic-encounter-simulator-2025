"""
Tech Powers - Aliens with technological and mechanical abilities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Android(AlienPower):
    """
    Android - Artificial Being.
    Your encounter cards cannot be affected by other powers.
    """
    name: str = field(default="Android", init=False)
    description: str = field(default="Cards immune to power effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Automaton(AlienPower):
    """
    Automaton - Machine Mind.
    When you lose ships, they return to colonies instead of warp.
    """
    name: str = field(default="Automaton", init=False)
    description: str = field(default="Ships return to colonies when lost.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clockwork(AlienPower):
    """
    Clockwork - Precision Timing.
    You may look at the top 5 cards of the cosmic deck at any time.
    """
    name: str = field(default="Clockwork", init=False)
    description: str = field(default="See top 5 cosmic deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cyborg(AlienPower):
    """
    Cyborg - Enhanced Being.
    Add +2 to your total in every encounter.
    """
    name: str = field(default="Cyborg", init=False)
    description: str = field(default="Add +2 to all encounter totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 to total."""
        return total + 2


@dataclass
class Database(AlienPower):
    """
    Database - Information Storage.
    You may look at any player's hand once per encounter.
    """
    name: str = field(default="Database", init=False)
    description: str = field(default="Look at one hand per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drone(AlienPower):
    """
    Drone - Remote Unit.
    Your allies can commit 5 ships instead of 4.
    """
    name: str = field(default="Drone", init=False)
    description: str = field(default="Allies commit 5 ships max.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Engineer(AlienPower):
    """
    Engineer - Builder.
    At the start of each turn, you may retrieve one ship from the warp.
    """
    name: str = field(default="Engineer", init=False)
    description: str = field(default="Retrieve ship at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Factory(AlienPower):
    """
    Factory - Production.
    When you win as offense, draw 2 extra cards.
    """
    name: str = field(default="Factory", init=False)
    description: str = field(default="Draw 2 cards on offensive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Generator(AlienPower):
    """
    Generator - Power Source.
    Once per encounter, add +5 to your total.
    """
    name: str = field(default="Generator", init=False)
    description: str = field(default="Add +5 once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 to total."""
        return total + 5


@dataclass
class Hacker(AlienPower):
    """
    Hacker - System Breaker.
    When you receive compensation, take it from any player.
    """
    name: str = field(default="Hacker", init=False)
    description: str = field(default="Take compensation from anyone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Interface(AlienPower):
    """
    Interface - Connection.
    When you ally, you also get the rewards of the main player.
    """
    name: str = field(default="Interface", init=False)
    description: str = field(default="Get main player rewards as ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Laser(AlienPower):
    """
    Laser - Focused Beam.
    When attacking with 1 ship, add +8 to your total.
    """
    name: str = field(default="Laser", init=False)
    description: str = field(default="+8 when attacking with 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mainframe(AlienPower):
    """
    Mainframe - Central Computer.
    You may see all players' hands at the start of each encounter.
    """
    name: str = field(default="Mainframe", init=False)
    description: str = field(default="See all hands at encounter start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Network(AlienPower):
    """
    Network - Connected System.
    Your colonies count as adjacent for ship movement.
    """
    name: str = field(default="Network", init=False)
    description: str = field(default="Colonies connected for movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Processor(AlienPower):
    """
    Processor - Computing Power.
    Once per turn, discard 2 cards to draw 3.
    """
    name: str = field(default="Processor", init=False)
    description: str = field(default="Discard 2, draw 3 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Radar(AlienPower):
    """
    Radar - Detection System.
    Before cards are revealed, you may look at opponent's card.
    """
    name: str = field(default="Radar", init=False)
    description: str = field(default="See opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Robot(AlienPower):
    """
    Robot - Mechanical Servant.
    Your ships in the warp return automatically after 1 encounter.
    """
    name: str = field(default="Robot", init=False)
    description: str = field(default="Ships return from warp in 1 turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scanner(AlienPower):
    """
    Scanner - Search Device.
    At the start of your turn, look at top 3 destiny cards.
    """
    name: str = field(default="Scanner", init=False)
    description: str = field(default="See top 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sensor(AlienPower):
    """
    Sensor - Detection Array.
    You are always aware when someone targets you with a power.
    """
    name: str = field(default="Sensor", init=False)
    description: str = field(default="Know when targeted by powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Server(AlienPower):
    """
    Server - Data Host.
    When you draw cards, draw 1 extra.
    """
    name: str = field(default="Server", init=False)
    description: str = field(default="Draw 1 extra card always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Terminal(AlienPower):
    """
    Terminal - Access Point.
    You may use any discarded card as if in your hand (once per turn).
    """
    name: str = field(default="Terminal", init=False)
    description: str = field(default="Use discarded card once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Turret(AlienPower):
    """
    Turret - Defense System.
    When defending, add +3 to your total.
    """
    name: str = field(default="Turret", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 when defending."""
        if side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Virus_Alt(AlienPower):
    """
    Virus_Alt - Digital Infection.
    When you win, opponent discards 2 cards.
    """
    name: str = field(default="Virus_Alt", init=False)
    description: str = field(default="Opponent discards 2 on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Android())
AlienRegistry.register(Automaton())
AlienRegistry.register(Clockwork())
AlienRegistry.register(Cyborg())
AlienRegistry.register(Database())
AlienRegistry.register(Drone())
# Engineer already exists - skip registration
# AlienRegistry.register(Engineer())
AlienRegistry.register(Factory())
AlienRegistry.register(Generator())
# Hacker already exists - skip
# AlienRegistry.register(Hacker())
AlienRegistry.register(Interface())
# Laser already exists - skip
# AlienRegistry.register(Laser())
AlienRegistry.register(Mainframe())
AlienRegistry.register(Network())
AlienRegistry.register(Processor())
AlienRegistry.register(Radar())
AlienRegistry.register(Robot())
AlienRegistry.register(Scanner())
AlienRegistry.register(Sensor())
AlienRegistry.register(Server())
AlienRegistry.register(Terminal())
AlienRegistry.register(Turret())
AlienRegistry.register(Virus_Alt())
