from __future__ import annotations
from dataclasses import dataclass

from typing import Callable, Generic, List, Optional, Sequence, Tuple
from datastructures.iavltree import IAVLTree, K, V

# class AVLNode(Generic[K, V]):
#     def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
#         self._key = key
#         self._value = value
#         self._left = left
#         self._right = right

#     @property
#     def key(self) -> K: return self._key

#     @key.setter
#     def key(self, new_key: K) -> None: self._key = new_key

@dataclass
class AVLNode(Generic[K, V]):
    def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self._height = 1

class AVLTree(IAVLTree[K,V], Generic[K, V]):
    def __init__(self, starting_sequence: Optional[Sequence[Tuple]]=None):
        self._root = None

        if starting_sequence:
            for key, value in starting_sequence:
                self.insert(key, value)


    def insert(self, key: K, value: V) -> None:
        raise NotImplementedError

    def search(self, key: K) -> V | None:
        raise NotImplementedError

    def delete(self, key: K) -> None:
        raise NotImplementedError

    def inorder(self, visit: Optional[Callable[[V], None]] = None) -> List[K]:
        raise NotImplementedError

    def preorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def postorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def bforder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError

