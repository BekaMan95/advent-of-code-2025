

def dfs(node: str):
    if node in visited:
        return 0
    
    if node == "out":
        return 1 if "dac" in visited and "fft" in visited else 0
    
    res = 0
    visited.add(node)

    for adj in graph[node]:
        res += dfs(adj)

    visited.remove(node)

    return res

visited, graph = set(), dict()

while True:
    line = input()

    if not line.strip():
        break

    key, lists = line.split(":")

    graph[key] = [s.strip() for s in lists.split(" ") if s]


print(dfs("svr"))

# Unsolved!
