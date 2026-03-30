class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        seen = set()
        res = 0

        for hi in range(len(s)):
            while s[hi] in seen:      
                seen.remove(s[lo])
                lo += 1
            seen.add(s[hi])           
            res = max(res, hi - lo + 1)

        return res      
