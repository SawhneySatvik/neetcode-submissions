class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums_set:
                pos = num
                cur = 1

                while pos + 1 in nums_set:
                    cur += 1
                    pos += 1
                
                res = max(res, cur)

        return res
            