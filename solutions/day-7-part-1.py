
res, grid = 0, list()

while True:
    line = input()

    if not line.strip():
        break

    grid.append(line)
    

rows, cols, beams = len(grid), len(grid[0]), set()

for i in range(cols):
    if grid[0][i] == "S":
        beams.add(i)

for r in range(1, rows):
    prev_row = beams.copy()
    for c in range(cols):
        if grid[r][c] == "^" and c in beams:
            prev_row.remove(c)
            res += 1

            if 0 <= c - 1 < cols:
                prev_row.add(c - 1)
            
            if 0 <= c + 1 < cols:
                prev_row.add(c + 1)
    
    beams = prev_row


print(res)

# Done!
