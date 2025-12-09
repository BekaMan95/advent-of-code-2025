
res, points = 0, list()

while True:
    line = input()

    if not line.strip():
        break
    
    col, row = map(int, line.split(","))
    points.append((row, col))

for i in range(len(points) - 1):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        res = max(res, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))


print(res)

# Done!
