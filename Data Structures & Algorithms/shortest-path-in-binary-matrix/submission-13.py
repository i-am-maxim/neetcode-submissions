class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs():
            neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
            dq = deque()
            if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
                return -1
            dq.append((0,0))
            grid[0][0] = 1
            level = 1
            while dq:
                for i in range(len(dq)):
                    cr, cc = dq.popleft()
                    if cr == ROWS-1 and cc==COLS-1:
                        return level 
                    grid[cr][cc] = 1
                    for r,c in neighbors:
                        r = cr + r
                        c = cc + c
                        if 0<=r<ROWS and 0<=c<COLS and grid[r][c]==0:
                            if r == ROWS-1 and c==COLS-1:
                                return level+1
                            dq.append((r,c))
                            grid[r][c] = 1
                level += 1
            return -1 
        return bfs()

        