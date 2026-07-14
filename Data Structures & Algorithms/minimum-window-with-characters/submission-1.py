class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        T, window = {}, {}

        for c in t:
            T[c] = T.get(c, 0) + 1

        l = 0
        have, need = 0, len(T)
        res = [-1, -1]
        resLen = float("infinity")
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            if s[r] in T and window[s[r]] == T[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in T and window[s[l]] < T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""