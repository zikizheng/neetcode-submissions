class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.timemap[key]
        if len(ls) == 0:
            return ""
        l, r = 0, len(ls) - 1
        while l <= r:
            m = l + (r - l) // 2
            if ls[m][0] == timestamp:
                return ls[m][1]
            elif ls[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return ls[r][1] if ls[r][0] <= timestamp else ""
