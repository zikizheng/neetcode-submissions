class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, i = 0, 0
        while i < len(s):
            while s[i] != "#":
                l = l * 10 + (ord(s[i]) - ord('0'))
                i += 1
            st = s[i + 1: i + l + 1]
            res.append(st)
            i = i + l + 1
            l = 0
        return res