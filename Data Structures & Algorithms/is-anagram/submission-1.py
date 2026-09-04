class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = dict()
        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
            chars[t[i]] = chars.get(t[i], 0) - 1
        
        for chars, count in chars.items():
            if count != 0:
                return False
        
        return True