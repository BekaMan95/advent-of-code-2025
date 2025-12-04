import sys
from collections import defaultdict, deque


def inbound(a: int, b: int) -> bool:
    return 0 <= a < rows and 0 <= b < cols

def helper(r: int, c: int) -> int:
    ans = 0
    
    for nr, nc in directions:
        nr += r
        nc += c

        if inbound(nr, nc) and grid[nr][nc] == "@":
            ans += 1 

    return ans

grid = list()
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    grid.append(list(line))

rows, cols, count = len(grid), len(grid[0]), defaultdict(int)
que, visited = deque(), set()

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            count[(r, c)] = helper(r, c)

            if count[(r, c)] < 4:
                que.append((r, c))
                visited.add((r, c))
                
                

while que:
    r, c = que.popleft()
    grid[r][c] = "."

    for nr, nc in directions:
        nr += r
        nc += c

        if inbound(nr, nc) and grid[nr][nc] == "@":
            count[(nr, nc)] -= 1

            if count[(nr, nc)] < 4 and (nr, nc) not in visited:
                que.append((nr, nc))
                visited.add((nr, nc))

print(len(visited))

# Done!
