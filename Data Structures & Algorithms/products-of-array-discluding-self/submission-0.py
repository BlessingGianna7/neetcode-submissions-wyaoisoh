class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        def suffix(n, nums):
            prod = math.prod(nums[i + 1:])
            return prod

        def prefix(n, nums):   
            prod = math.prod(nums[:i])
            return prod

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix(i, nums))
            elif i == len(nums) - 1:
                res.append(prefix(i, nums))
            else:
                res.append(suffix(i, nums) * prefix(i, nums))  

        return res    