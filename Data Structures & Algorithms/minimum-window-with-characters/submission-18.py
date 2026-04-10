class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        l = 0
        res_len = float('inf')
        res = ""
        formed = 0
        required = len(need)

        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                formed += 1

            while formed == required:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

        return res