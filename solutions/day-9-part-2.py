

res, points, max_bound = 0, list(), 10**5 + 1
row_bound = {i: [max_bound, -1] for i in range(max_bound)}
col_bound = {i: [max_bound, -1] for i in range(max_bound)}

while True:
    line = input()

    if not line.strip():
        break
    
    col, row = map(int, line.split(","))
    points.append((row, col))
    row_bound[row][0] = min(row_bound[row][0], col)
    row_bound[row][1] = max(row_bound[row][1], col)
    col_bound[col][0] = min(col_bound[col][0], row)
    col_bound[col][1] = max(col_bound[col][1], row)


for i in range(len(points) - 1):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]


print(res)

# Unsolved!
