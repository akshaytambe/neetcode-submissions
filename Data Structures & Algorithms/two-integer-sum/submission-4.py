class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, val in enumerate(nums):
            complement = target - val
            if complement not in seen:
                seen[val] = index
            else:
                return [seen[complement], index]        