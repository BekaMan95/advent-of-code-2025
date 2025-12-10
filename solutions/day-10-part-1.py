

def switch(current: str, button: list[int]) -> str:
    switched = list(current)

    for idx in button:
        switched[idx] = "." if switched[idx] == "#" else "#"
    
    return "".join(switched)

def dfs(steps: int, state: str) -> int:
    if state == indicator:
        return steps
    
    if steps == len(state) * len(buttons):
        return 10**9 + 7
    
    if (steps, state) not in cache:
        ans = 10**9 + 7

        for button in buttons:
            ans = min(ans, dfs(steps + 1, switch(state, button)))
        
        cache[(steps, state)] = ans
    
    return cache[(steps, state)]


res = 0

while True:
    line = input()

    if not line.strip():
        break
    
    machine, buttons = line.split(" "), list()
    indicator, cache = machine[0][1:-1], dict()
    
    for s in machine[1:-1]:
        buttons.append(tuple(map(int, s[1:-1].split(","))))

    res += dfs(0, "." * len(indicator))


print(res)

# Done!
