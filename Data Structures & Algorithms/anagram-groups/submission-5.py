class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in res:
                res[key].append(s)
            
            else:
                res[key] = [s]
        
        res_list = []

        for groups in res.values():
            res_list.append(groups)
        
        return res_list
