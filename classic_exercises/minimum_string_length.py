class MinimumStringLength:
    """Leetcode 1750: Minimum Length of String After
    Deleting Similar Ends
    """

    def calculate(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            c: str = s[0]
            while len(s) > 0 and s[0] == c:
                s = s[1:]
            while len(s) > 0 and s[-1] == c:
                s = s[:-1]
        return len(s)
