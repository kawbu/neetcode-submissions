class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def bfs(r, c, i):
            if len(word) == i:
                return True
            if (r >= rows or c >= cols or c < 0 or r < 0 or board[r][c] != word[i] or (r, c) in visited):
                return False
            visited.add((r, c))
            res = (bfs(r + 1, c, i + 1) or bfs(r, c + 1, i + 1) 
            or bfs(r - 1, c, i + 1) or bfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if (bfs(r, c, 0)):
                    return True
        return False
        