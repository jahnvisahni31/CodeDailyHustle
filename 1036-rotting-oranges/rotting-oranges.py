class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        fr = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fr += 1
        mini = 0
        while queue and fr:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fr -= 1
                        queue.append((nx, ny))
            mini += 1

        return mini if fr == 0 else -1