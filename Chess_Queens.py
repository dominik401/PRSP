# Input: Read the 8x8 board.
board = [input().strip() for _ in range(8)]

# Initialize variables for the count of solutions and sets for column and diagonal tracking.
count = 0  # Tracks valid configurations.
columns, diag1, diag2 = set(), set(), set()  # Sets to track used columns and diagonals.

# Backtracking function to place queens row by row.
def place(row=0):
    global count
    if row == 8:  # Base case: All 8 queens are placed.
        count += 1  # Found a valid configuration.
        return
    for col in range(8):  # Iterate over columns in the current row.
        if board[row][col] == '.' and col not in columns and (row + col) not in diag1 and (row - col) not in diag2:
            # Place a queen: Mark column and diagonals as used.
            columns.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            place(row + 1)  # Recur to place the next queen.
            # Backtrack: Unmark the column and diagonals.
            columns.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

place()  # Start placing queens from the first row.
print(count)  # Output the total number of valid configurations.
