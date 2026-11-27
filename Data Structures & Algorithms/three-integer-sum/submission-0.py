class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add(tuple((nums[i], nums[l], nums[r])))
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(l) for l in res]
