# Input: Read the 48-character path description.
path = input().strip()

# Initialize variables for the grid dimensions, result counter, and the grid's visited status.
res, visited = 0, [[False] * 7 for _ in range(7)]  # Result counter and visited grid.

# Directions: Down, Up, Left, Right and their respective coordinate changes.
dirs = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}

# Recursive function for backtracking.
def dfs(x, y, step):
    global res
    if x == 6 and y == 0 and step == 48:  # Base case: reached the end at the 48th step.
        res += 1
        return
    if not (0 <= x < 7 and 0 <= y < 7) or visited[x][y]:  # Out of bounds or already visited.
        return
    visited[x][y] = True  # Mark the current cell as visited.
    
    if step < 48:  # Ensure we do not go beyond the path length.
        move = path[step]
        if move in dirs:  # Fixed direction.
            dx, dy = dirs[move]
            dfs(x + dx, y + dy, step + 1)
        else:  # '?' wildcard: Try all directions.
            for dx, dy in dirs.values():
                dfs(x + dx, y + dy, step + 1)

    visited[x][y] = False  # Backtrack: Unmark the current cell.

dfs(0, 0, 0)  # Start from the top-left corner at step 0.
print(res)  # Output the total number of valid paths.
