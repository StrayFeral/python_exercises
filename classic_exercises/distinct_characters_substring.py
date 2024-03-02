from collections import defaultdict


class DistinctCharacters:
    """Find the length of the longest substring with at most
    K-distinct characters.
    
    2024 by Evgueni Antonov
    Evgueni.Antonov@gmail.com

    NOTE: Input string contains only lower case characters.
    We use the sliding window technique.

    Input : P="aabaccacb", K=1
    Output : 3
    """

    def __init__(self, p: str, k: int) -> None:
        self._p: str = p
        self._k: int = k

    def substring_length(self) -> int:
        k: int = self._k
        p: str = self._p
        n: int = len(p)

        result: int = 0
        distinct_chars: defaultdict = defaultdict(lambda: 0)

        if len(p) == 0 or k == 0:
            return result  # So far it is zero anyway

        left: int = 0
        right: int = 0

        while right < n:
            while right < n and len(distinct_chars.keys()) <= k:
                distinct_chars[p[right]] += 1
                result = max(result, sum(distinct_chars.values()))
                right += 1
                if (
                    right < n
                    and p[right] not in distinct_chars.keys()
                    and len(distinct_chars.keys()) == k
                ):
                    break

            while right < n and left < right and len(distinct_chars.keys()) >= k:
                distinct_chars[p[left]] -= 1
                if distinct_chars[p[left]] == 0:
                    del distinct_chars[p[left]]
                left += 1

        return result
