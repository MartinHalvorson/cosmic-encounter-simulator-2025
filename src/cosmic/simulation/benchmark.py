"""
Benchmarking utilities for Cosmic Encounter simulations.

Provides tools for measuring and comparing simulation performance.
"""

import time
import statistics
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Callable

from ..game import Game
from ..types import GameConfig, SimulationConfig
from .runner import Simulator


@dataclass
class BenchmarkResult:
    """Result of a benchmark run."""
    name: str
    total_games: int
    total_time_seconds: float
    games_per_second: float
    avg_time_per_game_ms: float
    min_time_per_game_ms: float
    max_time_per_game_ms: float
    std_dev_ms: float
    percentile_50_ms: float
    percentile_95_ms: float
    percentile_99_ms: float
    memory_usage_mb: Optional[float] = None

    def summary(self) -> str:
        """Generate a text summary of the benchmark."""
        lines = [
            f"Benchmark: {self.name}",
            "-" * 50,
            f"Total games: {self.total_games:,}",
            f"Total time: {self.total_time_seconds:.2f}s",
            f"Throughput: {self.games_per_second:.1f} games/second",
            "",
            "Per-game timing:",
            f"  Average: {self.avg_time_per_game_ms:.3f}ms",
            f"  Min: {self.min_time_per_game_ms:.3f}ms",
            f"  Max: {self.max_time_per_game_ms:.3f}ms",
            f"  Std Dev: {self.std_dev_ms:.3f}ms",
            "",
            "Percentiles:",
            f"  50th (median): {self.percentile_50_ms:.3f}ms",
            f"  95th: {self.percentile_95_ms:.3f}ms",
            f"  99th: {self.percentile_99_ms:.3f}ms",
        ]
        if self.memory_usage_mb is not None:
            lines.append(f"\nMemory usage: {self.memory_usage_mb:.1f}MB")
        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "total_games": self.total_games,
            "total_time_seconds": self.total_time_seconds,
            "games_per_second": self.games_per_second,
            "avg_time_per_game_ms": self.avg_time_per_game_ms,
            "min_time_per_game_ms": self.min_time_per_game_ms,
            "max_time_per_game_ms": self.max_time_per_game_ms,
            "std_dev_ms": self.std_dev_ms,
            "percentile_50_ms": self.percentile_50_ms,
            "percentile_95_ms": self.percentile_95_ms,
            "percentile_99_ms": self.percentile_99_ms,
            "memory_usage_mb": self.memory_usage_mb,
        }


