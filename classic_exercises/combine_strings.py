from typing import List
from collections.abc import Iterator, Iterable


class CustomIterator(Iterator):
    """Iterator which would go beyond the length of the iterable
    until a given end.
    """
    
    def __init__(self, sequence: Iterable, end: int) -> None:
        self._seq: Iterable = sequence
        self._idx: int = 0
        self._end: int = end

    def __next__(self):
        if self._idx < self._end and self._idx < len(self._seq):
            item = self._seq[self._idx]
            self._idx += 1
            return item
        elif self._idx < self._end:
            return ""
        else:
            raise StopIteration


class StringCombinator:
    """Combine two strings as a puzzle."""

    def __init__(self, s1: str, s2: str) -> None:
        self._s1: str = s1
        self._s2: str = s2

    def combine(self) -> str:
        maxlen: int = max(len(self._s1), len(self._s2))
        i1 = CustomIterator(self._s1, maxlen)
        i2 = CustomIterator(self._s2, maxlen)
        l: List[str] = [f"{a}{b}" for a, b in zip(i1, i2)]
        return "".join(l)
