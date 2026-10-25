class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for index, val in enumerate(nums):
            if val not in seen:
                seen[val] = index
            else:
                return True
        
        return False