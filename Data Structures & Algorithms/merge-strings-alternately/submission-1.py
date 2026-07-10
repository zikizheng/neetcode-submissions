class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        while i < min(len(word1), len(word2)):
            res += word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            res += word1[i:len(word1)]
        else:
            res += word2[i:len(word2)]
        return res