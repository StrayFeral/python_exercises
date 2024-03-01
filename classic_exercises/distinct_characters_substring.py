class DistinctCharacters:
    """Find the length of the longest substring with at most
    K-distinct characters.

    NOTE: Input string contains only lower case characters.
    We use the sliding window technique.

    Input : P="aabaccacb", K=1
    Output : 3
    """

    def __init__(self, p: str, k: int) -> None:
        self._p: str = p
        self._k: int = k

    def substring_length(self) -> int:
        """Solution by MLTechTrack youtube channel."""

        k: int = self._k
        p: str = self._p
        n: int = len(p)

        result: int = 0
        distinct_chars: dict = {}

        if len(p) == 0 or k == 0:
            return result  # So far it is zero anyway

        left: int = 0
        right: int = 0

        while right < n:
            if p[right] not in distinct_chars:
                k -= 1
            distinct_chars[p[right]] = right

            while k < 0:
                if distinct_chars[p[left]] == left:
                    k += 1
                    del distinct_chars[p[left]]
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result


if __name__ == "__main__":
    o = DistinctCharacters("ecebaa", 2)
    actual = o.substring_length()
    expected = 3
    print(f"result = {actual}, expected = {expected}")
    assert actual == expected
