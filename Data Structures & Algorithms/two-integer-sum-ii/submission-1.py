class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            remaining = target - numbers[i]

            low, high = i+1, len(numbers)-1
            while low <= high:
                mid = (low+high)//2
                if numbers[mid] == remaining:
                    return [i+1, mid+1]
                elif numbers[mid] > remaining:
                    high = mid - 1
                else:
                    low = mid + 1
            
        return [-1, -1]