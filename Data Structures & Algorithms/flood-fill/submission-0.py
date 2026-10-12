
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        start = image[sr][sc]

        def bfs(r,c):
            if r == ROWS or c == COLS: return 
            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            dq = deque()
            dq.append((r,c))
            visited = set()
            visited.add((r,c))
            image[r][c]=color

            while dq:
                cr, cc = dq.popleft()
                for nr, nc in neighbors:
                    nr = cr + nr
                    nc = cc + nc
                    if not (0<=nr<ROWS and 0<=nc<COLS) or (nr,nc) in visited or image[nr][nc] != start:
                        continue
                    dq.append((nr,nc))
                    visited.add((nr,nc))
                    image[nr][nc]=color
        bfs(sr,sc)
        return image
        