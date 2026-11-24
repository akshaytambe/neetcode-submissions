class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for index, num in enumerate(nums):
            if index != num:
                return index
        return index+1