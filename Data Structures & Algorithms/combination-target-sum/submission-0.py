class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target or i >= len(nums):
                return

            path.append(nums[i])
            dfs(i, path, total + nums[i])
            path.pop()

            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res