# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         k = 1
        
#         arr = []
#         for i in range(max(piles)):
#             arr.append(i)

#         l = arr[0]
#         r = arr[len(arr) - 1]   

#         while l < r:
#             m = (l + r) // 2
#             hours = 0
#             for i in range(len(piles)):
#                 hours += math.ceil(piles[i] / arr[m])

#             k = min(k, arr[m])
#             if hours > h:
#                 l = m + 1
#             if hours < h:
#                 r = m - 1    

#         return k
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)

            if hours <= h:
                r = m       # speed works, try slower
            else:
                l = m + 1   # too slow, need faster

        return l