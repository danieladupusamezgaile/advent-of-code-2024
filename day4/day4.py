import os
def count_xmas_occurrences(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Directions: (dx, dy) for 8 possible movements (horizontal, vertical, diagonal)
    directions = [
        (1, 0),   # Right
        (-1, 0),   # Left
        (0, 1),    # Down
        (0, -1),   # Up
        (1, 1),    # Down-Right
        (1, -1),   # Up-Right
        (-1, 1),   # Down-Left
        (-1, -1),  # Up-Left
    ]

    for y in range(rows):
        for x in range(cols):
            for dx, dy in directions:
                # Check if the next 4 characters match "XMAS" in this direction
                matched = True
                for i in range(target_len):
                    nx = x + i * dx
                    ny = y + i * dy
                    if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                        matched = False
                        break
                    if grid[ny][nx] != target[i]:
                        matched = False
                        break
                if matched:
                    count += 1
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Example usage
if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "example.txt")
    try:
        grid = read_grid_from_file(filename)
        occurrences = count_xmas_occurrences(grid)
        print(f"Total occurrences of 'XMAS': {occurrences}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")