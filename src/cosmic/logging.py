"""
Game Logging System for Cosmic Encounter Simulator.

Provides comprehensive logging for:
- Game events (turns, encounters, outcomes)
- Player actions (card plays, alliances, ship movements)
- Power activations and effects
- Debug information for troubleshooting

Logs can be output to console, file, or collected in memory for analysis.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Callable
from enum import Enum, auto
from datetime import datetime
import json


class LogLevel(Enum):
    """Logging levels."""
    DEBUG = 0
    INFO = 1
    EVENT = 2
    POWER = 3
    RESULT = 4
    WARNING = 5
    ERROR = 6


class EventType(Enum):
    """Types of game events."""
    GAME_START = auto()
    GAME_END = auto()
    TURN_START = auto()
    TURN_END = auto()
    ENCOUNTER_START = auto()
    ENCOUNTER_END = auto()
    PHASE_CHANGE = auto()
    DESTINY_DRAW = auto()
    ALLIANCE_INVITE = auto()
    ALLIANCE_JOIN = auto()
    CARD_PLAY = auto()
    CARD_REVEAL = auto()
    POWER_ACTIVATE = auto()
    POWER_EFFECT = auto()
    SHIPS_MOVE = auto()
    SHIPS_TO_WARP = auto()
    SHIPS_FROM_WARP = auto()
    COLONY_GAIN = auto()
    COLONY_LOSE = auto()
    CARD_DRAW = auto()
    CARD_DISCARD = auto()
    COMBAT_RESULT = auto()
    DEAL_ATTEMPT = auto()
    DEAL_SUCCESS = auto()
    DEAL_FAIL = auto()
    ALTERNATE_WIN = auto()


@dataclass
class LogEntry:
    """A single log entry."""
    timestamp: str
    turn: int
    phase: str
    event_type: EventType
    level: LogLevel
    player: Optional[str]
    message: str
    data: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "turn": self.turn,
            "phase": self.phase,
            "event_type": self.event_type.name,
            "level": self.level.name,
            "player": self.player,
            "message": self.message,
            "data": self.data,
        }

    def __str__(self) -> str:
        player_str = f"[{self.player}] " if self.player else ""
        return f"T{self.turn:03d} {self.phase:12s} {player_str}{self.message}"


class GameLogger:
    """
    Logs game events and state changes.

    Usage:
        logger = GameLogger(level=LogLevel.EVENT)
        logger.log_event(EventType.GAME_START, "Game started with 5 players")
        ...
        print(logger.get_summary())
    """

    def __init__(
        self,
        level: LogLevel = LogLevel.INFO,
        console_output: bool = False,
        max_entries: int = 10000
    ):
        self.level = level
        self.console_output = console_output
        self.max_entries = max_entries

        self.entries: List[LogEntry] = []
        self.current_turn = 0
        self.current_phase = "SETUP"
        self.game_id: Optional[str] = None

        # Statistics
        self.power_uses: Dict[str, int] = {}
        self.encounter_count = 0
        self.deal_count = 0

    def set_turn(self, turn: int) -> None:
        """Update current turn number."""
        self.current_turn = turn

    def set_phase(self, phase: str) -> None:
        """Update current game phase."""
        self.current_phase = phase

    def log(
        self,
        event_type: EventType,
        message: str,
        player: Optional[str] = None,
        level: LogLevel = LogLevel.INFO,
        data: Optional[Dict[str, Any]] = None
    ) -> None:
        """Log a game event."""
        if level.value < self.level.value:
            return

        if len(self.entries) >= self.max_entries:
            # Remove oldest entries
            self.entries = self.entries[1000:]

        entry = LogEntry(
            timestamp=datetime.now().isoformat(),
            turn=self.current_turn,
            phase=self.current_phase,
            event_type=event_type,
            level=level,
            player=player,
            message=message,
            data=data or {},
        )

        self.entries.append(entry)

        if self.console_output:
            print(f"[{level.name}] {entry}")

    def log_game_start(
        self,
        player_names: List[str],
        alien_map: Dict[str, str]
    ) -> None:
        """Log game start."""
        self.game_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log(
            EventType.GAME_START,
            f"Game started with {len(player_names)} players",
            level=LogLevel.RESULT,
            data={"players": player_names, "aliens": alien_map}
        )

    def log_game_end(
        self,
        winners: List[str],
        turn_count: int,
        final_colonies: Dict[str, int]
    ) -> None:
        """Log game end."""
        self.log(
            EventType.GAME_END,
            f"Game ended on turn {turn_count}. Winners: {', '.join(winners)}",
            level=LogLevel.RESULT,
            data={
                "winners": winners,
                "turns": turn_count,
                "final_colonies": final_colonies
            }
        )

    def log_turn_start(self, player: str) -> None:
        """Log turn start."""
        self.log(
            EventType.TURN_START,
            f"Turn {self.current_turn} begins",
            player=player,
            level=LogLevel.EVENT
        )

    def log_encounter(
        self,
        offense: str,
        defense: str,
        planet_id: int
    ) -> None:
        """Log encounter start."""
        self.encounter_count += 1
        self.log(
            EventType.ENCOUNTER_START,
            f"Encounter: {offense} attacks {defense} on planet {planet_id}",
            level=LogLevel.EVENT,
            data={"offense": offense, "defense": defense, "planet": planet_id}
        )

    def log_alliance(
        self,
        player: str,
        side: str,
        ships: int
    ) -> None:
        """Log alliance joining."""
        self.log(
            EventType.ALLIANCE_JOIN,
            f"{player} allies with {side} ({ships} ships)",
            player=player,
            level=LogLevel.EVENT,
            data={"side": side, "ships": ships}
        )

    def log_card_play(
        self,
        player: str,
        card_type: str,
        value: Optional[int] = None
    ) -> None:
        """Log card play."""
        value_str = f" ({value})" if value is not None else ""
        self.log(
            EventType.CARD_PLAY,
            f"Plays {card_type}{value_str}",
            player=player,
            level=LogLevel.EVENT,
            data={"card_type": card_type, "value": value}
        )

    def log_power_use(
        self,
        player: str,
        power_name: str,
        effect: str
    ) -> None:
        """Log power activation."""
        self.power_uses[power_name] = self.power_uses.get(power_name, 0) + 1
        self.log(
            EventType.POWER_ACTIVATE,
            f"Uses {power_name}: {effect}",
            player=player,
            level=LogLevel.POWER,
            data={"power": power_name, "effect": effect}
        )

    def log_combat_result(
        self,
        winner_side: str,
        offense_total: int,
        defense_total: int
    ) -> None:
        """Log combat resolution."""
        self.log(
            EventType.COMBAT_RESULT,
            f"{winner_side} wins ({offense_total} vs {defense_total})",
            level=LogLevel.EVENT,
            data={
                "winner": winner_side,
                "offense_total": offense_total,
                "defense_total": defense_total
            }
        )

    def log_deal(self, success: bool, players: List[str]) -> None:
        """Log deal attempt."""
        self.deal_count += 1
        event = EventType.DEAL_SUCCESS if success else EventType.DEAL_FAIL
        status = "successful" if success else "failed"
        self.log(
            event,
            f"Deal {status} between {', '.join(players)}",
            level=LogLevel.EVENT,
            data={"success": success, "players": players}
        )

    def log_ships_to_warp(
        self,
        player: str,
        count: int,
        source: str
    ) -> None:
        """Log ships going to warp."""
        self.log(
            EventType.SHIPS_TO_WARP,
            f"{count} ships to warp ({source})",
            player=player,
            level=LogLevel.EVENT,
            data={"count": count, "source": source}
        )

    def log_colony_change(
        self,
        player: str,
        gain: bool,
        planet_id: int
    ) -> None:
        """Log colony gain or loss."""
        event = EventType.COLONY_GAIN if gain else EventType.COLONY_LOSE
        action = "gains" if gain else "loses"
        self.log(
            event,
            f"{action} colony on planet {planet_id}",
            player=player,
            level=LogLevel.EVENT,
            data={"planet": planet_id, "gain": gain}
        )

    def log_warning(self, message: str, player: Optional[str] = None) -> None:
        """Log a warning."""
        self.log(
            EventType.POWER_EFFECT,
            message,
            player=player,
            level=LogLevel.WARNING
        )

    def log_error(self, message: str, player: Optional[str] = None) -> None:
        """Log an error."""
        self.log(
            EventType.POWER_EFFECT,
            message,
            player=player,
            level=LogLevel.ERROR
        )

    def get_entries(
        self,
        event_type: Optional[EventType] = None,
        player: Optional[str] = None,
        level: Optional[LogLevel] = None
    ) -> List[LogEntry]:
        """Get filtered log entries."""
        entries = self.entries

        if event_type:
            entries = [e for e in entries if e.event_type == event_type]
        if player:
            entries = [e for e in entries if e.player == player]
        if level:
            entries = [e for e in entries if e.level.value >= level.value]

        return entries

    def get_summary(self) -> str:
        """Get a summary of the logged game."""
        lines = [
            "=" * 60,
            f"GAME LOG SUMMARY (ID: {self.game_id})",
            "=" * 60,
            f"Total entries: {len(self.entries)}",
            f"Encounters: {self.encounter_count}",
            f"Deals: {self.deal_count}",
            "",
            "Power uses:",
        ]

        for power, count in sorted(
            self.power_uses.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]:
            lines.append(f"  {power}: {count}")

        return "\n".join(lines)

    def export_json(self, filepath: str) -> None:
        """Export log to JSON file."""
        data = {
            "game_id": self.game_id,
            "summary": {
                "entries": len(self.entries),
                "encounters": self.encounter_count,
                "deals": self.deal_count,
                "power_uses": self.power_uses,
            },
            "entries": [e.to_dict() for e in self.entries]
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def export_text(self, filepath: str) -> None:
        """Export log to text file."""
        with open(filepath, 'w') as f:
            for entry in self.entries:
                f.write(str(entry) + "\n")

    def clear(self) -> None:
        """Clear all log entries."""
        self.entries.clear()
        self.power_uses.clear()
        self.encounter_count = 0
        self.deal_count = 0


# Global logger instance (optional singleton pattern)
_global_logger: Optional[GameLogger] = None


def get_logger() -> GameLogger:
    """Get the global logger instance."""
    global _global_logger
    if _global_logger is None:
        _global_logger = GameLogger()
    return _global_logger


def set_logger(logger: GameLogger) -> None:
    """Set the global logger instance."""
    global _global_logger
    _global_logger = logger
