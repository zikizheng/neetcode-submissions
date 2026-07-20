class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append([value, timestamp])
        else:
            self.values[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        v = self.values[key]

        res = ""
        l, r = 0, len(v) - 1

        while l <= r:
            m = l + (r - l) // 2
            if v[m][1] <= timestamp:
                res = v[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
