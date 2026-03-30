class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                 continue
            f = i
            l = i + 1
            r = len(nums) - 1
            
            while(l < r):
                sum_lr = nums[l] + nums[r]
                diff = 0 - nums[f]
                
                if(sum_lr == diff):
                    result.append([nums[f],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif(sum_lr > diff):
                    r -= 1
                else:
                    l += 1
                   
        return result