class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        seen = set()
        res = 0

        for hi in range(len(s)):
            while s[hi] in seen:      # duplicate — shrink left
                seen.remove(s[lo])
                lo += 1
            seen.add(s[hi])           # no duplicate — add and expand
            res = max(res, hi - lo + 1)

        return res      
