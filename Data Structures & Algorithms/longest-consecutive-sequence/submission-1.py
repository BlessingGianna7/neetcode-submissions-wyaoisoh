class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in store:
            if (num - 1) not in store:
                streak = 0
                length = 0
                while (num + length) in store:
                    streak += 1
                    length += 1
                    res = max(streak, res)
        return res        

            