@dataclass
class Benchmark:
    """Benchmarking tool for simulation performance."""
    warmup_games: int = 10
    measure_memory: bool = False

    def run(
        self,
        name: str,
        num_games: int = 100,
        num_players: int = 5,
        seed: Optional[int] = None,
    ) -> BenchmarkResult:
        """
        Run a benchmark measuring individual game times.

        Args:
            name: Name for this benchmark run
            num_games: Number of games to run
            num_players: Players per game
            seed: Random seed for reproducibility

        Returns:
            BenchmarkResult with detailed timing statistics
        """
        game_times: List[float] = []
        memory_before = None

        # Measure memory if requested
        if self.measure_memory:
            try:
                import tracemalloc
                tracemalloc.start()
                memory_before = tracemalloc.get_traced_memory()[0]
            except ImportError:
                pass

        # Warmup phase
        for _ in range(self.warmup_games):
            game = Game(config=GameConfig(num_players=num_players, seed=seed))
            game.setup()
            game.play()

        # Measurement phase
        start_total = time.perf_counter()
        for i in range(num_games):
            game_seed = seed + i if seed else None
            game = Game(config=GameConfig(num_players=num_players, seed=game_seed))

            start_game = time.perf_counter()
            game.setup()
            game.play()
            end_game = time.perf_counter()

            game_times.append((end_game - start_game) * 1000)  # Convert to ms

        end_total = time.perf_counter()
        total_time = end_total - start_total

        # Calculate memory usage
        memory_usage = None
        if self.measure_memory and memory_before is not None:
            try:
                import tracemalloc
                current, peak = tracemalloc.get_traced_memory()
                memory_usage = (peak - memory_before) / (1024 * 1024)  # Convert to MB
                tracemalloc.stop()
            except ImportError:
                pass

        # Calculate statistics
        sorted_times = sorted(game_times)
        n = len(game_times)

        return BenchmarkResult(
            name=name,
            total_games=num_games,
            total_time_seconds=total_time,
            games_per_second=num_games / total_time if total_time > 0 else 0,
            avg_time_per_game_ms=statistics.mean(game_times),
            min_time_per_game_ms=min(game_times),
            max_time_per_game_ms=max(game_times),
            std_dev_ms=statistics.stdev(game_times) if n > 1 else 0,
            percentile_50_ms=sorted_times[n // 2],
            percentile_95_ms=sorted_times[int(n * 0.95)],
            percentile_99_ms=sorted_times[int(n * 0.99)],
            memory_usage_mb=memory_usage,
        )

    def compare(
        self,
        benchmarks: List[Dict[str, Any]],
        num_games: int = 100,
    ) -> List[BenchmarkResult]:
        """
        Compare multiple benchmark configurations.

        Args:
            benchmarks: List of dicts with 'name', 'num_players', etc.
            num_games: Number of games per benchmark

        Returns:
            List of BenchmarkResult objects
        """
        results = []
        for config in benchmarks:
            name = config.get("name", "Unnamed")
            num_players = config.get("num_players", 5)
            seed = config.get("seed")

            result = self.run(
                name=name,
                num_games=num_games,
                num_players=num_players,
                seed=seed,
            )
            results.append(result)
            print(f"Completed: {name} - {result.games_per_second:.1f} games/s")

        return results

    def profile_function(
        self,
        func: Callable[[], Any],
        name: str,
        iterations: int = 100,
    ) -> BenchmarkResult:
        """
        Profile a specific function's execution time.

        Args:
            func: Function to profile (no arguments)
            name: Name for this benchmark
            iterations: Number of times to call the function

        Returns:
            BenchmarkResult with timing statistics
        """
        times: List[float] = []

        # Warmup
        for _ in range(min(10, iterations // 10)):
            func()

        # Measurement
        start_total = time.perf_counter()
        for _ in range(iterations):
            start = time.perf_counter()
            func()
            end = time.perf_counter()
            times.append((end - start) * 1000)
        end_total = time.perf_counter()

        sorted_times = sorted(times)
        n = len(times)

        return BenchmarkResult(
            name=name,
            total_games=iterations,
            total_time_seconds=end_total - start_total,
            games_per_second=iterations / (end_total - start_total),
            avg_time_per_game_ms=statistics.mean(times),
            min_time_per_game_ms=min(times),
            max_time_per_game_ms=max(times),
            std_dev_ms=statistics.stdev(times) if n > 1 else 0,
            percentile_50_ms=sorted_times[n // 2],
            percentile_95_ms=sorted_times[int(n * 0.95)],
            percentile_99_ms=sorted_times[int(n * 0.99)],
        )


def run_quick_benchmark(
    num_games: int = 100,
    num_players: int = 5,
    show_results: bool = True,
) -> BenchmarkResult:
    """
    Run a quick benchmark with default settings.

    Args:
        num_games: Number of games to run
        num_players: Players per game
        show_results: Whether to print results

    Returns:
        BenchmarkResult
    """
    benchmark = Benchmark()
    result = benchmark.run(
        name=f"Quick benchmark ({num_players} players)",
        num_games=num_games,
        num_players=num_players,
    )

    if show_results:
        print(result.summary())

    return result


def compare_player_counts(
    num_games: int = 50,
    player_counts: Optional[List[int]] = None,
) -> List[BenchmarkResult]:
    """
    Compare performance across different player counts.

    Args:
        num_games: Number of games per player count
        player_counts: List of player counts to test

    Returns:
        List of BenchmarkResult objects
    """
    if player_counts is None:
        player_counts = [3, 4, 5, 6]

    benchmark = Benchmark()
    results = []

    for count in player_counts:
        result = benchmark.run(
            name=f"{count}-player games",
            num_games=num_games,
            num_players=count,
        )
        results.append(result)
        print(f"{count} players: {result.games_per_second:.1f} games/s "
              f"(avg {result.avg_time_per_game_ms:.2f}ms)")

    return results


def print_comparison_table(results: List[BenchmarkResult]) -> None:
    """Print a comparison table of benchmark results."""
    print("\n" + "=" * 80)
    print("BENCHMARK COMPARISON")
    print("=" * 80)
    print(f"{'Name':<30} {'Games/s':>10} {'Avg (ms)':>10} {'P95 (ms)':>10} {'P99 (ms)':>10}")
    print("-" * 80)

    for result in results:
        print(f"{result.name:<30} "
              f"{result.games_per_second:>10.1f} "
              f"{result.avg_time_per_game_ms:>10.3f} "
              f"{result.percentile_95_ms:>10.3f} "
              f"{result.percentile_99_ms:>10.3f}")

    print("=" * 80)
