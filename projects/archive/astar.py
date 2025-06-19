from typing import Callable, Dict, List
from datastructures.graph import Graph, Node


class AStar:
    @staticmethod
    def search(graph: Graph, 
               start: Node, 
               goal: Node, 
               h_func: Callable[[Node, Node], float],
               f_scores: Dict[Node, float],
               g_scores: Dict[Node, float]) -> List[Node]:
        
        raise NotImplementedError