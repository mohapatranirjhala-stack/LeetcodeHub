class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if not(0<= r<R and 0<=c<C and board[r][c]==word[i]):
                return False
            char,board[r][c]=board[r][c],'#'

            found = any(dfs(r+dr,c+dc,i+1) for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)))
            board[r][c]=char
            return found
        return any(dfs(r,c,0) for r in range(R) for c in range(C))