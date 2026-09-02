class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i in range(len(nums)):
            if target - nums[i] in need:
                return [need[target - nums[i]], i]
            need[nums[i]] = i
        return [-1, -1]