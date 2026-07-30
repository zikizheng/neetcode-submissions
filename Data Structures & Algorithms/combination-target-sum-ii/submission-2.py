class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, s):
            if s == target:
                res.append(curr.copy())
                return

            if i == len(candidates) or s > target:
                return

            curr.append(candidates[i])
            dfs(i + 1, curr, s + candidates[i])
            curr.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, s)

        dfs(0, [], 0)
        return res