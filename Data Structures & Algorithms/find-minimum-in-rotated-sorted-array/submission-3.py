class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                # Sorted Array
                result = min(result, nums[l])
                break

            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] >= nums[l]:
                # Search Right
                l = m + 1
            else:
                # Search Left 
                r = m - 1
        

        return result