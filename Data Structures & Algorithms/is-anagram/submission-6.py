class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = [0]*26

        for a, b in zip(s, t):
            chars[ord(a)-97] += 1
            chars[ord(b)-97] -= 1
        
        return all(count == 0 for count in chars)
