class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {"}" : "{", "]" : "[", ")" : "("}
        seen = []
        for c in s:
            if c in openToClose:
                if seen and seen[-1] == openToClose[c]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(c)
        return not seen