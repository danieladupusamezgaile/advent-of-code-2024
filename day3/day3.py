import re
import os

def sum_valid_multiplications(corrupted_memory):
    # Find all valid mul(X,Y) instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, corrupted_memory)
    
    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        total += x * y
    
    return total

def sum_enabled_multiplications(corrupted_memory):
    # Regex patterns
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'  # Note: escaped apostrophe
    
    enabled = True  # Initial state
    total = 0

    # Scan the string character by character to handle overlapping patterns
    i = 0
    n = len(corrupted_memory)
    while i < n:
        # Check for 'do()'
        if corrupted_memory.startswith('do()', i):
            enabled = True
            i += 4  # Skip past 'do()'
            continue
        # Check for 'don't()'
        elif corrupted_memory.startswith("don't()", i):
            enabled = False
            i += 7  # Skip past "don't()"
            continue
        # Check for 'mul(X,Y)'
        mul_match = re.match(mul_pattern, corrupted_memory[i:])
        if mul_match and enabled:
            x, y = map(int, mul_match.groups())
            total += x * y
            i += mul_match.end()  # Skip past the matched 'mul(X,Y)'
        else:
            i += 1  # Move to next character if no match

    return total

def read_corrupted_memory(filename):
    with open(filename, 'r') as file:
        return file.read()

# Example usage
if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "corruptedMemory.txt")
    try:
        corrupted_memory = read_corrupted_memory(filename)
        result = sum_valid_multiplications(corrupted_memory)
        print(f"Total sum of valid multiplications: {result}")
        result2 = sum_enabled_multiplications(corrupted_memory)
        print(f"Total sum of enabled multiplications: {result2}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename and path.")