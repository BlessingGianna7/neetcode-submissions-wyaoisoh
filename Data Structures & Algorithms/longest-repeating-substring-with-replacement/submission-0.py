class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        lo = 0
        res = 0

        for hi in range(len(s)):
            count[s[hi]] = count.get(s[hi], 0) + 1    # add right
            maxf = max(maxf, count[s[hi]])             # most frequent in window

            while (hi - lo + 1) - maxf > k:           # cost > budget
                count[s[lo]] -= 1                      # remove left
                lo += 1

            res = max(res, hi - lo + 1)

        return res  
        
            
    