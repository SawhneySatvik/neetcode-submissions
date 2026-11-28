from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        freq = Counter(s1)

        for l in range(len(s2) - n + 1):
            local = Counter(s2[l:l + n])

            if local == freq:
                return True

        return False