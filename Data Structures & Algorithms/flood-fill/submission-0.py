class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColour = image[sr][sc]
        stack = [[sr, sc]]
        seen = set()
        while stack:
            r, c = stack.pop()
            seen.add((r, c))
            if image[r][c] == startColour:
                image[r][c] = color
                for nr, nc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if 0 <= r + nr < len(image) and 0 <= c + nc < len(image[0]) and (r + nr, c + nc) not in seen:
                        stack.append((r + nr, c + nc))
        return image