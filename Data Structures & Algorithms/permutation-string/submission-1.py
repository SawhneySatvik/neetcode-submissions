from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        freq = Counter(s1)
        window = Counter(s2[:n])

        if window == freq:
            return True

        for r in range(n, len(s2)):
            window[s2[r-n]] -= 1
            window[s2[r]] += 1
            if window == freq:
                return True

        return False