class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_area = 0
        l, r = 0, len(nums)-1

        for i, num in enumerate(nums):
            max_area = max(max_area, min(nums[l], nums[r]) * (r-l))
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        
        return max_area