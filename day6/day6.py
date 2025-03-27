def solve_guard_patrol(map_lines):
    # Find the guard's starting position
    guard_x, guard_y = None, None
    for y, line in enumerate(map_lines):
        for x, char in enumerate(line):
            if char == '^':
                guard_x, guard_y = x, y
                break
        if guard_x is not None:
            break
    
    # Error handling if no starting position found
    if guard_x is None:
        print("No guard starting position found!")
        return 0
    
    # Track visited positions
    visited_positions = set([(guard_x, guard_y)])
    
    # Directions: up (0), right (1), down (2), left (3)
    # Each direction is represented by (dx, dy)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    current_direction = 0  # Start facing up
    
    # Prevent infinite loop with a maximum number of steps
    max_steps = len(map_lines) * len(map_lines[0]) * 2
    steps = 0
    
    while steps < max_steps:
        # Try to move forward in current direction
        dx, dy = directions[current_direction]
        new_x = guard_x + dx
        new_y = guard_y + dy
        
        # Check if new position is within map and not blocked
        if (0 <= new_y < len(map_lines) and 
            0 <= new_x < len(map_lines[0]) and 
            map_lines[new_y][new_x] != '#'):
            # Move to new position
            guard_x, guard_y = new_x, new_y
            visited_positions.add((guard_x, guard_y))
        else:
            # If blocked, turn right
            current_direction = (current_direction + 1) % 4
        
        # Check if guard has left the map
        if (guard_x < 0 or guard_x >= len(map_lines[0]) or
            guard_y < 0 or guard_y >= len(map_lines)):
            break
        
        steps += 1
    
    return len(visited_positions)

# Read the map from a file
def read_map_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Main program
def main():
    # Read the map from file
    filename = 'example.txt'
    map_lines = read_map_file(filename)
    
    # Solve the puzzle
    unique_positions = solve_guard_patrol(map_lines)
    
    # Print the result
    print(f"The guard will visit {unique_positions} distinct positions.")

# Run the main program
if __name__ == "__main__":
    main()