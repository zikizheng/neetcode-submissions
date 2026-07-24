class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((timestamp, value))
        else:
            self.mp[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        res = ""
        v = self.mp[key]
        l, r = 0, len(v) - 1
        while l <= r:
            m = l + (r - l) // 2
            if v[m][0] <= timestamp:
                res = v[m][1]
                l = m + 1
            else:
                r = m - 1
        return res