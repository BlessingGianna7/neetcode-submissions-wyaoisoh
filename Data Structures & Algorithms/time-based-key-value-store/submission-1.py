class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)   

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        l = 0
        r = len(self.store[key]) - 1
        values = self.store[key]

        while l <= r:
            m = (l + r) // 2

            if values[m][1] > timestamp:
                r = m - 1
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
      

    
        return res
