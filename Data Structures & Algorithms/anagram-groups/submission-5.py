class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            charFreq = [0] * 26
            for i in range(len(s)):
                charFreq[ord(s[i]) - ord('a')] += 1
            mp[tuple(charFreq)] = mp.get(tuple(charFreq), []) + [s]
        return list(mp.values())