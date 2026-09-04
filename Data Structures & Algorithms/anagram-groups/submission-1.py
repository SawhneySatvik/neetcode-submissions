class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            count = [0]*26

            for w in word:
                count[ord(w)-ord('a')] += 1
            
            key = tuple(count)
            
            if key in group:
                group[key].append(word)
            
            else:
                group[key] = [word]
        
        res = []

        for key, words in group.items():
            res.append(words)
        
        return res