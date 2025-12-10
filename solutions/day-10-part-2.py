

def switch(current: tuple, button: list[int]) -> tuple:
    switched = list(current)

    for idx in button:
        switched[idx] += 1

        if switched[idx] > joltage[idx]:
            return tuple()
    
    return tuple(switched)


def dfs(state: tuple) -> int:
    if state == joltage:
        return 0
    
    if not state:
        return 10**9 + 7
    
    if state not in cache:
        ans = 10**9 + 7

        for button in buttons:
            nxt = switch(state, button)
            if nxt:
                ans = min(ans, 1 + dfs(nxt))
        
        cache[state] = ans
    
    return cache[state]


res = 0

while True:
    line = input()

    if not line.strip():
        break
    
    machine, buttons = line.split(" "), list()
    joltage, cache = tuple(map(int, machine[-1][1:-1].split(","))), dict()
    
    for s in machine[1:-1]:
        buttons.append(tuple(map(int, s[1:-1].split(","))))

    res += dfs(tuple([0]) * len(joltage))


print(res)

# Unsolved!
