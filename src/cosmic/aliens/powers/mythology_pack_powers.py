"""
Mythology themed alien powers - Pack 1 (50 aliens).
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Zeus(AlienPower):
    """Zeus - King of gods. +6 always."""
    name: str = field(default="Zeus", init=False)
    description: str = field(default="+6 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Poseidon(AlienPower):
    """Poseidon - Sea god. +5 always."""
    name: str = field(default="Poseidon", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hades(AlienPower):
    """Hades - Underworld god. +5 defending."""
    name: str = field(default="Hades", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Apollo(AlienPower):
    """Apollo - Sun god. +4 attacking."""
    name: str = field(default="Apollo", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Artemis(AlienPower):
    """Artemis - Huntress. +5 attacking."""
    name: str = field(default="Artemis", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Ares(AlienPower):
    """Ares - War god. +6 attacking."""
    name: str = field(default="Ares", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Athena(AlienPower):
    """Athena - Wisdom goddess. +5 always."""
    name: str = field(default="Athena", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hermes(AlienPower):
    """Hermes - Messenger god. +4 always."""
    name: str = field(default="Hermes", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Hephaestus(AlienPower):
    """Hephaestus - Forge god. +4 defending."""
    name: str = field(default="Hephaestus", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Dionysus(AlienPower):
    """Dionysus - Wine god. Random +0-8."""
    name: str = field(default="Dionysus", init=False)
    description: str = field(default="Random +0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 8)
        return total


@dataclass
class Odin(AlienPower):
    """Odin - Allfather. +6 always."""
    name: str = field(default="Odin", init=False)
    description: str = field(default="+6 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Thor(AlienPower):
    """Thor - Thunder god. +6 attacking."""
    name: str = field(default="Thor", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Loki(AlienPower):
    """Loki - Trickster. Random +0-10."""
    name: str = field(default="Loki", init=False)
    description: str = field(default="Random +0-10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 10)
        return total


@dataclass
class Freya(AlienPower):
    """Freya - Love goddess. +4 always."""
    name: str = field(default="Freya", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Tyr(AlienPower):
    """Tyr - War god. +5 attacking."""
    name: str = field(default="Tyr", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Heimdall(AlienPower):
    """Heimdall - Guardian. +5 defending."""
    name: str = field(default="Heimdall", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Ra(AlienPower):
    """Ra - Sun god. +5 always."""
    name: str = field(default="Ra", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Osiris(AlienPower):
    """Osiris - Underworld ruler. +5 defending."""
    name: str = field(default="Osiris", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Isis(AlienPower):
    """Isis - Magic goddess. +4 always."""
    name: str = field(default="Isis", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Anubis(AlienPower):
    """Anubis - Death god. +4 attacking."""
    name: str = field(default="Anubis", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Horus(AlienPower):
    """Horus - Sky god. +5 attacking."""
    name: str = field(default="Horus", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Thoth(AlienPower):
    """Thoth - Wisdom god. +4 always."""
    name: str = field(default="Thoth", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Set(AlienPower):
    """Set - Chaos god. Random +0-10."""
    name: str = field(default="Set", init=False)
    description: str = field(default="Random +0-10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 10)
        return total


@dataclass
class Amaterasu(AlienPower):
    """Amaterasu - Sun goddess. +5 always."""
    name: str = field(default="Amaterasu", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Susanoo(AlienPower):
    """Susanoo - Storm god. +6 attacking."""
    name: str = field(default="Susanoo", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Tsukuyomi(AlienPower):
    """Tsukuyomi - Moon god. +4 defending."""
    name: str = field(default="Tsukuyomi", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Izanagi(AlienPower):
    """Izanagi - Creator god. +5 always."""
    name: str = field(default="Izanagi", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Izanami(AlienPower):
    """Izanami - Death goddess. +4 defending."""
    name: str = field(default="Izanami", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Vishnu(AlienPower):
    """Vishnu - Preserver. +5 defending."""
    name: str = field(default="Vishnu", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Shiva(AlienPower):
    """Shiva - Destroyer. +6 attacking."""
    name: str = field(default="Shiva", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Brahma(AlienPower):
    """Brahma - Creator. +5 always."""
    name: str = field(default="Brahma", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ganesha(AlienPower):
    """Ganesha - Obstacle remover. +4 always."""
    name: str = field(default="Ganesha", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Kali(AlienPower):
    """Kali - Destruction goddess. +5 attacking."""
    name: str = field(default="Kali", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Hanuman(AlienPower):
    """Hanuman - Monkey god. +5 attacking."""
    name: str = field(default="Hanuman", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Quetzalcoatl(AlienPower):
    """Quetzalcoatl - Feathered serpent. +5 always."""
    name: str = field(default="Quetzalcoatl", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Tezcatlipoca(AlienPower):
    """Tezcatlipoca - Smoking mirror. Random +0-8."""
    name: str = field(default="Tezcatlipoca", init=False)
    description: str = field(default="Random +0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 8)
        return total


@dataclass
class Huitzilopochtli(AlienPower):
    """Huitzilopochtli - War god. +6 attacking."""
    name: str = field(default="Huitzilopochtli", init=False)
    description: str = field(default="+6 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Mictlantecuhtli(AlienPower):
    """Mictlantecuhtli - Death god. +5 defending."""
    name: str = field(default="Mictlantecuhtli", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Tlaloc(AlienPower):
    """Tlaloc - Rain god. +4 always."""
    name: str = field(default="Tlaloc", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Morrigan(AlienPower):
    """Morrigan - War goddess. +5 attacking."""
    name: str = field(default="Morrigan", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Lugh(AlienPower):
    """Lugh - Master of all. +5 always."""
    name: str = field(default="Lugh", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Dagda(AlienPower):
    """Dagda - Good god. +5 always."""
    name: str = field(default="Dagda", init=False)
    description: str = field(default="+5 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Brigid(AlienPower):
    """Brigid - Fire goddess. +4 attacking."""
    name: str = field(default="Brigid", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Cernunnos(AlienPower):
    """Cernunnos - Horned god. +4 always."""
    name: str = field(default="Cernunnos", init=False)
    description: str = field(default="+4 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Danu(AlienPower):
    """Danu - Mother goddess. +4 defending."""
    name: str = field(default="Danu", init=False)
    description: str = field(default="+4 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


MYTHOLOGY_PACK_POWERS = [
    Zeus, Poseidon, Hades, Apollo, Artemis, Ares, Athena, Hermes, Hephaestus, Dionysus,
    Odin, Thor, Loki, Freya, Tyr, Heimdall, Ra, Osiris, Isis, Anubis,
    Horus, Thoth, Set, Amaterasu, Susanoo, Tsukuyomi, Izanagi, Izanami, Vishnu, Shiva,
    Brahma, Ganesha, Kali, Hanuman, Quetzalcoatl, Tezcatlipoca, Huitzilopochtli, Mictlantecuhtli,
    Tlaloc, Morrigan, Lugh, Dagda, Brigid, Cernunnos, Danu,
]

for power_class in MYTHOLOGY_PACK_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
