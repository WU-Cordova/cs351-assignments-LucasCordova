from __future__ import annotations
from typing import List, Tuple


class Node:
    def __init__(self, name: str, position: Tuple[int, int], cost: float = 1.0) -> None:
        self.name = name
        self.position = position
        self.cost = cost
        self.is_trap = False
        self.neighbors: List[Tuple[Node, float]] = []

    def add_neighbor(self, node: Node, weight: float) -> None:
        self.neighbors.append((node, weight))

    def toggle_trap(self) -> None:
        self.is_trap = not self.is_trap
        self.cost = 5.0 if self.is_trap else 1

    def __lt__(self, other: Node) -> bool:
        return self.cost < other.cost

class Graph:
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes
