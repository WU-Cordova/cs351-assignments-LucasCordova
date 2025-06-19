from datastructures.graph import Node


class HueristicFunction:
    @staticmethod
    def manhattan_distance(node1: Node, node2: Node) -> float:
        x1, y1 = node1.position
        x2, y2 = node2.position
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def euclidean_distance(node1: Node, node2: Node) -> float:
        x1, y1 = node1.position
        x2, y2 = node2.position
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5