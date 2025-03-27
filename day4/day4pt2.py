def find_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    x_mas_count = 0
    
    # Check every possible center point
    for x_row in range(rows):
        for x_col in range(cols):
            # Check all 8 directions from the center
            x_mas_count += check_eight_directions(grid, x_row, x_col)
    
    return x_mas_count

def check_eight_directions(grid, x_row, x_col):
    directions = [
        (0, 1),    # Right
        (0, -1),   # Left
        (1, 0),    # Down
        (-1, 0),   # Up
        (1, 1),    # Down-Right
        (1, -1),   # Down-Left
        (-1, 1),   # Up-Right
        (-1, -1)   # Up-Left
    ]
    
    x_mas_count = 0
    
    # Try each direction for the MAS patterns
    for first_dir in directions:
        for second_dir in directions:
            # Skip if directions are the same to prevent duplicates
            if first_dir == second_dir:
                continue
            
            # Check if X-MAS pattern exists with these directions
            if is_x_mas_pattern(grid, x_row, x_col, first_dir, second_dir):
                x_mas_count += 1
    
    return x_mas_count

def is_x_mas_pattern(grid, x_row, x_col, first_dir, second_dir):
    rows, cols = len(grid), len(grid[0])
    
    # Ensure we're at a valid grid position
    if not (0 <= x_row < rows and 0 <= x_col < cols):
        return False
    
    # Check both possible MAS configurations
    first_configs = [
        (['M', 'A', 'S'], first_dir),
        (['S', 'A', 'M'], first_dir)
    ]
    second_configs = [
        (['M', 'A', 'S'], second_dir),
        (['S', 'A', 'M'], second_dir)
    ]
    
    # Try all possible MAS configurations
    for first_pattern, first_offset in first_configs:
        for second_pattern, second_offset in second_configs:
            if check_mas_pattern(grid, x_row, x_col, first_pattern, first_offset) and \
               check_mas_pattern(grid, x_row, x_col, second_pattern, second_offset):
                return True
    
    return False

def check_mas_pattern(grid, x_row, x_col, pattern, direction):
    rows, cols = len(grid), len(grid[0])
    dx, dy = direction
    
    # Check each letter of the pattern
    for i, letter in enumerate(pattern):
        check_row = x_row + i * dx
        check_col = x_col + i * dy
        
        # Validate position and letter
        if not (0 <= check_row < rows and 0 <= check_col < cols):
            return False
        
        if grid[check_row][check_col] != letter:
            return False
    
    return True

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def main():
    # Example grid for testing
    grid = [
        list(".M.S......"),
        list("..A..MSMS."),
        list(".M.S.MAA.."),
        list("..A.ASMSM."),
        list(".M.S.M...."),
        list(".........."),
        list("S.S.S.S.S."),
        list(".A.A.A.A.."),
        list("M.M.M.M.M."),
        list("..........")
    ]
    
    # Find X-MAS patterns
    x_mas_count = find_x_mas_patterns(grid)
    
    # Print result
    print(f"Number of X-MAS patterns: {x_mas_count}")

# Run the main program
if __name__ == "__main__":
    main()