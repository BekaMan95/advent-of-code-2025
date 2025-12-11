

def dfs(node: str, dac_found: bool, fft_found: bool):
    if node in visited:
        return 0
    
    if node == "out":
        return 1 if dac_found and fft_found else 0
    
    if (node, dac_found, fft_found) not in cache:
        res = 0
        dac_found = dac_found or (node == "dac")
        fft_found = fft_found or (node == "fft")
        visited.add(node)

        for adj in graph[node]:
            res += dfs(adj, dac_found, fft_found)

        visited.remove(node)
        cache[(node, dac_found, fft_found)] = res

    return cache[(node, dac_found, fft_found)]

visited, graph, cache = set(), dict(), dict()

while True:
    line = input()

    if not line.strip():
        break

    key, lists = line.split(":")

    graph[key] = [s.strip() for s in lists.split(" ") if s]


print(dfs("svr", False, False))

# Done!
