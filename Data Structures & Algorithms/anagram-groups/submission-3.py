class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            if tuple(chars) not in seen:
                seen[tuple(chars)] = []
            seen[tuple(chars)].append(s)
        return list(seen.values())