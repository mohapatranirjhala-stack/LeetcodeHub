class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return[]
        ROWS,COLS=len(heights),len(heights[0])
        pac,atl=set(),set()
        
        def dfs(r,c,visit,prev_h):
            if (r,c) in visit or not(0 <= r<ROWS and 0<=c<COLS) or heights[r][c]<prev_h:
                return
            visit.add((r,c))
            for dr,dc in[(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(r+dr,c+dc,visit,heights[r][c])
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        return list(pac & atl)
