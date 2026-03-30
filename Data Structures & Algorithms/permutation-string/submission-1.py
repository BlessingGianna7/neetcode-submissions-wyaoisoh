class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        count1 = {}
        count2 = {}

        # fill count1 with s1 frequencies
        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        # fill count2 with FIRST WINDOW of s2 (size = len(s1))
        for c in s2[:len(s1)]:
            count2[c] = count2.get(c, 0) + 1

        # check first window
        if count1 == count2:
            return True

        # slide window across s2
        k = len(s1)
        for i in range(k, len(s2)):
            # add new right char
            count2[s2[i]] = count2.get(s2[i], 0) + 1

            # remove old left char
            left = s2[i - k]
            count2[left] -= 1
            if count2[left] == 0:
                del count2[left]

            # check window
            if count1 == count2:
                return True

        return False