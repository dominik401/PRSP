t, sx, sy, ex, ey = map(int, input().split())  # Time and coordinates (sx, sy) -> (ex, ey)
wind = input().strip()  # Wind directions for each second

# Wind direction mappings (east, south, west, north)
dirs = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}

# Current position of the boat
x, y = sx, sy

# Process each wind direction and check if the boat reaches the target
for i in range(t):
    dx, dy = dirs[wind[i]]  # Get the direction change for this second
    x += dx  # Update boat's x-coordinate
    y += dy  # Update boat's y-coordinate

    # Check if the boat has reached the target
    if (x, y) == (ex, ey):
        print(i + 1)  # Output the earliest second (1-based index)
        break
else:
    print(-1)  # If the loop completes without finding the destination, output -1
