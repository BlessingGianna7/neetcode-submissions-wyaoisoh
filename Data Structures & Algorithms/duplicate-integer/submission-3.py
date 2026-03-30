class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        # num = (1,2,3)
        if len(num) != len(nums):
            return True
        return False