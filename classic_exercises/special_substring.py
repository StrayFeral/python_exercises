class SpecialSubstring:
    """Find the length of the longest substring with at most K normal
    characters.

    NOTE: Input string contains only lower case characters.
    We use the sliding window technique.

    Input : P="normal", Q="00000000000000000000000000", K=1
    Output : 1
    Explanation : In string Q all characters are normal.
    Hence, we can select any substring of length 1.


    Input : P="giraffe", Q="01111001111111111011111111", K=2
    Output : 3
    Explanation : Normal characters in P from Q are {a, f, g, r}.
    Therefore, possible substrings with at most 2 normal characters are
    {gir, ira, ffe}.
    The maximum length of all substring is 3.

    Hint: The actual char is totally irrelevant. Once we convert the
    entire input string to a string of just 0 and 1 it all becomes
    very clear.
    """

    # DEFINITIONS
    NORMAL_CHAR: str = "0"
    SPECIAL_CHAR: str = "1"
    ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, p: str, char_value: str, k: int) -> None:
        self._p: str = p
        # self._cval: str = char_value
        self._k: int = k

        # Speeding up a bit: preparing a character map up-front
        self._map = dict(zip([*self.ALPHABET], [*char_value]))

    def max_normal_substring_length(self) -> int:
        # While variable names like k, p, q, n are ambiguous
        # this is for consistency with the programming books
        k: int = self._k
        p: str = self._p
        # Q was supposed to be the character_value string
        # but we already built a character map and don't need it
        # q: str = self._cval
        n: int = len(p)

        result: int = 0

        if k == 0:
            return result  # So far it is zero anyway

        # Count of normal chars in the current window
        normal_char_count: int = 0

        # Window boundaries indexes
        left: int = 0
        right: int = 0

        # Iterating from the start to the end of the input string
        while right < n:
            while right < n and normal_char_count < k:
                if self._map[p[right]] == self.NORMAL_CHAR:
                    if normal_char_count == k:
                        break
                    normal_char_count += 1

                right += 1
                result = max(result, right - left)

            while left < right:
                if self._map[p[left]] == self.NORMAL_CHAR:
                    normal_char_count -= 1

                left += 1
                if normal_char_count < k:
                    break

        return result
