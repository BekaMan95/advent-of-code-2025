from math import sqrt
from collections import Counter
import heapq


res, points = 1, list()

while True:
    line = input()

    if not line.strip():
        break
    
    x, y, z = map(int, line.split(","))
    points.append((x, y, z))

heap = list()

for i in range(len(points) - 1):
    x1, y1, z1 = points[i]

    for j in range(i + 1, len(points)):
        x2, y2, z2 = points[j]
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        heapq.heappush(heap, (dist, i, j))

group_id, group_map = 0, dict()

for _ in range(1000):
    if not heap:
        break

    _, i, j = heapq.heappop(heap)

    if i in group_map and j in group_map:
        cur_id = group_map[i]
        other_id = group_map[j]

        for key in group_map:
            if group_map[key] == other_id:
                group_map[key] = cur_id
    elif i in group_map:
        group_map[j] = group_map[i]
    elif j in group_map:
        group_map[i] = group_map[j]       
    else:
        group_map[i] = group_id
        group_map[j] = group_id
        group_id += 1

top_3_circuits = Counter(group_map.values()).most_common(3)

for _, freq in top_3_circuits:
    res *= freq

print(res)

# Done!
